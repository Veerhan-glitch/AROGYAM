SELECT p.ProductID,p.Name,SUM(p.Price * oi.Quantity) AS TotalRevenue
FROM Product p
JOIN OrderItems oi ON p.ProductID = oi.ProductID
JOIN Orders o ON oi.OrderID = o.OrderID
WHERE o.UserID IN (
       SELECT UserID 
       FROM Prescription
	   )
GROUP BY p.ProductID, p.Name
ORDER BY TotalRevenue DESC
LIMIT 5;