-- As a group, develop at least 4 advanced SQL queries for your application. These queries should be relevant to the functionality of your application and are expected to be part of your final application. The queries should each involve at least two of the following SQL concepts:
--   Join multiple relations
--   SET Operators
--   Aggregation via GROUP BY
--   Subqueries that cannot be easily replaced by a join. 

-- grab the specific users pantry
select ingredientName, quantity
from pantry natural join ingredients
where memberID == {currentuser}      -- see how to reference
group by memberID asc                    -- confirm alphabetical


-- ific users pantry
select count(ingredientID), dishID
from pantry join userpantries join mealplan join dishIngredients
where pantry.pantryID = userpantries.pantryID and userpantries.memberID = mealplan.memberID and mealplan.dishID = dishIngredients.dishID and ingredientID = ingredientsID      -- see how to reference
group by dishID asc      -- confirm alpha

select dishID, mealName
from dish natural join dishIngredients 
where ingredientsID not in (select ingredientID
                              from users join ingredients
                              where users.allergies = ingredients.name, users.userID = {currentuser}) as allergens             -- and allergies = ingredientName) as allergens
      
group by dishID


select dishID, mealName
from dish d1 natural join dishIngredients 
where not exists 
  ( select 1
    from users join ingredients on allergies = ingredientName join dishIngredients di on ingredientsID = ingredientID
    where di.dishID = d1.dishID and users.UID = 1)
group by dishID, mealName
limit 15;


      
-- select ingredientName, quantity
-- from pantry natural join ingredients
-- where memberID == {currentuser}      -- see how to reference
-- group by memberID asc     
-- select allergies
-- from users
-- where memberID = {currentuserID}
      


-- grab the meal plan of the specific user
select mealName, datePlanned, timePlanned, description
from mealPlan natural join dish
where memberID == {currentuser}
group by memberID asc 
order by datePlanned, timePlanned


-- -- create a "grocery list" for the user given the meal plan
-- select name, (amountrequired - quantity) as amountneeded
-- from (select ingredientID, SUM(quantity) as amountrequired
--       from ingredients natural join dishIngredients join (select dishID
--                                                           from mealPlan 
--                                                           where memberID == {currentuser}
--                                                           order by datePlanned, timePlanned) as dish  
--                                                           on dishID
--       group by ingredientID
--       ) as ingredientsneeded,  
--       (select name, quantity
--         from pantry natural join ingredients
--         where memberID == {currentuser}      -- see how to reference
--         order by name asc)                    -- confirm alphabetical
--       ) as ingredientshave
-- -- where
-- having amountrequired - quantity > 0
-- order by name            BOOO FRANK AND SAMVIT MAKE ME WORK HARD

-- create a "grocery list" for the user given the meal plan
select name
from (select ingredientID
      from dishIngredients join (select dishID                              -- should this be right join? we want all the ingredients that have a dish id in meal plan
                                  from mealPlan 
                                  where memberID == {currentuser}
                                  order by datePlanned, timePlanned) as dish  
                                  on dishID
      ) as ingredientsneeded,  ingredients
where ingredientsneeded.ingredientID == ingredients.ingredientID
limit 15


      

-- select ingredientID, SUM(quantity) as amountrequired
-- from ingredients natural join dishIngredients join (select dishID
--                                                     from mealPlan 
--                                                     where memberID == {currentuser}
--                                                     order by datePlanned, timePlanned) on dishID



-- suggest meals given the users pantry --limit 15
 -- dishID         INT NOT NULL AUTO_INCREMENT,
 --                              mealName       VARCHAR(20), 
 --                              cuisine        VARCHAR(20), 
 --                              time2Cook      INT, 
 --                              instructions   VARCHAR(255), 
 --                              description    VARCHAR(255), 
 --                              rating         FLOAT, 
 --                              image          LONGBLOB,
 --                              PRIMARY KEY    (dishID));

-- select mealName
-- from dish, (select ingredientID, SUM(quantity) as amountrequired
--             from ingredients natural join dishIngredients join (select dishID
--                                                                 from mealPlan 
--                                                                 where memberID == {currentuser}
--                                                                 order by datePlanned, timePlanned) as dish  
--                                                                 on dishID
--             group by ingredientID
--             ) as ingredientsneeded,  
--             (select name, quantity
--               from pantry natural join ingredients
--               where memberID == {currentuser}      -- see how to reference
--               order by name asc)                    -- confirm alphabetical
--             ) as ingredientshave
-- where cuisine == {cuisine} and time2Cook <= {time} and rating >= {rating} 
-- having avg(quantity/amountrequired) >= {threshhold}
-- limit 25

select mealName
from dish, (select count(ingredientID)
            from pantryingredients natural join dishIngredients join (select dishID
                                                                from mealPlan 
                                                                where memberID == {currentuser}
                                                                order by datePlanned, timePlanned) as dish  
                                                                on dishID
            group by ingredientID
            ) as ingredientsneeded,  
            (select name
              from pantry natural join ingredients
              where memberID == {currentuser}      -- see how to reference
              order by name asc)                    -- confirm alphabetical
            ) as ingredientshave
where cuisine == {cuisine} and time2Cook <= {time} and rating >= {rating} 
having avg(quantity/amountrequired) >= {threshhold}
limit 25



      
SELECT u.UID, u.username, p.memberID, i.name AS pantry_ingredient, di.ingredientsID, di.quantity AS ingredient_quantity, di.rating
FROM users u
INNER JOIN pantry p ON u.UID = p.memberID
INNER JOIN ingredients i ON p.ingredientID = i.ingredientID
INNER JOIN dishIngredients di ON i.ingredientID = di.ingredientsID
GROUP BY cuisine
ORDER BY di.rating ASC ;

SELECT u.UID, u.username, mp.planID, m.mealName, m.cuisine, m.instructions, m.description
FROM users u
INNER JOIN mealPlan mp ON u.UID = mp.memberID
INNER JOIN meals m ON mp.dishID = m.dishID;

SELECT u.UID, u.username, mp.planID, m.mealName, m.cuisine, m.instructions, m.description
FROM users u
INNER JOIN mealPlan mp ON u.UID = mp.memberID
INNER JOIN meals m ON mp.dishID = m.dishID
WHERE u.UID = 1

SELECT i.name AS ingredient_name, SUM(p.quantity) AS total_quantity
FROM pantry p
INNER JOIN ingredients i ON p.ingredientID = i.ingredientID
WHERE p.memberID = <userID>
GROUP BY i.name;

SELECT u.UID, u.username, u.allergies
FROM users u
WHERE NOT EXISTS (
    SELECT u.allergies
    FROM users u
    LEFT JOIN pantry p ON u.UID = p.memberID
    WHERE p.memberID = u.UID
);

SELECT name, mealName 
  FROM users JOIN ingredients ON users.allergies = ingredients.ingredientName 
  JOIN dishIngredients ON ingredients.ingredientID = dishIngredients.ingredientsID 
  JOIN dish ON dishIngredients.dishID = dish.dishID 
  GROUP BY name, mealname 
  order by name 
  LIMIT 15;

