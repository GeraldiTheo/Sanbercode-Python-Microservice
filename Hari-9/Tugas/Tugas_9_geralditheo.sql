SELECT 
	orders.orderNumber, 
    orders.orderDate, 
    customers.customerName, 
    customers.city, 
    customers.country, 
    orderdetails.quantityOrdered, 
    products.productName
FROM orders
INNER JOIN customers
ON orders.customerNumber = customers.customerNumber
INNER JOIN orderdetails
ON orders.orderNumber = orderdetails.orderNumber
INNER JOIN products
ON orderdetails.productCode = products.productCode

WHERE 
	productName = "1992 Ferrari 360 Spider red"
    AND
    
    orderDate >= 20040801
    AND
    orderDate <= 20041201
    
