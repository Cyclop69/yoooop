def prime(a):
  for as i range(2,a+1):
  for i in range(2,a):
    b=a%i
    if b==0:
      c="the number is not prime"
    else:
      c="the number is prime"
    return c
nu=int(input("enter the number:\n"))
print(prime(nu))
  
