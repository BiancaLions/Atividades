fibo = [0, 1]
while len(fibo) <10:
    fibo.append(fibo[-1] + fibo[-2])
print(fibo)