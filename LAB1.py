#Programming Syntax
print ("Hello World!")

#Comments in python
x=1
#The initial value of x is 1
if x>0:
 print ("These two are comments") #Print a string

#Iput/Output
txt = input("Type something to test this out: ") 
print(txt)

#Multiple statements on a single line
print ("Statement1")
print ("Statement2")
#We can write above two statements in the following way
print ("Statement1") ;print ("Statement2")

#Indentation
x=1
if x>0:
print("This statement has a no Indentation")
print("This statement has a no space Indentation")

x=1
if x>0:
 print("This statement has a single space Indentation")
 print("This statement has a single space Indentation")

x=1
if x>0:
    print("This statement has a single tab Indentation")
    print("This statement has a single tab Indentation")

x=1
if x>0:
    print("This statement has a single space+tab Indentation")
    print("This statement has a single space+tab Indentation")

#Special characters in strings
print("This is a backslash (\\) mark.")
print("This is tab \t key.")
print("These are \'single qoutes\'")
print("These are \"double qoutes\"")
print("This is a new line\nNew Line.")

#String indices and accessing string elements
string1="Python Tutorial"
print(string1[0])  #print 1st character
print(string1[-15])  #print 1st character
print(string1[14])  #print last character
print(string1[-1])  #print last character
print(string1[4])  #print 4th character
print(string1[-11])  #print 4th character

#Lists
my_list1=[5,12,13,14]
print(my_list1)
my_list2=['red','blue','black','white']
print(my_list2)
my_list3=['red',12,112.12]
print(my_list3)

#List indices
color_list=["RED","BLUE","GREEN","BLACK"]
print(color_list[0]) 
print(color_list[0],color_list[3]) 
print(color_list[-1]) 

#List Slice
print(color_list[0:2])
print(color_list[1:2]) 
print(color_list[1:-2])  
print(color_list[:3]) 
print(color_list[:]) 