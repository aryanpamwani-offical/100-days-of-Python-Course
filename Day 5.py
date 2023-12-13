
# String Methods

a="!!!!Apple!!! !!!!!";
print(a.upper());
print(a.lower());
print(a.rstrip('!'));
print(a.replace("Apple","Harry"));
print(a.capitalize());
print(a.count('a'));
print(a.center(50));
print(len(a));
print(len(a.center(50)));
print(a.count('a'));
print(a.endswith("!!!"));
print(a.endswith("!!!",7,12));
print(a.find("n"));
# print(a.index("dfdk"));
str1 = "WelcomeToTheConsole";
print(str1.isalnum());
str1 = "Welcome"
print(str1.isalpha());
str1 = "hello world";
print(str1.islower());
str1 = "We wish you a Merry Christmas";
print(str1.isprintable());
str1 = "        " ;      #using Spacebar
print(str1.isspace());
str2 = "        ";       #using Tab
print(str2.isspace());
str1 = "World Health Organization"; 
print(str1.istitle());
str1 = "WORLD HEALTH ORGANIZATION"; 
print(str1.isupper());
str1 = "Python is a Interpreted Language"; 
print(str1.startswith("Python"));
str1 = "Python is a Interpreted Language"; 
print(str1.swapcase());
str1 = "He's name is Dan. Dan is an honest man.";
print(str1.title());

# if-else

age=int(input("Enter your age: "));
print("Your age: ",age);

#Conditional Operators:>,<,<=,>=,==,!=
if(age>18):
    print("You are eligible.");
else:
    print("Sorry ");

num = 0
if (num < 0):
    print("Number is negative.");
elif (num == 0): # elif = else if(num==0) 
    print("Number is Zero.");
else:
    print("Number is positive.");


import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hours = int(time.strftime('%H'));
if(hours>=4 & hours<10):
    print("Good Morning");

elif(hours>=12 & hours<20):
    print("Good AfterNoon");
elif(hours>=22 & hours<24):
    print("Good Night");