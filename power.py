squares = 5
result = list(map(lambda X: 2 ** X, range(terms)))
for i in range(squares):
 print("2 raised to the power of",i,"is",result[i])
