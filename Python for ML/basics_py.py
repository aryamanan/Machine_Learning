#single line comment in Python
from math import * #importing python built-in maths library

'''
this is a multiple line comment in python
yesss
'''

#Python allows us to declare variables like this and assign any type of value to it
string = "abhsdihfslidhf"
number = -50
Boolean_Value = True
print(string, number, Boolean_Value) #command to print

#remember that in python every code executes line to line
print("  /|")
print(" / |")
print("/  |")
print("---!") #these codes will run in order in order, hence the triangle shape will hold itslef
#therefore the code placement in program matters a lot


#Working with strings in Python

#print("the "quote" doesn't work") #this command doesn't work since our string literal quote is executed as part of our command in python
#so we use \" in code which means the charachter with it not seperared by space is a part of our string literal
print("the \"quote\" does work")
#endline -- ends a string line and starts a newline using \n
print(" the line ends here \n and new line begins here")


#Modifying strings
name = "Aryan"
print(name + " is cool")
#we can do other operations as well like
print(len(name))#prints no of charachters used in string
print(name.upper()) #gives ARYAN
print(name.lower()) #GIVES aryan
print(name.isupper()) #checks if our code is uppercase or not (it isn't entirely so False)
print(name.upper().isupper()) #merging two built-in meathods upper and isupper, one makes string uppercase and other checks if it is uppercase, so result is Tautology

#using string like an array
print(name[2]) #prints 3rd charachter in string, like printing 3rd element of an array
print(name.index("y")) #locates charachter y in string at its first appearance
print(name.replace("n", "manan")) #replaces with a, returns aryamanan

#operations
print((3+1)-4*(-77)+number/99) #simple arithmatic in python
print(5//2) #gives rounded value to nearest lower integer
print(7%3) #gives remainder of division ie modulus
print(2**3) #same as 2^3
print(str(number)) #converts integer into string ie cant perform operations on it
print(abs(number)) #gives absolute value of number ie non negative
print(pow(3, 2)) #gives 3^2=9
print(max(17, 64)) #since 64>17, returns 64
print(min(3, 4)) #since 3<4, returns 3
print(round(3.9434)) #rounds to nearest integer

#for the next operations u need to import bulit-in maths library of python
print(floor(73.9234)) #rounds to lower bound integer, ie 73
print(ceil(17.0001)) #rounds to higher bound integer, ie 18
print(sqrt(36)) #gives square root


#Lists -- Same as arrays in cpp

#Declaring a list in python
Tekken = ["Kasuya", "Jin", "Hihachi", "King", "Lee", "Yoshimitsu", "Paul", "Nina"]
print(Tekken[2]) #indexes 3rd element from the begining
print(Tekken[-2]) #indexes 2nd element from back of the list
print(Tekken[1:]) #all elements from 2nd elemnt till the end of List
print(Tekken[1:6]) #elements from 2nd till 6th returned

Mario = ["Mario", "Luigi", "Peach", "Donkey Kong", "Bowser"]
Tekken.extend(Mario) #merges ario list in Tekken
print(Tekken)

Mario.append("Goomba") #adds an alement at the end of the List
print(Mario)

Mario.insert(3, "Turtle")
print(Mario)

Mario.remove("Donkey Kong") #removes the said element
print(Mario)

Mario.pop() #removes the last entry in list
print(Mario)

print(Mario.index('Peach'))
print(Mario.count("Luigi")) #no of times Luigi shows up in our list

#sorting
Tekken.sort() #all elemnts in ascending order
print(Tekken)
Tekken.reverse() #reverses the order of list
print(Tekken)

#copying a List
#Tekken2 = Tekken.copy() #all attributes of Tekken list copied to Tekken2

#Tuples -- used to store permanent data
coordinates = (1, 3) #a tuple cant be mutated, ie can't change its value and their positionings, it's static
print(coordinates[1])
#coordinates[1]=18 #gives error cant change value of a tuple,
#'tuple' object does not support item assignment

more = [(1,2), (23,24), (23,54), (4,87)] #list of tuples

def Hello(name, age): #function in python
    print("Hello user, "+name+", you are "+age+" years old")

print('top')
Hello("Aryan", "20") #as we can see functions aren't executed linearly in python, only execute when they're called
print('bottom')

#Return Statements
#Usually I want some info or value to be retuned by function, we do that using retuen statements

def cube(n):
    return n*n*n #return breaks a function, once u execute it compiler stops reading code written ahead


result = cube(3);
print(result)


#Conditionals - If and Else

is_male=True
is_tall=True
if is_male or is_tall:
    print('you are a male or you are tall')
elif is_male and not(is_tall):
    print('you are a male and not tall')
elif is_tall and not(is_male):
    print('you are a female but tall')
else:
    print('you are a female and not tall')

#comparisons in conditionals
def max_num(n1, n2, n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    elif n1 == n2 or n1== n3 or n2==n3:
        return null;
    else:
        return n3
print(max_num(300,45,23))

#Dictionaries -- specipy an entry and a key to it
#IMPORTANT -- every one of the keys in a dictionary should be unique, can't be the Same

monthConversions = {
   "jan": "january",
   "feb": "feburary",
   "mar": "march",
}
print(monthConversions["mar"])

#Loops
i=1
while i<=10: #while loop executes till condition along it is true
    print(i)
    i += 1

for letter in "girrafe":
     #For loop, the word after "for" is an ID of the loop,"in" basically defines a range for the loop,
     #here for every charachter in string "girrafe" our code Loops
     print(letter)

for name32323 in Tekken:
    print(name)
for bhb3eh3eb2h3 in range (10):
    print(bhb3eh3eb2h3)
for daexxw23sdadas in range(12,23):
    print(daexxw23sdadas)

#2D Lists
number_grid = [[1,2,3], [1,4,23], [12,34,12], [9,2]]
print(number_grid[0][0]) #returns 1

#Nested Loops
for row in number_grid:
    for col in row:
        print(col) #Nested loop to print all elements of 2D array

#Building a vowel checker
phrase ="dog"
def vow(phrase):
    for letter in phrase:
        if letter.lower() in 'aeiou':
            print('yes')
        else:
            print('no')
    return vow


#Try Except Block
#  try:
#     number=int(input('Enter a number: '))
#     print(number)
# except: #except insures if program is broken by some errors in external input, it still gives out our desired results
#     print("Invalid error")






#Taking Input
age = input("Enter your age")
print('so your age is ' + age)

#but the problem is that whatever imput you give to python, it treats it as string, even numbers
#so we can define them as datatypes like float, int etc

age2 = input(int("Enter Your Age: "))
print('so your age 5 years later will be: ', age2+5)
