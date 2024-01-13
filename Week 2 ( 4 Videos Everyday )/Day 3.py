# Exception Handling
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")

# Finally Keyword
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")

# Custom Error
a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")
 

x = func1()
print(x)

# Short Hand if-else
a = 330000
b = 3303
print("A") if a > b else print("=") if a == b else print("B")

c = 9 if a>b else 0
print(c)