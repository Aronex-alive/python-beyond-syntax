#  python-beyond-syntax

##  #DAY_1 
Today I learned about the history of python. It was created in 1991 by Guido van rossum
along with that I learned about repl which stands for read evaluate print loop. 
After read a simple definition of programming.<br>
THAT IS ALL FOR TODAY <br>

##  #DAY_2 <br>
Today i learned about the different ways in which python can be used for suppose machine learning AI and 
many more.I have also seen a simple program of Javis ,which can perform certain prebuild tasks like
opening youtube, google etc.YOu can check the program as it is attacted in this repo as #DAY_2.py .<br>
Let's meet tomorrow. <br>

##  #DAY_3 <br>
It was a nice day and i learned about modules in python which are basically pre-written code which anyone 
can fetch and use according to his/her use. <br>It is of two types:-<br> 1. Build-in module <br>2. External module<br> python contains some preinstalled modules whic travel with or which are installed with the install of
python on the other hand there are external module which the user has to download from internet before it.
<br>
**Code for installing an external module:**  
```
pip install <module-name>
```
for example :- pip install pandas, pip install sklearn<br>
See you tomorrow<br>

##  #DAY_4 <br>
Today I made my first python programe .which wasn't much but a simple programe that prints some instructions. I used print() function in python:-
``` print("Hello world")
print("I am Aronex"," \n nice to meet you")
```
This is up for today tomorrow I will study escape sequences.<br>

##  #DAY_5 <br>
Hola! world. Today i learned about escape sequence characters in python. It refers to those characters which help us to tell the python that we want a new line or '' or "" to be displayed to the user.
```
print("Hello Word \n my name is Aronex")  # here the \n is a escape sequence character
print("he said that,\"I am ill\"") 
```
I also learned about some more functions used within print function that are :-
1.sep<br>
2.end<br>
3.file<br>
The **sep** is used to define that what should be printed between the Statement present within the the print function and **end** is used to specify what should be printed at the end of the print function.
```
print("Have a good day","my friend",sep="-",end="@")
```
Have a great day ahead.<br>

##  #DAY_6  <br>
Hola World! today i learned abuot data types in python and variables. **variables** are basically containers inpython which can store different data types. Ther are two types of data types that is :-<br>
1.**Mutable datatype**<br>
2.**Imutable datatype**<br>
Those datatypes which can be changed are called mutable data types whereas those datatypes which can not be changed are know as imutable datatypes. The mutable data type includes **list ,dictionary and sets** and imutable datatype includes **string , tuple** etc. Following are the few data types in python :-<br>
 **1. String datatype** :- anything enclosed within single or double quotes is a string.
 ```
 a="Hello World"
 print(a)   # here a is a variable which stores the value in it
 print(type(a))  # this type() function is used to find the type of a data entered in python
 ```
**2. Numeric datatype** :- this includes numeric values
```
b=142  
print(type(b))  # here the type will be integer so <class= 'int'> wil be printed
c=123.5
print(type(c))   # here float will be printed
d=complex(4,2)
print(type(d))  # here complex will be printed
```
**3. Sequencial datatype** :- it incles lists,tupleand sets
```
list=[1,2,3,[apple,orange]] 
tuple1=(12,3,34,76) 
dict={ "Name":"Aronex","Class":11}
set={12,54,78,4,5}
```
**4. Boolean datatype** :- it gives otput only in True or False
<br>
so these were the different data types in python. **You can check the DAY_6** program file for more codes( it is present in the save repo).<br>
let's meet tomorrow have a great day.<br>
##  #DAY_7  <br> 
Welcome back friends today i learned about operators in python which are following :-
```
+ #addition
- #subtraction
* #multiplication
/ #division
// #floor division 
% #remainder modulus
** #exponential
```
 and make that you check **My first Python exercise or program #DAY_7.py** for creating a calculator.<br>
 Thah's all for today. Adios Amigos<br>

 ##  #DAY_8   <br>
 Today i have not learned much because today was the solution day of the previous day's exercise but still ther are few **VS Code** stortcuts which i want to tell you guys :-
```
ctrl + / # for making the selected lines a comment
alt + shift + downarrow # for replicating the line 
```
Let's hope for a better tomorrow.Adios<br>

##  #DAY_9   <br>
 Welcome again guys, Today I learned what is typecasting in python. It is the procees of changing the type of different data types using function like **int(), hex(), oct(), float() etc.** and type casting is of two types that are :-<br>
 1.Explicit Type casting<br>
 2.Inplicit Type casting<br>
 Explicit type casting is done by the coder or programer which involes use of functions like :-<br>
 **a=34<br>
 print(str(a)+"Hello")**<br>
 And in Implicit type casting the python interpretor Automatically converts the type of a data ex.<br>
 **a=12<br>
 b=1.8<br>
 print(a+b) # here python first converts a into float type after that it adds it**<br>
Following some sample code:-
 ```
 a=31
 b=52
 print(a+b)
 print(str(a)+str(b))  #Here output will be 3152 because a and b is treated as string
 ```
 I also learned about the **type() function**, which tells us the type of data entered.<br>
**Make sure that you Check DAY_9 program for it.**<br>
 Have a great day<br>

##  #DAY_10   <br>
 Hola! Today i learned how to take input from the user which is done by usiny the **input() function** in python. the input function by default takes the value in string and in order to change it's data type we have to do type casting.Further more we have to assign the input() function or store the input in a variable.
 ``` 
 a=input("Enter your name : ")
 print(a)
 b=input("enter a no. : ")
 c=input("enter a no. : ")
 print(b+c)  #here b and c are treated as string
 print(type(b))
 ```
 That is all for today.<br>

 ##  #DAY_11   <br>
 Hello World today i learned about **strings** which is one of the data types present in python. Anything within a single or double quote is treated as a string and the string's indexing starts from 0. Further more if you want to print multiline string you can use triple quotes.I also studied about how to use for loop to print different characters of the string.
 ```
 a="Milkyway"
 print(a[0])  # here only M will be printed
 print(a[1:5])
 b='''I am a student whose dreams
 are out of world.
 but the thing is i am currently working as hard as i should or ass i could'''
print(b)

for i in b:
  print(i)  # this will print every character of vari.b in different lines
```
Make sure that you check **#DAY_11** program. this is all for today see you next time.<br>

##  #DAY_12   <br>
Hola! today i learned how to slice a string in python and furthermore I learned about the **len()** function in python. the slicing is of two types that is positive and negative slicings. Following are few examples :-
```
a="Aronex"
print(a[0:6]) # here whole word will be printed
print(a[-4:-1]) 
print(a[len(a)-4:len(a)-1]) # this and above are same 
```
From <u> _**left to right or positive**_</u> index starts from <u>_**0 to ...**_</u> and from <u>_**right to left or negative**_ </u>index starts from  <u>_ **-1 to ...**_</u>:--       For negative slicing the python interpreter subtracts the given negative indicies from the length of string. We can iterate the characters of the string also by using for loop. 
```
s="adjoining program"
for i in s:
  print(i)
```
Check **#DAY_12 program** for more examples. Thanks <br>

##  #DAY_13   <br>
Hola amigos. Today i leared about the different commands or functions of string data type. As string are immutable type of data that's why they can not be change. So the functions of string are generally applied on a copy of the string. There are the functions available for the string data type:- <br>
1. **upper()**:- this converts the string into uppercase.<br>
syntax- a.upper() <br>
2. **lower()**:- this converts the string into lowercase<br>
syntax- a.lower()<br>
3. **strip()**:- this removes the white spaces from the starting and from the ending of a string.<br>
syntax- a.strip()<br>
4. **rstrip()**:- this removes any trailing character<br>
syntax- a.rstrip()<br>
5. **replace()** :-
The replace() method replaces all occurences of a string with another string. Example:<br>
str2 = "Silver Spoon"<br>
print(str2.replace("Sp", "M"))<br>
6. **split()** :
The split() method splits the given string at the specified instance and returns the separated strings as list items.
Example:<br>
str2 = "Silver Spoon"<br>
print(str2.split(" "))      #Splits the string at the whitespace " ".<br>
7. **capitalize()** : Converts the first character of the string to uppercase and the rest to lowercase.<br>

8. **center()** : Centers the string within a specified width. You can use a custom fill character.<br>
Example:<br>
"Hello".center(10, "*") # Output: '**Hello***'<br>

9. **count(**) : Returns the number of times a substring appears in the string.<br>

10. **endswith()** : Checks if the string ends with a specified value. Returns True or False.<br>

11. **find()** : Returns the index of the first occurrence of a substring, or -1 if not found.<br>

12. **index()** : Similar to find(), but raises an error if the substring is not found.<br>

13. **isalnum()** : Returns True if all characters are alphanumeric (A–Z, a–z, 0–9).<br>

14. **isalpha()** : Returns True if all characters are alphabetic (A–Z, a–z).<br>

15. **islower()** : Returns True if all characters in the string are lowercase.<br>

16. **isprintable()** : Returns True if all characters in the string are printable (no control characters).<br>

17. **isspace()** : Returns True if the string contains only whitespace characters (spaces, tabs, etc.).<br>

18. **istitle()** : Returns True if each word in the string starts with an uppercase letter.<br>
Example:<br>
"World Health Organization".istitle() # True<br>

19. **isupper()** : Returns True if all characters in the string are uppercase.<br>

20. **startswith()** : Checks if the string starts with a specified value. Returns True or False.<br>

21. **swapcase()** : Converts uppercase letters to lowercase and vice versa.<br>
Example:<br>
"Python".swapcase() # 'pYTHON'<br>

22. **title()** : Capitalizes the first letter of every word in the string.<br>
<br>
That is all for today see you tommorow.

##  #DAY_14   <br>
welcome back guys today i learned about the the conditional statements in python i.e, the use of if, elif and else.
There keywords are used in python so that the interpreter can find or solve a conditional statement. for example:-<br>
```
a=int(input("enter a number :"))
if a<0:
  print(a,'is a negative number')
elif a==0:
  print(a,'is equal to 0')
elif a>0:
  print(a,'is a positive number')
else:
  print("Enter a valid input")
```
This is the way or syntax of using conditional stataments in python. I hope i will see you next time.<br>

##  #DAY_15   <br>
Today i got an exercise to make a program using time module which checkes the time and then reply good morning or evening or night according to the time. For this see the #DAY_15 program.<br>
ok then have a good day.

