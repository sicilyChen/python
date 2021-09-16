item=['Fruit','Book','Others']
prices=[98,89,56]
d={item.upper():price for item,price in zip(item,prices)}
print(d)