SELECT DISTINCT u.userid, u.name
FROM users u
WHERE u.userid IN (
    SELECT o.userid
    FROM orders o, orderitems oi, product p
    WHERE o.orderid = oi.orderid AND oi.productid = p.productid
    AND p.prescriptionneeded = true); 