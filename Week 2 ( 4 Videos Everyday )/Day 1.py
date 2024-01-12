
# fStrings

letter="Hey my name is {1} and I live in {0}";
country="India";
name="Aryan"
print(letter.format(country,name));
print(f"Hey my name is {name} and I live in {country}");

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
print(f"{2 * 30}")


# DocStrings

def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__)

# Recursion
def factorial(n):
  if(n==0 or n==1):
    return 1;
  else:
    return n*factorial(n-1);
print(factorial(7))

# Sets

s={2,2,4,5,7,4,2}
print(s) 