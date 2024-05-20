DELIMITER $$

CREATE PROCEDURE AddIngredientToPantry(
    IN _userID INT,
    IN _pantryID INT,
    IN _ingredientName VARCHAR(20),
    IN _quantity FLOAT
)
BEGIN
    DECLARE _ingredientID INT;

    
    SELECT ingredientID INTO _ingredientID
    FROM ingredients
    WHERE ingredientName = _ingredientName;

    
    IF _ingredientID IS NULL THEN
        INSERT INTO ingredients (ingredientName)
        VALUES (_ingredientName);
        
        
        SET _ingredientID = LAST_INSERT_ID();
    END IF;

    
    IF EXISTS (SELECT 1 FROM userPantries WHERE memberID = _userID AND pantryID = _pantryID) THEN
        
        INSERT INTO pantry (pantryID, ingredientID, quantity)
        VALUES (_pantryID, _ingredientID, _quantity);
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No matching pantry found for this user.';
    END IF;
END$$

DELIMITER ;

CALL AddIngredientToPantry(1, 1, 'Flour', 2.5);
