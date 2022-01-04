#866245048942316
# self and __init__ / constructor
#
# List comprehension
l =	[x for x in range(1,11)]
s =	[x*x for x in range(1,11)]
v =	[x**3 for x in s]
m =	[x for x in range(1,11) if x%2==0]
print(l)
print(s)
print(v)
print(m)


num1=[10,20,30,40]
num2=[30,40,50,60]
num3=[i for i in num1 if i not in num2]
num4=[i for i in num1 if i in num2]
print(num3) 
print(num4) 

words="the quick brown fox jumps over the lazy dog".split()
print(words)
l=[[w.upper(),len(w)] for w in words]
print(l)

vowels=['a','e','i','o','u']
word=input('Enter a word:')
result=[]
[result.append(i) for i in word if i in vowels if i not in result]
print (result)

#DICT

n=int(input("Enter number of students:"))
d={}
for i in n:
    name =input("Enter name of the student:")
    marks= int(input("Enter marks of", name, ":"))
    d[name]=marks
print ("Name and Marks have been stored.")
print ("*" * 20)
print ("Name", '/t/t' ,"Marks" )
print ("*" * 20)
for k,v in d.items:
    print(k, '/t/t',v)


#Types of VARIABLES
class Student:
    collegeName='IGNOU' # static variable
    def __init__(self, name, rollno):
        self.name=name#instance variable
        self.rollno=rollno#instance variable
    def m1 (self):
        x=10 # local variable
        for i in range (x): #i & x is local variable
            print(i)

#Types of VARIABLES
    #Static Variale
class Test:
    a=10
    def __init__(self):
        Test.b=20
    def m1 (self):
        Test.c=30
t=Test()
t.m1()
print(Test.__dict__)
#Types of VARIABLES
#Static Variale
class Test:
    a=10 #static variable
    def __init__(self):
        self.b=20 #instance variable
        Test.c=30 #static variable
    def m1 (self):
        self.d=40#instance variable
    def m2 (self):
        Test.e=50#static variable
    def m3 (self):
        x=49 #local variable
        Test.f=x+1#static variable
t1=Test()
t1.m1()
t1.m2()
t1.m3()
print(Test.__dict__)
print(t1.__dict__)
print(t1.a)
print(t1.b)
print(t1.c)
print(t1.d)
print(t1.e)
print(t1.f)
#############################################
#local variable******************************
class Student:
        def m1 (self):
            x=10 # local variable
            for i in range (x): #i & x is local variable
                print(i)
s=Student()
s.m1()
#*******************************************************
#Example of Instance Method
class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Hi", self.name)
        print("Your marks are:", self.marks)
    def grade(self):
        if self.marks>=60:
            print("Hey you got First Grade")
        elif self.marks>=50:
            print("Hey you got Second Grade")
        elif self.marks>=40:
            print("Hey you got Third Grade")
        elif self.marks>=33:
            print("Hey you got Passing Grade")
        elif self.marks<=33:
            print("Hey you are Failed")
n=int(input("Enter number of students:"))
for i in range (n):
    name=input("Enter Name:")
    marks=int(input("Enter Marks:"))
    s=Student(name,marks)
    s.display()
    s.grade()
    print('*'*20)
#*********same example with while loop*************************
n=int(input("Enter number of students:"))
count=1
while count <=n:
    name=input("Enter Name:")
    marks=int(input("Enter Marks:"))
    s=Student(name,marks)
    s.display()
    s.grade()
    print('*'*20)
    count= count+1
_________________________________________________________________
#Best Example of Instance Method is Setter and Getter
class Student:
    def setName(self, name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self, marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
    def grade(self):
        if self.marks>=60:
            print("Hey you got First Grade")
        elif self.marks>=50:
            print("Hey you got Second Grade")
        elif self.marks>=40:
            print("Hey you got Third Grade")
        elif self.marks>=33:
            print("Hey you got Passing Grade")
        elif self.marks<=33:
            print("Hey you are Failed")
n=int(input("Enter number of students:"))
for i in range(n):
    name=input("Enter Name:")
    marks=int(input("Enter Marks:"))
    s=Student()
    s.setName(name)
    s.setMarks(marks)
    print ("hi",s.getName())
    print ("Your marks are:", s.getMarks())
    s.grade()
    print('*'*20)


class Student:
        def m1 (self):
            x=10 # local variable
            for i in range (x): #i & x is local variable
                print(i)
s=Student()
s.m1()

import gc
print (gc.isenabled())
gc.disable()
print (gc.isenabled())
gc.enable()
print (gc.isenabled())

______________________________________________________

-------------------------------------------------------------------------------------
Operator	        Description	                                                            Example
+ Addition	        Adds values on either side of the operator.	                            a + b = 30
- Subtraction	    Subtracts right hand operand from left hand operand.	                a – b = -10
* Multiplication	Multiplies values on either side of the operator	                    a * b = 200
/ Division	        Divides left hand operand by right hand operand	                        b / a = 2
% Modulus	        Divides left hand operand by right hand operand and returns remainder	b % a = 0
** Exponent	        Performs exponential (power) calculation on operators	                a**b =10 to the power 20
//	Floor Division  The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) −	
                                                                                            9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
----------------------------------------------------------------------------------------
# super () Method
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display (self):
        print ('Name:', self.name)
        print ('Age:', self.age)
class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks
    def display(self):
        super().display()
        print('RollNo:', self.rollno)
        print ('Marks:', self.marks)
class Teacher(Person):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age)
        self.salary = salary
        self.subject = subject
    def display(self):
        super().display()
        print ('Salary:', self.salary)
        print ("Subject:", self.subject)
s=Student("Neer", 31, 7, 90)
t=Teacher("Sam", 32, 10000, "Python")
s.display()
t.display()
___________________________________________________

# Creating a Thread without using any class
from threading import *
def display():
        for i in range (10):
            print ("Child Thread")
t=Thread(target=display)
t.start()
for i in range (10):
    print ("Main thread")

# Creating a Thread by extending Thread class
from threading import *
class MyThread(Thread):
    def run(self):
        for i in range (10):
            print ("Child Thread")
t=MyThread()
t.start()
for i in range (10):
    print ("Main thread")

# Creating a Thread without extending Thread class
from threading import *
class Test:
    def m1(self):
        for i in range (10):
            print ("Child Thread....")
obj=Test()
t=Thread(target=obj.m1)
t.start()
for i in range (10):
    print ("Main thread....") 

# setting and getting name of the thread
from threading import *
print(current_thread().getName())
current_thread().setName("Dimpy")
print(current_thread().getName())
print(current_thread().name)

# another example
from threading import *
def display():
        for i in range (10):
            print ("Child Thread")
t=Thread(target=display, name="Dimpy")
t.start()
for i in range (10):
    print ("Main thread")

# Tread Identification Number
from threading import *
def test():
    pass
t=Thread(target=test)
t.start()

print("Main thread Identification Number:", current_thread().ident)
print("child thread Identification Number:", t.ident)
__________________________________________________________________________
# active count
from threading import *
import  time
def display():
    print(current_thread().name, "started...")
    print(current_thread().name, "Identification Number is", current_thread().ident)
    time.sleep(3)
    print(current_thread().name, "...ended")
print("Number of active thread:", active_count())
t1=Thread(target=display, name="Child thread 1")
t2=Thread(target=display, name="Child thread 2")
t3=Thread(target=display, name="Child thread 3")
t1.start()
t2.start()
t3.start()
print("Number of active thread:", active_count())
time.sleep(10)
print("Number of active thread:", active_count())

____________________________________________________________

# enumerate():
from threading import *
import  time
def display():
    print(current_thread().name, "started...")
    print(current_thread().name, "Identification Number is", current_thread().ident)
    time.sleep(3)
    print(current_thread().name, "...ended")
print("Number of active thread:", active_count())
t1=Thread(target=display, name="Child thread 1")
t2=Thread(target=display, name="Child thread 2")
t3=Thread(target=display, name="Child thread 3")
t1.start()
t2.start()
t3.start()
l=enumerate()
for i in l:
    print(i.name, 'Ident No.', i.ident)
print("Number of active thread:", active_count())
time.sleep(10)
print("Number of active thread:", active_count())

________________________________________________________
class Movie:
    def __init__(self, title, hero, heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine
    def info (self):
        print('Movie Name:', self.title)
        print('Hero Name:', self.hero)
        print('Heroine Name:', self.heroine)-55
list_of_movies=[]
while True:
    title=input ('Enter Movie Name:')
    hero=input ('Enter Movie hero:')
    heroine=input ('Enter Movie Heroine:')
    m=Movie(title,hero,heroine)
    list_of_movies.append(m)
    print('Movie added to the list successfully')
    option=input('Do you want to add one more movie [Yes|No]:')
    if option.lower()=='no':
        break
print ('all movies information')
print('#'*40)
for movie in list_of_movies:
    movie.info()

___________________________________________________________________
# interview question in liveFurnish
l=[4,2,3,1,1,2,4,2,2]
d={}
for i in l:
    count=0
    for j in l:
        if i==j:
            count = count + 1
        d [i] = count
print (d)

#Live Furnish
from PIL import Image
import os
from os import listdir
from os.path import isfile, join
rootPath= 'C:/Work/Black/Black'
fileName=[f for f in listdir(rootPath + '/Pillow_1') if isfile(join(rootPath + '/Pillow_1', f))]

directory = "Final"
path_dir = rootPath
if not os.path.exists(directory):
	os.mkdir(os.path.join(path_dir, directory))

i=0
while i<len(fileName):
    pillow1 = rootPath + '/Pillow_1/' + fileName[i]
    pillow2 = rootPath + '/Pillow_2/' + fileName[i]
    pillow3 = rootPath + '/Pillow_3/' + fileName[i]
    seat = rootPath + '/Seat/' + fileName[i]
    sofa = rootPath + '/sofa/' + fileName[i]

    # Open Image
    firstImage = Image.open(pillow1)
    secondImage = Image.open(pillow2)
    thirdImage = Image.open(pillow3)
    fourthImage = Image.open(seat)
    fifthImage = Image.open(sofa)
  
    # Convert image to RGBA
    firstImage = firstImage.convert("RGBA")
    secondImage = secondImage.convert("RGBA")
    thirdImage = thirdImage.convert("RGBA")
    fourthImage = fourthImage.convert("RGBA")
    fifthImage = fifthImage.convert("RGBA")


    # Merge the Image
    secondImage.paste(firstImage,(0, 0), firstImage )
    thirdImage.paste(secondImage,(0, 0), secondImage)
    fourthImage.paste(thirdImage,(0, 0), thirdImage)
    fifthImage.paste(fourthImage,(0, 0), fourthImage)
    # Save this image
    fifthImage.save(rootPath + '/Final/'+fileName[i]+'.png', format="png")
    i=i+1
print('All images merged and saved.')


#########################################
# transparent
    def transparent(img):
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
            img.putdata(newData)
        return(newData)

-----------------------------------------------------
# transparent
    datas = firstImage.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    firstImage.putdata(newData)
    
    datas = secondImage.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    secondImage.putdata(newData)

    datas = thirdImage.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    thirdImage.putdata(newData)

    datas = fourthImage.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    fourthImage.putdata(newData)

    datas = fifthImage.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    fifthImage.putdata(newData)

# Black
from PIL import Image
import os
from os import listdir
from os.path import isfile, join
rootPath= 'C:/Work/Black/Black'
fileName=[f for f in listdir(rootPath + '/Pillow_1') if isfile(join(rootPath + '/Pillow_1', f))]

directory = "Final"
path_dir = rootPath
if not os.path.exists(directory):
	os.mkdir(os.path.join(path_dir, directory))



i=0
while i<len(fileName):
    pillow1 = rootPath + '/Pillow_1/' + fileName[i]
    pillow2 = rootPath + '/Pillow_2/' + fileName[i]
    pillow3 = rootPath + '/Pillow_3/' + fileName[i]
    seat = rootPath + '/Seat/' + fileName[i]
    sofa = rootPath + '/sofa/' + fileName[i]

    # Open Image
    firstImage = Image.open(pillow1)
    secondImage = Image.open(pillow2)
    thirdImage = Image.open(pillow3)
    fourthImage = Image.open(seat)
    fifthImage = Image.open(sofa)

    # Convert image to RGBA
    firstImage = firstImage.convert("RGBA")
    secondImage = secondImage.convert("RGBA")
    thirdImage = thirdImage.convert("RGBA")
    fourthImage = fourthImage.convert("RGBA")
    fifthImage = fifthImage.convert("RGBA")

    # transparent
    datas = firstImage.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    firstImage.putdata(newData)
    
    datas = secondImage.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    secondImage.putdata(newData)

    datas = thirdImage.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    thirdImage.putdata(newData)

    datas = fourthImage.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    fourthImage.putdata(newData)

    datas = fifthImage.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    fifthImage.putdata(newData)
    
    # Merge the Image
    secondImage.paste(firstImage,(0, 0), firstImage )
    thirdImage.paste(secondImage,(0, 0), secondImage)
    fourthImage.paste(thirdImage,(0, 0), thirdImage)
    fifthImage.paste(fourthImage,(0, 0), fourthImage)
    # Save this image
    fifthImage.save(rootPath + '/Final/'+fileName[i]+'.png', format="png")
    i=i+1
print('All images merged and saved.')


_____________________________________________________
# Convert image to RGBA
    firstImage = firstImage.convert("RGBA")
    secondImage = secondImage.convert("RGBA")
    thirdImage = thirdImage.convert("RGBA")
    fourthImage = fourthImage.convert("RGBA")
    fifthImage = fifthImage.convert("RGBA")
# Half alpha
    firstImage.putalpha(240)
    secondImage.putalpha(240)
    thirdImage.putalpha(240)
    fourthImage.putalpha(240)
    fifthImage.putalpha(240)

# Merge the Image
    secondImage.paste(firstImage,(0, 0), firstImage )
    thirdImage.paste(secondImage,(0, 0), secondImage)
    fourthImage.paste(thirdImage,(0, 0), thirdImage)
    fifthImage.paste(fourthImage,(0, 0), fourthImage)
-------------------------------------------------------------------------------------------------------------
#single Image transparent

from PIL import Image
import os
from os import listdir
from os.path import isfile, join
rootPath= 'C:/Work/Black/Black'
fileName=[f for f in listdir(rootPath + '/Pillow_1') if isfile(join(rootPath + '/Pillow_1', f))]

pillow1 = rootPath + '/Pillow_1/' + fileName[0]
firstImage = Image.open(pillow1)
# Convert image to RGBA
firstImage = firstImage.convert("RGBA")
datas = firstImage.getdata()
newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
  
firstImage.putdata(newData)
firstImage.save("./New.png", "PNG")
print("Successful")
--------------------------------------------------------------------------------------------------------
from PIL import Image
import os
from os import listdir
from os.path import isfile, join
rootPath= 'C:/Work/Black/Black'
fileName=[f for f in listdir(rootPath + '/Pillow_1') if isfile(join(rootPath + '/Pillow_1', f))]

directory = "Final"
path_dir = rootPath
if not os.path.exists(directory):
	os.mkdir(os.path.join(path_dir, directory))

class abc():
    def t(x):
        datas = x.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        x.putdata(newData)
        return x

i=0
while i<len(fileName):
    pillow1 = rootPath + '/Pillow_1/' + fileName[i]
    pillow2 = rootPath + '/Pillow_2/' + fileName[i]
    pillow3 = rootPath + '/Pillow_3/' + fileName[i]
    seat = rootPath + '/Seat/' + fileName[i]
    sofa = rootPath + '/sofa/' + fileName[i]

    # Open Image
    firstImage = Image.open(pillow1)
    secondImage = Image.open(pillow2)
    thirdImage = Image.open(pillow3)
    fourthImage = Image.open(seat)
    fifthImage = Image.open(sofa)

    # Convert image to RGBA
    firstImage = firstImage.convert("RGBA")
    secondImage = secondImage.convert("RGBA")
    thirdImage = thirdImage.convert("RGBA")
    fourthImage = fourthImage.convert("RGBA")
    fifthImage = fifthImage.convert("RGBA")

    # transparent
    firstImage= abc.t(firstImage)
    secondImage= abc.t(secondImage)
    thirdImage= abc.t(thirdImage)
    fourthImage= abc.t(fourthImage)
    fifthImage= abc.t(fifthImage)

    # Merge the Image
    secondImage.paste(firstImage,(0, 0), firstImage )
    thirdImage.paste(secondImage,(0, 0), secondImage)
    fourthImage.paste(thirdImage,(0, 0), thirdImage)
    fifthImage.paste(fourthImage,(0, 0), fourthImage)
    # Save this image
    fifthImage.save(rootPath + '/Final/'+fileName[i]+'.png', format="png")
    i=i+1
print('All images merged and saved.')
----------------------------------------------------------------------------------------------------
#Test
from PIL import Image
import os
from os import listdir
from os.path import isfile, join
rootPath= 'C:/Work/option2/option2'
fileName=[f for f in listdir(rootPath + '/Pillow_1') if isfile(join(rootPath + '/Pillow_1', f))]

""" directory = "Test"
path_dir = rootPath
if not os.path.exists(directory):
	os.mkdir(os.path.join(path_dir, directory)) """

""" class abc():
def t(x):
    datas = x.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    x.putdata(newData)
    return x """

pillow1 = rootPath + '/Pillow_1/' + fileName[0]
pillow2 = rootPath + '/Pillow_2/' + fileName[0]
pillow3 = rootPath + '/Pillow_3/' + fileName[0]
seat = rootPath + '/Seat/' + fileName[0]
sofa = rootPath + '/sofa/' + fileName[0]

    
    # Open and Convert image to RGBA
""" firstImage = Image.open(pillow1).convert("RGBA")
secondImage = Image.open(pillow2).convert("RGBA")
thirdImage = Image.open(pillow3).convert("RGBA")
fourthImage = Image.open(seat).convert("RGBA")
fifthImage = Image.open(sofa).convert("RGBA") """

""" # transparent
    firstImage= abc.t(firstImage)
    secondImage= abc.t(secondImage)
    thirdImage= abc.t(thirdImage)
    fourthImage= abc.t(fourthImage)
    fifthImage= abc.t(fifthImage) 
     # alpha
    firstImage.putalpha(255)
    secondImage.putalpha(255)
    thirdImage.putalpha(255)
    fourthImage.putalpha(255)
    fifthImage.putalpha(255) """
# Merge the Image
secondImage.paste(firstImage,(0, 0), firstImage )
thirdImage.paste(secondImage,(0, 0), secondImage)
fourthImage.paste(thirdImage,(0, 0), thirdImage)
fifthImage.paste(fourthImage,(0, 0), fourthImage)
    # Save this image
# fifthImage.save(rootPath + '/Final/'+fileName[0]+'.png', format="png")
fifthImage.show()
---------------------------------------------------------------------------------------------------
# Merge the Image
    for n in range (40):
        secondImage=secondImage.paste(firstImage,(0, 0), firstImage)
        secondImage = Image.open(secondImage)
        thirdImage=thirdImage.paste(secondImage,(0, 0), secondImage)
        thirdImage = Image.open(thirdImage)
        fourthImage=fourthImage.paste(thirdImage,(0, 0), thirdImage)
        fourthImage = Image.open(fourthImage)
        fifthImage=fifthImage.paste(fourthImage,(0, 0), fourthImage)
        fifthImage = Image.open(fifthImage)
        firstImage=firstImage.paste(fifthImage,(0, 0), fifthImage)
        firstImage = Image.open(firstImage)

#makeShadow
def makeShadow(image, iterations=3, backgroundColour=0xffffff, shadowColour=0x444444, offset=(5,5), border=8):
    # image: base image to give a drop shadow
    # iterations: number of times to apply the blur filter to the shadow
    # border: border to give the image to leave space for the shadow
    # offset: offset of the shadow as [x,y]
    # backgroundCOlour: colour of the background
    # shadowColour: colour of the drop shadow
    
    #Calculate the size of the shadow's image
    fullWidth  = image.size[0] + abs(offset[0]) + 2*border
    fullHeight = image.size[1] + abs(offset[1]) + 2*border
    
    #Create the shadow's image. Match the parent image's mode.
    shadow = Image.new(image.mode, (fullWidth, fullHeight), backgroundColour)
    
    # Place the shadow, with the required offset
    shadowLeft = border + max(offset[0], 0) #if <0, push the rest of the image right
    shadowTop  = border + max(offset[1], 0) #if <0, push the rest of the image down
    #Paste in the constant colour
    shadow.paste(shadowColour, 
                [shadowLeft, shadowTop,
                 shadowLeft + image.size[0],
                 shadowTop  + image.size[1] ])
    
    # Apply the BLUR filter repeatedly
    for i in range(iterations):
        shadow = shadow.filter(ImageFilter.BLUR)

    # Paste the original image on top of the shadow 
    imgLeft = border - min(offset[0], 0) #if the shadow offset was <0, push right
    imgTop  = border - min(offset[1], 0) #if the shadow offset was <0, push down
    shadow.paste(image, (imgLeft, imgTop))

    return shadow

fifthImage= makeShadow(fifthImage,iterations=3, shadowColour=(0x00,0x00,0x00,0xff), border=0)


------------------------------------------------------------------------------------------------------------
from PIL import Image
import os
from os import listdir
from os.path import isfile, join
import numpy

thirdImage = Image.open('C:/Work/option2/option2/Final/00001.png')
R, G, B, A = thirdImage.convert('RGBA').split() 

alpha = A.load()

w, h = A.size

npimage= numpy.array(A)
npimage[npimage>0]= 255
arr2im = Image.fromarray(npimage)
  

alpha = Image.merge('RGBA', (R, G, B,arr2im))
alpha.show()
alpha.save('C:/Work/og_a.png', format="png")

-------------------------------------------------------------------------------------------------------------------------------
from PIL import Image, ImageFilter
import os
from os import listdir
from os.path import isfile, join
import numpy
import time

rootPath= 'C:/Work/All/All/'
finalPath= 'C:/Work/All/merged/'

folder = os.listdir(rootPath)
fileName=[f for f in listdir(rootPath + folder[0]) if isfile (join(rootPath + folder[0], f))]

begintime=time.time()
i=0
while i<len(fileName):
    pillow1 = rootPath + folder[0] + '/' + fileName[i]
    pillow2 = rootPath + folder[1] + '/' + fileName[i]
    pillow3 = rootPath + folder[2] + '/' + fileName[i]
    seat = rootPath + folder[3] + '/' + fileName[i]
    sofa = rootPath + folder[4] + '/' + fileName[i]

    # Open Image
    firstImage = Image.open(pillow1)
    secondImage = Image.open(pillow2)
    thirdImage = Image.open(pillow3)
    fourthImage = Image.open(seat)
    fifthImage = Image.open(sofa)

    # Merge the Image

    secondImage=Image.alpha_composite(firstImage, secondImage)
    thirdImage=Image.alpha_composite(secondImage, thirdImage)
    fourthImage=Image.alpha_composite(thirdImage, fourthImage)
    fifthImage=Image.alpha_composite(fourthImage, fifthImage)

    finalImage = fifthImage
    R, G, B, A = finalImage.convert('RGBA').split() 
    alpha = A.load()
    npimage=numpy.array(A)
    npimage[npimage>10]= 255

    arr2im = Image.fromarray(npimage)
    arr2im = arr2im.filter(ImageFilter.GaussianBlur(radius = 0.1))
    alpha = Image.merge('RGBA', (R,G,B, arr2im))
    alpha.save(finalPath+fileName[i], format="png", optimize=False, compress_level=0)
    i=i+1
    break
print("The total time taken:",time.time()-begintime)

----------------------------------------------------------------------------------------------------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i in range(0, 1500):
        if npimage[i, 0:2] == (255,255,255) and npimage[i+100, 0:2]== (255,255,255):
            for j in range (npimage[i], npimage[i+100]):
                npimage[j, 0:2]== (255,255,255)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-----------------------------------------------------------------------------------------------------------------------------------
class student:
    def __init__(self, name, age, city):
        self.name=name
        self.age=age
        self.city=city

    def below_30(self):
        return self.age <= 30
            
        

s1=student(name="Rama", age = 35, city='Lucknow')
s2=student(age=25, name='Shyama', city='Goa')
s3=student(city='Kochi', age=33, name='Hari')
s4=student("Om", 22, 'Chennai')
list_Student=[s1,s2,s3,s4]



for i in range(len(list_Student)):
    print (list_Student[i].name)
    print (list_Student[i].age)
    print (list_Student[i].city)
    print('*'*10)

for i in range (len(list_Student)):
    if(list_Student[i].below_30()):
        print (list_Student[i].name) 

print("--"*10)

list_Student_below_30=list(filter(student.below_30, list_Student))

for i in range(len(list_Student_below_30)):
    print (list_Student_below_30[i].name)
    print (list_Student_below_30[i].age)
    print (list_Student_below_30[i].city)
    print('^'*10)
------------------------------------------------------------------------------------------------------------------------------------
class Human:
    def __init__(self,name):
        self.name=name
        self.head=self.Head()
    def info(self):
        print("Hello my self", self.name)
        print ("I am", self.head.talk(), "and ", self.head.brain.think()) 
    class Head:
        def __init__(self):
            self.brain=self.Brain()
        def talk(self):
            print("talking...")
        class Brain:
            def think(self):
                print("thinking...")
human=Human("neeraj")
human.info()
--------------------------------------------------------------------------------------------------------------------------------------
class Person:
    def __init__(self,name,dd,mm,yyyy):
        self.name=name
        self.dob=self.DOB(dd,mm,yyyy)
        
    def info(self):
        print("name:", self.name)
        self.dob.display()

    class DOB:
        def __init__(self,dd,mm,yyyy):
            self.date=dd
            self.month=mm
            self.year=yyyy
        def display(self):
            print("DOB: {}/{}/{}".format(self.date, self.month, self.year))
p1=Person("Neer",7,9,1989)
p1.info()

----------------------------------------------------------------------------------------------------------
# clock time real time clock watch
import time
from datetime import datetime
while True:   
    now = datetime.now()
    print (now.strftime("%m/%d/%Y %H:%M:%S"), end="\r", flush=True)
    time.sleep(1)
-------------------------------------------------------------------------------------------------------
from  tkinter import *
import time 

def times():
    current_time=time.strftime("%H:%M:%S") 
    clock.config(text=current_time)
    clock.after(200,times)


root=Tk()
root.geometry("450x140")
clock=Label(root,font=("times",50,"bold"),bg="black",fg='yellow')
clock.grid(row=2,column=2,pady=25,padx=100)
times()

root.mainloop()
----------------------------------------------------------------------------------------------------------------
# Fake data
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djproject.settings')
import django
django.setup()

from newsapp.models import *
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range (9):
        num=num+str(randint(0,9))
    return int(num)
def populate():
    for i in range (n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=("Project Manager","Team Lead","Full Stack Developer","Front End Developer"))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hydjobs_records=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,address=faddress,email=femail,phonenumber=fphonenumber)
populate(30)
----------------------------------------------------------------------------------------------------------------
class P():
    def __init__(self) -> None:
        print('Parent Constructor')
    def m1(self):
        print("Instance Method")
    @classmethod
    def m2(cls):
        print("Class Method ")
    @staticmethod
    def m3():
        print ("Static Method")
class C(P):
    def __init__(self) -> None:
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    @classmethod
    def m2(cls):
        super(C,cls).__init__(cls)
        super(C,cls).m1(cls)
        super().m2()
        super().m3()
    @staticmethod
    def m3():
        # super(C,C).__init__()
        # super(C,C).m1()
        super(C,C).m2()
        super(C,C).m3()
c=C()
print()
c.m3()
_____________________________________________________________
# Exception Handling
try:
    print(10/0)
except ZeroDivisionError as msg:
    print("Type of Error is : ", type(msg))
    print("Type of Error is : ", msg.__class__)
    print("Exception class name : ", msg.__class__.__name__)
    print("Exception description : ", msg)
    ------------------------------------------------------------
try:
    x=int(input('Enter first number:'))
    y=int(input('Enter second number:'))
    print('The result is : ', x/y )
except BaseException as msg:
    print("Type of Error is : ", type(msg))
    print("Type of Error is : ", msg.__class__)
    print("Exception class name : ", msg.__class__.__name__)
    print("Exception description : ", msg)
----------------------------------------------------------------
try:
    x=int(input('Enter first number:'))
    y=int(input('Enter second number:'))
    print('The result is : ', x/y )
except ZeroDivisionError :
    print("can't divide with Zero ")
    
except ValueError :
    print("Enter only int value")
    ------------------------------------------------------------

try:
    x=int(input('Enter first number:'))
    y=int(input('Enter second number:'))
    print('The result is : ', x/y )
except ZeroDivisionError :
    print("ZeroDivisionError: can't divide with Zero ")
    
except:      # default except block should be last in order
    print("Default except block: Please enter a valid value")
    --------------------------------------------------------------------
Patterns

n=int(input('Enter a number:'))
for i in range(1, n+1):
    print ('{}'.format (i) *i)


n=int(input('Enter a number:'))
for i in range (1, n+1):
    print(" "*(n-i),end="")
    for j in range(1,2):
        print("*" *(2*i-1),end="")
    print()

Enter a number:5
    *
   ***
  *****
 *******
*********
-----------------------------------------------------------
n=int(input('Enter a number:'))
for i in range (1, n+1):
    print(" "*(n-i),end="")
    for j in range(1,2):
        print("*" *(2*i-1),end="")
    print()

Enter a number:6
     *     
    ***    
   *****   
  *******  
 ********* 
***********