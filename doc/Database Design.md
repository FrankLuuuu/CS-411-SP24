# Database Design
Below we provide the Data Definition Language (DDL) commands we used to create each of these tables in the database. Here’s the syntax of the CREATE TABLE DDL command:
  CREATE TABLE table_name (column1 datatype, column2 datatype, column3 datatype,...);


```
CREATE TABLE users           (UID            INT NOT NULL AUTO_INCREMENT, 
                              username       VARCHAR(20), 
                              password_hash  VARCHAR(20), 
                              name           VARCHAR(50), 
                              allergies      VARCHAR(100),
                              PRIMARY KEY    (UID));
```

```
CREATE TABLE userPantries    (pantryID       INT NOT NULL AUTO_INCREMENT,
                              memberID       INT NOT NULL,
                              PRIMARY KEY    (pantryID),
                              FOREIGN KEY    (memberID)       REFERENCES users(UID));
```

```
CREATE TABLE pantry          (pantryID       INT NOT NULL,
                              ingredientID   INT NOT NULL,
                              quantity       FLOAT,
                              FOREIGN KEY    (pantryID)       REFERENCES userPantries,
                              FOREIGN KEY    (ingredientID)   REFERENCES ingredients(ingredientID));
                            
```

```
CREATE TABLE mealPlan        (planID         INT NOT NULL,
                              dishID         INT NOT NULL, 
                              notes          VARCHAR(255), 
                              datePlanned    DATE, 
                              timePlanned    TIME, 
                              memberID       INT NOT NULL,
                              PRIMARY KEY    (planID)
                              FOREIGN KEY    (dishID)         REFERENCES dish,
                              FOREIGN KEY    (memberID)       REFERENCES users(UID),  ON DELETE CASCADE);
```

```
CREATE TABLE dishIngredients (dishID         INT NOT NULL, 
                              ingredientsID  INT NOT NULL,
                              PRIMARY KEY    (dishID, ingredientsID)
                              FOREIGN KEY    (dishID)         REFERENCES dish(dishID),
                              FOREIGN KEY    (ingredientsID)  REFERENCES ingredients);
```

```
CREATE TABLE dish            (dishID         INT NOT NULL AUTO_INCREMENT,
                              mealName       VARCHAR(20), 
                              instructions   VARCHAR(255), 
                              description    VARCHAR(255), 
                              PRIMARY KEY    (dishID));
```

```
CREATE TABLE ingredients     (ingredientID   INT NOT NULL AUTO_INCREMENT, 
                              name           VARCHAR(20),
                              PRIMARY KEY    (ingredientID));
```
