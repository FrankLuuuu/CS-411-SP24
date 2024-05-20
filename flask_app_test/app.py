from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import pymysql
import bcrypt
from dotenv import load_dotenv, dotenv_values
import sqlalchemy
import os
import mysql

app = Flask(__name__)
load_dotenv()
connection = pymysql.connect(
    host='35.184.94.222',
    user='root',
    password='password',
    database='projectdb',
    cursorclass=pymysql.cursors.DictCursor
)



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search_meals', methods=['GET'])
def search_meals():
    return render_template('search_meals.html')


@app.route('/api/meal_details', methods=['GET'])
def meal_details():
    meal_name = request.args.get('meal_name', '')
    with connection.cursor() as cursor:
        sql = "SELECT * FROM dish WHERE mealName = %s;"
        cursor.execute(sql, (meal_name,))
        meal_details = cursor.fetchone() 
        print("printing meal details")
        print(meal_details)
        if meal_details:
            print(f"Details fetched for meal: {meal_name}")
        else:
            print("No details found for the meal.")
            meal_details = {}
    return jsonify(meal_details)

@app.route('/api/search_meals', methods=['GET'])
def api_search_meals():
    query = request.args.get('query', '')
    with connection.cursor() as cursor:
            sql = "SELECT mealName from dish limit 100;"
            cursor.execute(sql)
            connection.commit()
            print(cursor.lastrowid)
            dishes_result = cursor.fetchall()
    dishes_result_json = jsonify(dishes_result)
    
    meal_names = [dish['mealName'] for dish in dishes_result]
    print(meal_names)
    all_meals = ['Apple Pie', 'Banana Bread', 'Carrot Cake', 'Doughnut', 'Eclair']
    filtered_meals = [meal for meal in meal_names if query.lower() in meal.lower()]
    return jsonify(filtered_meals)


@app.route('/fetch_pantry', methods=['POST'])
def fetch_pantry():
    user_id = request.form.get('user_id')
    print("Fetching pantry for User ID:", user_id)
    return redirect(url_for('show_pantry', user_id=user_id))

@app.route('/pantry/<user_id>', methods=['GET','POST'])
def show_pantry(user_id):
    print("Showing pantry for User ID:", user_id)
   
    with connection.cursor() as cursor:
        sql = """
        SELECT i.ingredientName
        FROM users u
        JOIN userpantries up ON u.UID = up.memberID
        JOIN pantry p ON up.pantryID = p.pantryID
        JOIN ingredients i ON p.ingredientID = i.ingredientID
        WHERE u.UID = %s;
        """
        cursor.execute(sql, (user_id,))
        pantry_items_ = cursor.fetchall()
        print(pantry_items_)

    pantry_items = ["garlic", "onion"]
    if request.method == 'POST':
        item = request.form.get('item_name')
        if item:
            
            print(item)
            with connection.cursor() as cursor:
                sql = """
                SELECT pantryID from userpantries where memberID = %s;
                """
                cursor.execute(sql, user_id)
                result = cursor.fetchone()
                pantryid = result['pantryID'] 

                print(pantryid)
                sql = """
                CALL AddIngredientToPantry(%s, %s, %s, 1);
                """
                cursor.execute(sql, (user_id, pantryid,item))
                print("item")
        return redirect(url_for('show_pantry', user_id=user_id))  # Redirect to clear the form
    return render_template('pantry.html', user_id=user_id, pantry_items=pantry_items_)

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form.get('user_id')
        name = request.form.get('name')
        allergies = request.form.get('allergies')
        plain_password = request.form.get('password')
        hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        print(f"Creating user with User ID: {username}, Name: {name}, Allergies: {allergies}")
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (username, password_hash, name, allergies) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (username,hashed_password , name, allergies))
            connection.commit()

            
            uid = cursor.lastrowid
       
        message = 'User successfully created!'
        return render_template('create_user.html', message=message)
        return redirect(url_for('index'))
    return render_template('create_user.html')

@app.route('/add_item_to_pantry', methods=['POST'])
def add_item_to_pantry():
    user_id = request.form.get('user_id')
    item_name = request.form.get('item_name')
    print(f"Adding item {item_name} to pantry for User ID {user_id}")
    return redirect(url_for('show_pantry', user_id=user_id))

@app.route('/meal_plan/<user_id>', methods=['GET'])
def show_meal_plan(user_id):
    print("Displaying meal plan for User ID:", user_id)
    return render_template('meal_plan.html', user_id=user_id)

@app.route('/search_by_ingredients', methods=['GET'])
def search_by_ingredients():
    return render_template('search_by_ingredients.html')

# @app.route('/api/search_by_ingredients', methods=['GET'])
# def api_search_by_ingredients():
#     ingredients = request.args.get('ingredients', '')
#     ingredient_list = [i.strip() for i in ingredients.split(',')]
#     with connection.cursor() as cur:
#         grab = 'select ingredientID from ingredients where ingredientName like %s'
#         grabbed = []
#         for ing in ingredient_list:
#             ingr = f"%{ing}%"
#             cur.execute(grab, ingr)
#             grabbed.append(cur.fetchall()) 
#             print(grabbed)
#             #creates a 2d array of ingredents like
#             #grabbed = [[1,6,3],
#             #           [2,14,75],
#             #           [20,36,45,345]]

#         grabdish = 'select dishID from dishIngredients where ingredientsID = %s intersect select dishID from dishIngredients where ingredientsID = %s intersect select dishID from dishIngredients where ingredientsID = %s'
#         grabbeddish = []
#         for i in range(len(grabbed[0])):
#             for j in range(len(grabbed[1])):
#                 for k in range(len(grabbed[2])):
#                     ingredients = (grabbed[0][i].values,grabbed[1][j].values,grabbed[2][k].values)
#                     cur.execute(grabdish, ingredients)
#                     grabbeddish.append(cur.fetchall())

#         dishname = []
#         grabdishname = 'select mealName from dish where dishID = %s'
#         for i in range(len(grabbeddish)):
#             dishname.append(cur.execute(grabdishname, grabbeddish[i]))

#     return jsonify(dishname)

@app.route('/update_allergies', methods=['GET', 'POST'])
def update_allergies():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        allergy = request.form.get('allergy')
        try:
            with connection.cursor() as cursor:
                # Update the allergies information for a given user
                cursor.execute("update users set allergies = %s where UID = %s;", (allergy, user_id))
                connection.commit()
                message = 'Allergies updated successfully!'
                return render_template('update_allergies.html', message='Allergies updated successfully!')
        except Exception as e:
            return render_template('update_allergies.html', message=f'Failed to update allergies. Error: {str(e)}')
    else:
        return render_template('update_allergies.html')


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE UID = %s", (user_id,))
            connection.commit()
            
        return render_template('delete_user.html', message='User successfully deleted!')
    return render_template('delete_user.html')


@app.route('/api/search_by_ingredients', methods=['GET'])
def api_search_by_ingredients():
    ingredients = request.args.get('ingredients', '')
    ingredient_list = [i.strip() for i in ingredients.split(',')]
    with connection.cursor() as cur:
        
        grab = 'SELECT ingredientID FROM ingredients WHERE ingredientName LIKE %s'
        ingredient_ids = []
        for ing in ingredient_list:
            like_pattern = f"%{ing}%"
            cur.execute(grab, (like_pattern,))
            fetched = cur.fetchall()
            if fetched:
                
                ingredient_ids.extend([item['ingredientID'] for item in fetched])
        
       
        if not ingredient_ids:
            return jsonify([])

        
        placeholders = ', '.join(['%s'] * len(ingredient_ids))
        sql = f"""
            SELECT dishID, COUNT(DISTINCT ingredientsID) AS matched_ingredients
            FROM dishIngredients
            WHERE ingredientsID IN ({placeholders})
            GROUP BY dishID
            HAVING matched_ingredients = {len(ingredient_list)}
        """
        cur.execute(sql, ingredient_ids)
        dish_ids = cur.fetchall()

        
        dish_names = []
        if dish_ids:
            placeholders = ', '.join(['%s'] * len(dish_ids))
            grab_dish_name = f"SELECT mealName AS meal, description AS meal_description FROM dish WHERE dishID IN ({placeholders})"
            cur.execute(grab_dish_name, [dish['dishID'] for dish in dish_ids])
            dish_names = cur.fetchall()

        return jsonify(dish_names)
    

@app.route('/dietary_restrictions', methods=['GET'])
def dietary_restrictions():
    user_id = 1  
    try:
        with connection.cursor() as cursor:
            connection.begin()
            
            cursor.execute("""
                SELECT dishID, mealName FROM dish d1 NATURAL JOIN dishIngredients 
                WHERE NOT EXISTS( SELECT 1 FROM users JOIN ingredients ON allergies = 
                ingredientName JOIN dishIngredients ON ingredientsID = ingredientID WHERE 
                dishID = d1.dishID and users.UID = 1) GROUP BY dishID, mealName;
            """)
            result1 = cursor.fetchall()

            
            cursor.execute("""
                SELECT name, mealName FROM users JOIN ingredients ON 
                users.allergies = ingredients.ingredientName JOIN 
                dishIngredients ON ingredients.ingredientID = 
                dishIngredients.ingredientsID JOIN dish ON dishIngredients.dishID 
                = dish.dishID GROUP BY name, mealname ORDER BY name;
            """)
            result2 = cursor.fetchall()

            connection.commit()
    except pymysql.Error as e:
        print("Error:", e)
        connection.rollback()
        return render_template('dietary_restrictions.html', message=f"Error fetching data: {str(e)}")
    
    return render_template('dietary_restrictions.html', result1=result1, result2=result2)

