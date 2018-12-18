if num > 1:
    for i in range(2,num):
        if(num % i) == 0:
          print(num,"is not a prime number")
          print(i,"time,"num//i,"is",num)
          break
        else:
            ptint(num,"is a prime number")
else:
    print(num,"is not a prime number")
