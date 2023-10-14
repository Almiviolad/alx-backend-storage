-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.

-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN uid INT)
BEGIN
    DECLARE av_score DECIMAL(10, 2);  -- Declare a variable to store the average score
    
    -- Calculate the average score for the specified user
    SELECT AVG(score) INTO av_score FROM corrections WHERE user_id = uid;
    
    -- Update the user's average score in the 'users' table
    UPDATE users
    SET average_score = av_score
    WHERE id = uid;    
END;
//
DELIMITER ;
