SELECT u.UserID,u.Name,
  COALESCE(SUM(o_total.total_value),0) AS TotalSpent,
  COUNT(DISTINCT o.OrderID) AS OrderCount
FROM Users u
LEFT JOIN Orders o ON u.UserID = o.UserID
LEFT JOIN (
   SELECT o.OrderID,SUM(p.Price * oi.Quantity) AS total_value
   FROM Orders o
   JOIN OrderItems oi ON o.OrderID = oi.OrderID
   JOIN Product p ON oi.ProductID = p.ProductID
   GROUP BY o.OrderID
) AS
o_total ON o.OrderID = o_total.OrderID
WHERE u.UserID IN (SELECT DISTINCT UserID FROM UserOffers)
GROUP BY u.UserID, u.Name;
