SELECT Name, Email
FROM Users 
WHERE UserID IN (
    SELECT UserID 
    FROM Orders 
    WHERE OrderID IN (
        SELECT OrderID 
        FROM Payments 
        GROUP BY OrderID 
        HAVING SUM(Amount) > 500
    )
);