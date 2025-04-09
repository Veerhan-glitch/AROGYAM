SELECT Name AS ProductName, Brand, 
       (SELECT SUM(Quantity) 
        FROM OrderItems 
        WHERE OrderItems.ProductID = Product.ProductID) AS TotalOrdered
FROM Product
WHERE ProductID IN  (SELECT DISTINCT ProductID 
  FROM OrderItems)
ORDER BY TotalOrdered DESC
LIMIT 10;










