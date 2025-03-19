#While Loop
count = 0
while (count < 10):
  count = count + 1 
  print("Hello Geek")

#For loop
#Iteration over a list
print("List Iteration")
list = ["Mama", "Baba", "Api","Me"] 
for i in list:
  print(i)

#Iteration over a tuple
print("\nTuple Iteration")
tuple = ("Dua", "Nida", "Umaira") 
for i in tuple:
  print(i)

#Iteration over a string
print("\nString Iteration") 
str = "Hello"
for i in str:
  print(i)

#Iterating by index of sequences
list1 = ["Nida", "Umaira", "Dua"] 
for index in range(len(list1)):
  print(list1[index])

# Prints all letters except 'e' and 's'
for letter in 'bscssemster6':
  if letter == 'e' or letter == 's': continue
  print ('Current Letter :', letter) 
  
# break the loop as soon it sees 'e' or 's'
for letter in 'hello':
  if letter == 'e' or letter == 's': break
  print ('Current Letter :', letter)

#Functions
#Creating a functiom
def my_function(): 
  print("Hello from a function")
my_function()

#Parameters
def my_function(name):
 print(name + " are crazy")
my_function("Kids")
my_function("Adults")

#Default Parameter Value
def my_function(country ="Pakistan"): print("I am from " + country)
my_function()
my_function("India")
my_function("Brazil")

#List as parameter
def my_function(food):
 for x in food: print(x)
fruits = ["apple", "banana", "cherry"] 
my_function(fruits)

#Return values
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#class
class MyClass: x = 5

#object
p1 = MyClass() 
print(p1.x)

#The __init__() funtion
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
   print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1)
p1.myfunc()