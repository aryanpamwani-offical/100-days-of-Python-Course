for i in range(12):
  if(i == 10):
   break
  else:
   print("5 X", i, "=", 5 * i)
  
print("");
for k in range(12):
  if(k == 10):
    print("Skip the iteration using continue")
    continue
  print("5 X", k, "=", 5 * k)
  
def calculateGmean(a,b):
  mean=(a*b)/(a+b)
  print("Calculating gmean of first value:",a,"and second value:",b,"=",mean);

def isGreater(a,b):
  if(a>b):
    print("A is greater than B");
  else:
    print("B is greater than A");

def isLesser(a,b):
  pass
a=5;
b=16;
calculateGmean(a,b);
isGreater(a,b);

def Avg(*numbers):
  sum=0;
  for i in numbers:
    sum=sum+i;
  print("Average is:",sum/len(numbers));

Avg(a,6,9,8,24);