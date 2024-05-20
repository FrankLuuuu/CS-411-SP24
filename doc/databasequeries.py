### this references my (kyt3) work from CS461

import os, sys
import pymysql as mdb
from bottle import FormsDict
from hashlib import md5

# connection to database project2
def connect():
    """
    Creates a connection object to the MySQL database.
    @return a mysqldb connection object.
    """

    # this should be right but confirm

    return mdb.connect(host='35.184.94.222', user='root', password='password', db='projectdb')

def createUser(username, password, name, allergies):
    """
    Creates a row in table named `users`
    @param username: username of user
    @param password: password of user
    """

    db_rw = connect()
    cur = db_rw.cursor()
    password_hash = str(md5(password.encode('utf-8')).hexdigest()) #should i use os.urandome or whatever thisis
    
    action = ('insert into users (username, password_hash, name, allergies) values (%s, %s, %s, %s)')  
    entry = (username, password, name, allergies)                      #the entry    
    cur.execute(action, entry)                                      #insert

    db_rw.commit()

def validateUser(username, password):
    """ validates if username,password pair provided by user is correct or not
    @param username: username of user
    @param password: password of user
    @return True if validation was successful, False otherwise.
    """

    db_rw = connect()
    cur = db_rw.cursor()

    pw_hash = md5(password.encode('utf-8')).hexdigest()
    
    action = ('SELECT username, password_hash FROM users WHERE username = %s AND password = %s')
    check = (username, pw_hash)

    cur.execute(action,check)       #holds count 

    if cur.rowcount < 1:        # user does not exist
        return False
    
    return True

def fetchUser(username):
    """ checks if there exists given username in table users or not
    if user exists return (id, username) pair
    if user does not exist return None
    @param username: the username of a user
    @return The row which has username is equal to provided input
    """

    db_rw = connect()
    cur = db_rw.cursor(mdb.cursors.DictCursor)
    
    action = ('SELECT id, username FROM users WHERE username = %s')
    check = username

    cur.execute(action, check)

    if cur.rowcount < 1:
        return None    
    return FormsDict(cur.fetchone())



# does not apply to us unless we want to use these
# def addHistory(user_id, query):
#     """ adds a query from user with id=user_id into table named history
#     @param user_id: integer id of user
#     @param query: the query user has given as input
#     """

#     db_rw = connect()
#     cur = db_rw.cursor()
    
#     action =('insert into history (user_id, query) values (%s, %s)')
#     edit = (user_id, query)

#     cur.execute(action, edit)

#     db_rw.commit()

# def getHistory(user_id):
#     """ grabs last 15 queries made by user with id=user_id from
#     table named history in descending order of when the searches were made
#     @param user_id: integer id of user
#     @return a first column of a row which MUST be query
#     """

#     db_rw = connect()
#     cur = db_rw.cursor()
    
#     action = ('select query from history where user_id = %s order by id desc')
    
#     user = user_id
#     cur.execute(action, user)

#     rows = cur.fetchall()
#     if len(rows) > 15:
#         return [row[0] for row in rows[-15:]]
#     return [row[0] for row in rows]

def getvalidmeals(user_id):
    db_rw = connect()
    cur = db_rw.cursor()
    
    action = ('select dishID, mealName from dish d1 natural join dishIngredients where not exists ( select 1 from users join ingredients on allergies = ingredientName join dishIngredients di on ingredientsID = ingredientID where di.dishID = d1.dishID and users.UID = 1) group by dishID, mealName limit 15;')

    user = user_id
    cur.execute(action, user)

    rows = cur.fetchall()
    if len(rows) > 15:
        return [row[0] for row in rows[-15:]]
    return [row[0] for row in rows]
