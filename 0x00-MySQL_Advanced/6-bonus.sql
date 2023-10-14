-- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

-- creates a stored procedure\ AddBonus that adds a new correction for a student.
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;
    
    -- Check if the project exists, and if not, insert it
    IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    
    -- Get the project ID
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    
    -- Insert the correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END;
//
DELIMITER ;
