-- SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

-- creates a trigger that resets the attribute valid_email only when the email has been changed.
DELIMITER //
CREATE TRIGGER validate_email
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
    IF NEW.email IS NOT NULL AND NEW.email REGEXP '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}$' THEN
       SET NEW.valid_email = 1;
    ELSE
       SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;
