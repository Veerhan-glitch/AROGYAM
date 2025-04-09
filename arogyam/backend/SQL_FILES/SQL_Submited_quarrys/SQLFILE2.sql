SELECT Name,Address,Age,Email,PhoneNumber 
FROM Users 
WHERE UserID IN (
    SELECT DISTINCT UserID 
    FROM Orders 
) AND UserID IN (
    SELECT DISTINCT UserID 
    FROM Feedback
);