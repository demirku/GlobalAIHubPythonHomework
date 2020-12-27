d = {"firstname":"kubilay", "lastname":"demir"}
lessons= ["math", "science","history" ,"art","music"]
import random

def login():

  i=0
  while i<3:

   name=input("please enter your name")
   surname=input("please enter your surname")
   d2=[name, surname]

   if (d["firstname"] == name and d["lastname"]==surname):
    print("welcome", name+surname)
    break
   else:
     print("please try again")
     i+=1

   if i==3:
    print("FAILED! PLEASE TRY AGAIN LATER")


def courses():

    x = int(input("how many course will you take? : "))
    if x<3 :
        print("you failed in class")

    else:
        takenlessons = []
    for i in range(x):
        print(lessons)
        takenlessons.append(input("write your course name like above:"))
        print(takenlessons)
        b=takenlessons
        print("your lessons are :")
 
    j = 0
    for j in range(x):
     a = {"your course": b[j], "midterm": random.randint(1,100), "final": random.randint(1,100), "project": random.randint(1,100)}
     average=a['midterm']*0.3+a['final']*0.5+a['project']*0.2
     print(a)
     if average > 90:
       print("AA")
     if 70<average<90:
       print("BB")
     if 50<average<70:
       print("CC")
     if 30<average<50:
       print("DD")
     if average<30:
       print("FAİL")       
     j=+1

login()                                                                 
courses()
