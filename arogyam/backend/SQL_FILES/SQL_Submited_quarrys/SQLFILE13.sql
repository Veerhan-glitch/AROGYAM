SELECT 
    u.userid AS "User ID",  u.name AS "Customer",  o.orderid AS "Order ID",
    o.status AS "Order Status", p.name AS "Product", oi.quantity AS "Qty",
    pay.amount AS "Paid", pay.status AS "Payment Status"
FROM users u
JOIN orders o ON u.userid = o.userid
JOIN orderitems oi ON o.orderid = oi.orderid
JOIN product p ON oi.productid = p.productid
LEFT JOIN payments pay ON o.orderid = pay.orderid
ORDER BY o.orderid DESC;