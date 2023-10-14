-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

-- creates trigger that decrease quantity of items after a new order is added
DELIMITER //
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE NEW.item_name = name;
END;
//
DELIMITER ;
