# Plate Pal

Potential Tables:

- Cuisine (meals in the cuisine)
- Ingredients (of everything, regardless of meal)
- Recipes (contains recipes, ingredients, amounts, instructions)
- Caloric intake (output of calculation if we need an extra table)
- Grocery stores (if need to get ingredients)
- Users (first name, last name, uid, password)
- Users' ingredients (in pantry of user)
- Meal Plan (tracks users meals that have been made, amount, and macros)
- Grocery List (takes a meal as an ID, provides ingredients and amounts for each meal)

## Project Summary 

In this project, we want to use a recipe dataset to help users find a meal recipe that utilizes the ingredients that they have on hand. If they are missing any ingredients from the recipe, a list of nearby grocery stores will be generated for them to choose where to get the necessary ingredients. We will also have other features like cuisine generation and meal plan storage to help the user select and manage the meals that they want.

## Project Description 

Numerous people find themselves with a collection of ingredients on hand but lack ideas on what to prepare with them, leading to potential wastage. This project offers a solution by enabling users to input their available ingredients and discover recipes tailored to their inventory. This empowers users to experiment with new dishes and make the most of their ingredients, minimizing waste and fostering culinary exploration.

Key Features:

1. Ingredient Input: Users input the ingredients they have available, either manually or through a convenient search feature.
2. Cuisine Selection: Users can specify their desired cuisine or select from a list of available options, allowing for a more tailored recipe recommendation.
3. Recipe Generation: The system analyzes the user's input ingredients and desired cuisine preferences, then retrieves relevant recipes from the database.
4. Threshold Management: The system incorporates a threshold mechanism to ensure that recipes are still suggested even if the user does not have all the required ingredients. The threshold allows for flexibility in ingredient availability while still ensuring the quality and relevance of recipe suggestions.
5. User Interface: The web-based interface provides a user-friendly experience, with intuitive controls for ingredient input, cuisine selection, and recipe browsing.
6. Recipe Details: Each recipe suggestion includes detailed instructions, ingredient lists, cooking times, and optional variations to accommodate different preferences and dietary restrictions.
7. Database Integration: The system connects to a centralized recipe database, continuously updated with new recipes and cuisines, ensuring a diverse selection of meal options for users.
8. Customization Options: Users can customize their experience by filtering recipe suggestions based on dietary preferences, cooking difficulty, and other criteria.

## Creative Component 

In our project, we aim to introduce several creative components to enhance the user experience and provide tailored recipe recommendations. One such component involves the development of a Python model capable of classifying recipes into specific cuisines, leveraging a robust training and testing dataset. By utilizing machine learning techniques, this model will accurately categorize recipes based on their ingredients, cooking methods, and other features, allowing users to explore diverse culinary traditions effortlessly. Additionally, we plan to empower users with the ability to customize their experience by implementing advanced filtering options. Users will have the flexibility to refine recipe suggestions according to their dietary preferences, cooking difficulty preferences, and various other criteria, ensuring that the generated recipes align perfectly with their individual tastes and preferences. These creative components not only enhance the functionality of our recipe generator but also foster a more engaging and personalized cooking experience for users of all culinary backgrounds.

## Usefulness Description 

The Smart Recipe Generator with Cuisine Integration project stands out as an exceptionally useful tool in the domain of personal health, nutrition, and culinary exploration. It addresses a common challenge faced by many: the task of meal planning and preparation based on the ingredients already available at home.

Here are some of the basic and unique use-cases for the Smart Recipe Generator:

**Automated Recipe Suggestions**: By enabling users to input their available ingredients and select meals based on specific calorie counts or nutritional requirements, the project directly supports personal health and nutrition goals.

**Cuisine Selection**: The application allows users to explore recipes from various cuisines, enabling them to broaden their culinary horizons and experiment with new flavors and cooking techniques.

**Grocery List and Store Locator**: The project streamlines the meal planning and preparation process, saving users time and effort in searching for recipes that fit their dietary and ingredient availability constraints. Additionally, by providing a grocery list for missing ingredients along with nearby grocery store options, it helps users with a streamlined shopping experience.

**Personalized Cooking Experience**: Through advanced filtering options and the ability to customize recipe suggestions based on dietary preferences, cooking difficulty, and other criteria, the project offers a highly personalized cooking experience.

There are several recipe and meal planning applications available, such as MyFitnessPal, Yummly, and Allrecipes Dinner Spinner. These platforms share some basic features with our application, such as recipe discovery based on ingredients and dietary preferences.

Our application places a significant emphasis on exploring global cuisines, offering users the opportunity to discover meals from different cultural backgrounds, which is not always a focus of other apps. While some apps provide grocery list features, our application enhances this by also suggesting nearby grocery stores, making it a more comprehensive tool for meal planning and preparation.

## Data Sources 

We decided to source one of our datasets from Kaggle. The recipes dataset we are using is called “[Food.com Recipes with Search Terms and Tags](https://www.kaggle.com/datasets/shuyangli94/foodcom-recipes-with-search-terms-and-tags)” and it’s a dataset of crawled data from [Food.com](http://food.com/) (GeniusKitchen) online recipe aggregator. The dataset is in CSV format and is around 800 MB in size. It has around 500,000 tuples with 10 attributes each. The main attributes being the recipe name, the list of ingredients, and the recipe instructions. Since it contains food recipes and the ingredients that are needed, we will mainly use this dataset to search for recipes given the available ingredients.

Another source we have found is data.world where we found a dataset of the locations of grocery stores in the US. The dataset is called “[Grocery Stores](https://data.world/usda/grocery-stores)” and it’s created by the US Department of Agriculture. It’s a CSV dataset of around 33 MB in size and it has 72,864 rows with 64 columns each. We will likely use this dataset to search for the grocery stores near the user.

## Functionality Description 

The application will function as a user-friendly platform where individuals can easily discover and create personalized recipes based on their available ingredients and culinary preferences. Upon accessing the application, users will be greeted with a clean and intuitive interface where they can input the ingredients they currently have on hand. They can either manually enter each ingredient or utilize a convenient search feature to quickly add items from a pre-populated list.

Once the user has inputted their ingredients, they will have the option to further customize their recipe suggestions by selecting their desired cuisine preferences. The application will offer a diverse range of cuisines to choose from, ensuring that users can explore and experiment with various culinary traditions.

Additionally, the application will incorporate advanced filtering options to allow users to further refine their recipe suggestions based on dietary preferences, cooking difficulty levels, and other criteria. This customization feature ensures that users receive recipe recommendations tailored to their individual tastes, dietary restrictions, and cooking skill levels.

Once the recipe generation process is complete, the application will present the user with a curated list of recipe suggestions that match their specified criteria. Each recipe will include detailed instructions, ingredient lists, cooking times, and optional variations to accommodate different preferences and dietary restrictions.

## Low Fidelity UI Mockup 
Attached is the link to the low-fidelity UI MockUp. Included in the slides is an example of what it might look like to add meals to the meal plan, what the log in screen might look like, and how a user might search through the available recipes. 
[PlatePal MockUp](https://github.com/cs411-alawini/sp24-cs411-team075-GroupProject/blob/main/doc/PlatePal_UI_MockUP.pdf)

## Project Work Distribution 

**Database and Backend System Development**

The development of the database and backend system is a foundational task that involves setting up the infrastructure to store and process recipes, user data, grocery store locations, and other essential information. This task includes designing the database schema, integrating the [Food.com](http://food.com/) Recipes and grocery stores datasets, and developing the APIs for data retrieval and manipulation. Kathryn and Samvit will work on this part.

**Frontend Development and User Interface Design**

Frontend development focuses on creating an intuitive and engaging user interface that allows users to easily interact with the application. This includes designing the layout, implementing the ingredient input system, cuisine selection interface, and recipe suggestion display. Frank and Divya will be primarily working on the frontend development.
