-- SQL script thatf creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

-- function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS DECIMAL(35, 33)
DETERMINISTIC
NO SQL
BEGIN
    IF(b = 0) THEN
       RETURN 0;
    ELSE
       RETURN a / b;
    END IF;
END; //
DELIMITER ;
