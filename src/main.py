#checking if a number is prime
def prime(a):
  for i in range(2,a):
    if a%i==0:
      return False
  return True

#finding out the prime numbers up to a highest number
def within_prime(h):
  list=[]
  for t in range(2,h+1):
    if prime(t) is True:
      list.append(t)
  return list
#finding prime factors
def no(m):
  hi=[]
  hu=within_prime(m)
  for h in hu:
    if m%h==0:
      hi.append(h)
  return hi

y=int(input("the num:\n")) 
s=no(y)
print("the prime factors of "+str(y)+" are:\n")
for t in s:
  print(t)

  
  

    
  

    
      
    
    
  
