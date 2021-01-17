#1)menu -driven:sorting algorithms
"""def insert(lst):
    a=len(lst)
    for i in range(1,a):
        b=lst[i]
        j=i-1
        while j>=0 and b<lst[j]:
            lst[j+1]=lst[j]
            j-=1
            lst[j+1]=b
    return lst

def selection(lst):
    for i in range(0,len(lst)):
        b=i
        for j in range(i+1,len(lst)):
            if lst[b]>lst[j]:
                c=j
                lst[i],lst[c]=lst[c],lst[i]
    return lst

def bubble(lst):
    for i in range(len(lst)):
        for j in range(0,len(lst)-i-1):
            if lst[j]>lst[j+1]:
               lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

#main
lst=[]
flag=True
while flag:
    a=int(input("enter element:"))
    lst.append(a)
    flag=bool(int(input("do you want to continue?(1/0)")))

flag1=True
while flag1:
    x=int(input("enter your choice of sorting algorithm:\n1.Press 1 for bubble\n2.Press 2 for insertion\n3.Press 3 for selection.\n"))
    if x==1:
        print(bubble(lst))
    elif x==2:
        print(insert(lst))
    elif x==3:
        print(selection(lst))
    else:
        print("Invalid choice!")
    flag1=bool(int(input("Do you want to continue?(1/0):")))
print("This is the end.)"""

# 2)recursion :factorial
"""def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

flag=True
while flag:
   num=int(input("enter the number whose factorial you want to see:"))
   if num < 0:
      print("Sorry, factorial does not exist for negative numbers")

   elif num == 0:
      print("The factorial of 0 is 1")
   else:
      print("The factorial of", num, "is", recur_factorial(num))
   flag=bool(int(input("Do you want to continue?(1/0):")))
print("This is the end.")"""

# 3)palindrome checking


"""def check_palindrome(a):

    if(a==a[::-1]):
      print("The string is a palindrome")
    else:
      print("The string isn't a palindrome")
#main
flag=True
while flag:
   string=input("enter the number who you want to check:")

   check_palindrome(string)
   flag=bool(int(input("do you want to continue:")))
"""


# 4)binary file:add ,update
"""import pickle as p
def add(filename):
    f = open(filename, "ab")
    lst=[]
    flag=True
    while flag:
        roll = int(input("enter your rollno.:"))
        text = input("enter your required text:")
        R=[roll,text]
        lst.append(R)
        flag = bool(int(input("do you want to continue?(1/0)")))
    p.dump(lst,f)

    print("data appended.")
    f.close()
def update(filename):
    lst=[]
    found=0
    try:
        f=open(filename,"rb")
        lst=p.load(f)
    except EOFError:
        print("ok")
    f.close()
    f=open(filename,"wb")
    for i in lst:
        print(i)
    x=int(input("enter roll no you want to modify:"))
    for j in range(len(lst)):
        if lst[j][0]==x:
            found=1
            text=input("enter new text:")
            lst[j][1]=text
            print("DONE!")
    if found==0:
        print("data not found...")
    p.dump(lst,f)
    f.close()
#MAIN
filename=input("enter your filename:")

while True:
    x=int(input("1.Add\n2.Update\n"))
    if x==1:
       add(filename)
    elif x==2:
       update(filename)
    elif x==3:
        break
    else:
        print("Invalid Choice!")"""

#5)binary file:delete,search
"""import pickle as p

def delete(filename):
    f=open(filename,"rb+")
    Rec=p.load(f)
    found=0
    K=[]
    x=int(input("enter the rollno. to be deleted"))
    for i in Rec:
        if i[0]==x:
            found+=1
        else:
            K.append(i)
    if found==0:
        print("data not found....")
    else:
        f.seek(0)
        p.dump(K,f)
    f.close()

def search(filename):
    f=open(filename,"rb")
    s=p.load(f)
    found=0
    flag=True
    while flag:
        x=int(input("enter the roll no to be searched."))
        for i in s:
            if i[0]==x:
               print("record found....")
               print(i[0],i[1])
               found=1
        if found==0:
            print("record not found...")

        flag=bool(int(input("do you want to continue?(1/0)")))
    f.close()
#main
filename=input("enter your filename:")

while True:
    x=int(input("1.delete\n2.Search\n3.exit?"))
    if x==1:
       delete(filename)
    elif x==2:
       search(filename)
    elif x==3:
        break
    else:
        print("Invalid Choice")"""
#6)binary search
"""def binary_search(item_list,item):
    item_list.sort()
    first=0
    last=len(item_list)-1
    found=False
    while (first<=last and not found):
        mid=(first+last)//2
        if item_list[mid]==item:
            found=True
        else:
            if item<item_list[mid]:
                last=mid-1
            else:
                first=mid+1
    return found
lst=[]
c=1
flag=True
while flag:
    a=int(input(f"enter element {c}:"))
    lst.append(a)
    flag=bool(int(input("do you want to continue?(1/0)")))
    c+=1
flag1=True
while flag1:
    item=int(input("what do you want to search?"))
    print(binary_search(lst,item))
    flag1=bool(int(input("do you want to continue?")))"""

#7)linear search
"""
def linear(lst):
    c=0
    x=int(input("enter number to be searched:"))
    for i in range(0,len(lst)):
        if lst[i]==x:
            print( lst[i])
            print("your element has been found.")
            c=1
        else:
            pass
    if c==0:
        print("your element is not found...")
lst=[]
c=1
flag=True
while flag:
    a=int(input(f"enter element {c}:"))
    lst.append(a)
    flag=bool(int(input("do you want to continue?(1/0)")))
flag1=True
while flag1:
    linear(lst)
    flag1=bool(int(input("do you want to continue?")))
print("This is the end...")
"""
#8)Operations on: Stack
"""def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1
def pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
def Peek(stk):
    if isEmpty(stk):
        print("Stack Empty!")
    else:
        top=len(stk)-1
        return stk[top]
def Display(stk):
    if isEmpty(stk):
        print("Stack Empty")
    else:
        top=len(stk)-1
        print(stk[top],"<--top")
        for i in range(top-1,-1,-1):
            print(stk[i])
#main
flag=True
Stack=[]
top=None
while True:
    print("Stack Operations\n1.Push\n2.Pop\n3.Peek\n4.Display Stack\n5.Exit")
    x=int(input("Enter your choice(1-5):"))
    if x==1:
        while flag:
            item=int(input("Enter item:"))
            Push(Stack,item)
            flag=bool(int(input("do you want to add more?:")))
    elif x==2:
        item=pop(Stack)
        if item=="Underflow":

            print("Underflow! the Stack is empty!")
        else:
            print("Popped item is :",item)
    elif x==3:
        item=Peek(Stack)
        if item=="Underflow":
            print("Stack is empty!")
        else:
            print("Topmost item is:",item)
    elif x==4:
        Display(Stack)
    elif x==5:
        break
    else:
        print("Invalid choice!")
"""
#9)Operations on:Queue

"""Queue = []
front = None
rear = None
choice = True


def Enqueue(Queue):
    global front, rear
    choice = True
    while choice:

        val = int(input("enter the value to be inserted into the queue:"))
        if Queue == []:
            Queue.append(val)
            front = rear = 0
        else:
            Queue.append(val)
            rear = len(Queue) - 1
        choice = bool(int(input("do you want to add more:")))
    print("contents of the queue=", Queue)
    print("the front value=", Queue[front], "the rear value is:  ", Queue[rear])
    print("the position of front value is=", front, "/", -(rear + 1), "the position of rear value is=", rear, "/",
          front - 1)


def Dequeue(Queue):
    global front, rear
    choice = True
    while choice:
        val = Queue.pop(0)
        print("after deleting element contents of the Queue=", Queue)
        rear = len(Queue) - 1
        if (Queue != []):
            print("contents of the queue=", Queue)
            print("the front value=", Queue[front], "the rear value is:  ", Queue[rear])
            print("the position of front value is=", front, "/", -(rear + 1), "the position of rear value is=", rear,
                  "/", front - 1)
        else:
            return
        choice = bool(int(input("enter do you want to delete more:")))


def Peek(Queue):
    if Queue == []:
        print("Underflow")
    else:
        front = 0
        print("here front value is:", Queue[front])


a = True
while a:
    print(
        "\n1. Insertion in Queue.\n2. Deletion in Queue.\n3. Display the Queue.\n4. press 4 for exit.\n5. Press 5 to Peek\n")
    c = int(input("Enter your choice from the above.(1-5)"))
    if c == 1:
        Enqueue(Queue)

    elif c == 2:
        if Queue == []:
            print("Now deletion cannot be done as it is Underflow condition. ")
        else:
            Dequeue(Queue)
    elif c == 3:
        if Queue == []:
            print("Queue is empty.")
        else:
            for i in range(rear + 1):
                print(Queue[i], end="<---")
            print("\n")
    elif c == 4:
        a = False
    elif c == 5:
        Peek(Queue)
    else:
        print("Invalid choice!")
"""

# 10)Insertion in linear list
"""def FindPos(lst,item):
    size=len(lst)
    if item<lst[0]:
        return 0
    else:
        pos=-1
    for i in range(size-1):
        if (lst[i]<=item and item<lst[i+1]):
                pos=i+1
                break
    if (pos==-1 and i<=size-1):
        pos=size
    return pos
def Shift(lst,pos):
    lst.append(None)
    size=len(lst)
    i=size-1
    while i>=pos:
        lst[i]=lst[i-1]
        i-=1
lst=[]
flag=True
c=1
while flag:
    a=int(input(f"enter element {c}:"))
    lst.append(a)
    flag=bool(int(input("do you want to continue?(1/0)")))
    c+=1
print("This is the list:\n",lst)
item=int(input("Enter new element to be inserted:"))
position=FindPos(lst,item)
Shift(lst,position)
lst[position]=item
print("The list after inserting :",item,"is")
print(lst)"""
#11)Deletion in Linear list
"""def Bsearch(lst,item):
    lst.sort()
    first=0
    last=len(lst)-1
    while (first<=last):
        mid=(first+last)//2
        if item==lst[mid]:
            return mid
        elif (item>lst[mid]):
            first=mid+1
            
        else:
            last=mid-1
    else:
        return False
lst=[]
flag=True
c=1
while flag:
    a=int(input(f"enter element {c}:"))
    lst.append(a)
    flag=bool(int(input("do you want to continue?(1/0)")))
    c+=1
print("This is the list:\n",lst)
item=int(input("Enter new element to be Deleted:"))
position=Bsearch(lst,item)
if position:
    del lst[position]
    print("The list after deleting ",item,"is")
    print(lst)
else:
    print("Sorry! no such element exists in the list")
"""
#12)Circular Queue Implementation in Python
max_Queue=int(input("Enter size of Queue:"))
__frontPointer = 0
__rearPointer  = max_Queue-1
__size = 0
queue = []
for i in range(max_Queue):
	queue.append('')


def display(queue,max_Queue): # Print magic method
        global __frontPointer,__rearPointer,__size
        string = '\n'
        for i in range(max_Queue):
            string += '{}'.format(i) + ' : ' + str(queue[i]) + '\n'
        string += '\n'
        string += 'Front Pointer : ' + str(__frontPointer) +'\n'
        string += 'Rear Pointer  : ' + str(__rearPointer)  +'\n'
        string += 'Size          : ' + str(__size)         +'\n'
        return string

def __isEmpty(queue):
        global __size
        return __size == 0

def __isFull(queue,max_Queue):
        global __size
        return __size == max_Queue

def enqueue(queue,max_Queue,item):
        global __rearPointer,__size
        if __isFull(queue,max_Queue):
            print("Queue is full.")
            return False
        else:

            __rearPointer = (__rearPointer + 1) % max_Queue  #circular increment
            queue[__rearPointer] = item
            __size += 1



def dequeue(queue,max_Queue):
	global __rearPointer,__frontPointer,__size
	if __isEmpty(queue):
		print("Queue is empty.")
		return False
	else:
		dequeued = queue[__frontPointer]
		queue[__frontPointer] = ''
		__frontPointer = (__frontPointer + 1) % max_Queue
		__size -= 1
		print("Element", dequeued, "is removed")

while True:
	x = int(input("1.Enter 1 for EnQueue\n2.Enter 2 for DeQueue\n3.Enter 3 for Display\n4.Press 4 for Exit"))
	if x == 1:
		a = int(input("Enter element for EnQueue:"))
		enqueue(queue,max_Queue,a)
		if __isFull(queue,max_Queue)==False:
			print("Element added")

	elif x == 2:
		dequeue(queue,max_Queue)
	elif x == 3:
		print(display(queue,max_Queue))
	elif x == 4:
		break
	else:
		print("Invalid Choice!")
#13) Data structures Q10
"""def select_errors(STL):
    newList=[]
    for record in STL:
        name_surname=record.split(' ')
        name=name_surname[0]
        surname=name_surname[1]
        if name[0].islower() or surname[0].islower():
            newList.append(record)
    return newList

def select_correct(STL):
    newList=[]
    for record in STL:
        name_surname=record.split(' ')
        name=name_surname[0]
        surname=name_surname[1]
        if not name[0].islower() and not surname[0].islower():
            newList.append(record)
    return newList

def correct_entries(STL):
    newList = []
    for record in STL:
        name_surname = record.split(' ')
        name = name_surname[0]
        surname = name_surname[1]
        newList.append(name.capitalize()+' ' + surname.capitalize())
    return newList
STL=[]
flag=True
while flag:
    print("\t---")
    print("\tMENU")
    print("\t---")
    print("1. Apply for the school Post\n2.List of all applicants\n3. Correct the Incorrect Entries\n4.Exit")
    ch=int(input("Enter your choice(1-4):"))
    if ch==1:
        name=input("Enter your name:")
        STL.append(name)
    elif ch==2:
        print("Students applied so far:")
        print(STL)
    elif ch==3:
        ok_entries=select_correct(STL)
        error_entries=select_errors(STL)
        corrected_entries=correct_entries(STL)
        print("Correct entered names:",ok_entries)
        print("Incorrectly entered names:",error_entries)
        print("Corrected names:",corrected_entries)
    elif ch==4:
        break
    else:
        print("Invalid choice")
else:
    print("Thank you")"""

#14)Display the number of lines in a file.
"""def display_lines(filename):
   with open(filename,"r") as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1

flag=True
while flag:
    a=input("enter your filepath or filename:")
    display_lines(a)
    flag=bool(int(input("do you want to continue(1/0):")))
print("The END")"""

#15)Display the size of a file in bytes.
"""def display_bytes(filename):
    with open(filename,"r") as f:
        str1=f.read()
        size=len(str1)
        print("Size of the given text file is :",size,"bytes")
filename=input("enter filename or file path:")
display_bytes(filename)
"""
#16)print traingle
"""def traingle(n):

    m = (2 * n) - 2
    for i in range(0, n):
        for j in range(0, m):
            print(end=" ")
        m = m - 1
        for j in range(0, i + 1):

            print("* ", end=' ')
        print(" ")
n=int(input("enter height:"))
traingle(n)"""

#17)ch:3 Q9

"""def ser(a,b ) :
    d = int ( ( b - a ) / 3 )
    print("Series = " , a , a + d , a + 2*d , b )

first = int(input("Enter first Term = "))
last = int(input("Enter last Term = "))

ser(first , last )"""

#18)ch:3 Q8
"""def min(x , y ) :
    a = x % 10
    b = y % 10
    if a < b :
        return x
    else :
        return y


first = int(input("Enter first number = "))
second = int(input("Enter second number = "))

print ( "Minimum one's digit number = " , min( first , second ) )
"""



#19) Generate a Python list of all the even numbers between any two numbers
"""def generate_even(a,b):
    for i in range(a, b + 1):


        if i % 2 == 0:
           print(i, end=" ")
flag=True
while flag:
      start = int(input("Enter the start of range: "))
      end = int(input("Enter the end of range: "))
      generate_even(start,end)
      flag=bool(int(input("\ndo you want to continue:")))
print("The End.")
"""
#20)Traversing a 2D list
def traverse_2d(lst, r, c):
    print("[")
    for i in range(r):
        print("\t[", end=" ")
        for j in range(c):
            print(lst[i][j], end=" ")
        print("]")
    print("\t]")

#21)Creating a 2D list
"""def create_2D(r,c):
    lst=[]
    for i in range(r):
        row=[]
        for j in range(c):
            elem=int(input("Element ("+str(i)+","+str(j)+"):"))
            row.append(elem)
        lst.append(row)
    print("List created is:")
    traverse_2d(lst,r,c)
flag=True
while flag:
    r=int(input("how many rows?:"))
    c=int(input("How many columns:"))
    create_2D(r,c)
    flag = bool(int(input("\ndo you want to continue:")))
print("The end")
"""

#22)Data structues Type C:Q2

"""
def string_reverse(line):
    stack = [  ]
    for i in line :
        stack.append(i+i)

    stack.reverse()

    for j in stack :
        print( j , end=" ")
flag=True
while flag:
    line=input("enter a line:")
    string_reverse(line)
    flag = bool(int(input("\ndo you want to continue:")))
print("The end")
"""

#23)Data structues Type C:Q7
"""def isEmpty_2(stk):
    if stk==[]:
        return True
    else:
        return False
def  Push_2(stk,item):
    stk.append(item)
    top=len(stk)-1
def pop_2(stk):
    if isEmpty_2(stk):
        return "Underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item

def Display_2(stk):
    if isEmpty_2(stk):
        print("Stack Empty")
    else:
        top = len(stk) - 1
        print(stk[top], "<--top")
        for i in range(top - 1, -1,-1):

            print(stk[i])
Stack=[]
top=None
while True:
    print(" Operations available\n1.Push\n2.Pop\n3.Display\n4.Exit\n")
    x=int(input("Enter your choice(1-4):"))
    if x==1:
        pincode=int(input("enter pincode:"))
        city=input("Enter city:")
        record=[pincode,city]
        Push_2(Stack,record)
    elif x==2:
        record=pop_2(Stack)
        if record=="Underflow":

            print("Underflow! the Stack is empty!")
        else:
            print("Popped item is :",record)

    elif x==3:
        Display_2(Stack)
    elif x==4:
        break
    else:
        print("Invalid choice!")
print("The end")"""
#24)PYTHON PROGRAM TO GENERATE ALL POSSIBLE PERMUTATIONS IN A LIST
"""def permutation(lst):
    if len(lst) == 0:
       return []

    if len(lst) == 1:
       return [lst]

    perm = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            perm.append([m] + p)
    return perm
#--main--
lst=[]
n=int(input("Enter list size:"))
for i in range (n):
 s=int(input("Enter element:"))
 lst.append(s)
print()
print("Original list:",lst)
print("Possible permutation:")
print()
for p in permutation(lst):
 print (p)"""
#25)deleting duplicate entries
"""def remove_element(lst):
    a=[]
    for i in lst:
        if i not in a:
            a.append(i)
    return a
lst=[]
flag=True
while flag:
    x=int(input("enter element:"))
    lst.append(x)
    flag=bool(int(input("do you want to contine:")))
print("The list after removing duplicates is:",remove_element(lst))
"""
#26)Type C :Data structures 1
"""CB4=[i**3 for i in range(1,11) if i**3%4==0]
print(CB4)"""
#27)Write a program that inputs a main string and then creates an encrypted string by embedding a short symbol based string after each character
"""def encrypt(sttr,enkey):
    return enkey.join(sttr)
def decrypt(sttr,enkey):
    return sttr.split(enkey)
mainstring=input("Enter main string:")
encryptStr=input("Enter encryption key:")

enStr=encrypt(mainstring,encryptStr)
deLst=decrypt(enStr,encryptStr)
deStr="".join(deLst)
print("The encrypted string is:",enStr)
print("String after decrpytion is:",deStr)"""

#28)shifting elements
"""def Lshift(lst,n):
    for i in range(0,n):
        first=lst[0]
        for j in range(0,len(lst)-1):
            lst[j]=lst[j+1]
        lst[len(lst)-1]=first
    print("Array after left rotation",lst)
lst=[]
flag=True
while flag:
    x=int(input("enter element:"))
    lst.append(x)
    flag=bool(int(input("do you want to continue:")))
a=int(input("By how many steps:"))
print("Original Array is:",lst)
Lshift(lst,a)"""
#29)Write a program to perform read operation with .csv file."""
"""import csv
def read_csv(filename):

    with open(filename,"r") as f:


            reader=csv.reader(f)
            for i in reader:
                print(i)
filename=input("Enter filename or filepath:")
read_csv(filename)"""
#30)Write a program to perform write operation with .csv file.
"""import csv
def write_csv(filename,content):
    with open(filename,"w") as f:
        f_writer=csv.writer(f,delimiter=",")
        for i in content:
            f_writer.writerow(i)
    print("Content written!")
content=[]

flag=True
while flag:
    row = []
    x=int(input("Enter how many details in one list?:"))
    for i in range(x):
        b=input("Enter any detail:")
        row.append(b)
    content.append(row)
    flag=bool(int(input("do you want to continue?:")))
filename=input("Enter filename or filepath:")
write_csv(filename,content)
"""
#31) every number is double the previous number.
"""def diagram(rows):
    for i in range(1, rows):
        for j in range(-1+i, -1, -1):
            print(2**j, end=' ')
        print("")

x=int(input("Enter number of rows:"))
diagram(x)
"""
#32)Recursion Type C:Q1

"""def prime(num,i=2) :
    if (num<=2):
        if (num==2):
            return True
        else:
            return False
    elif (num%i==0):
        return False
    elif (i*i>num):
        return True
    return prime(num,i+1)
flag=True
while flag:
    x=int(input("Enter number you want to check:"))
    print(prime(x))
    flag=bool(int(input("Do you want to continue?:")))"""





#33)Recursion Type C:Q4
"""def sum_sq_digits(n):
    c=0
    for i in str(n):
        c+=int(i)*int(i)
    return c

def is_happy(n):
    if (len(str(n)))==1:
        if n==1:
            return "It is a happy number"
        else:
            return "It is not a happy number"
    else:
        n=sum_sq_digits(n)
        return is_happy(n)
flag=True
while flag:
    x=int(input("Enter number you want to check :"))
    print(is_happy(x))
    flag=bool(int(input("Do you want to continue?:")))"""
#34)Simulate a dice
"""import random
def rolldice():

    a=random.randint(1,6)

    return a
n=1
while n==1:
    n=int(input("Enter 1 to roll a dice and get a random number:"))
    if n==0:
        break
    print(rolldice())
"""

#========PYTHON-MYSQL CONNECTIONS==========================
#1)Create database
import pymysql
"""
def database_creation(db_name):
    db=pymysql.connect("localhost","root",'')
    cursor=db.cursor()
    cursor.execute("CREATE DATABASE {}".format(db_name))
    db.commit()
    db.close()
    print("Database created.")
db_name=input("Enter your database name:")
database_creation(db_name)"""
#2)=================Creation of table===================
"""def table_creation(db_name,tablename):

    db = pymysql.connect("localhost", "root", '',db_name)
    cursor = db.cursor()
    cursor.execute("CREATE TABLE {} (id INT AUTO_INCREMENT PRIMARY KEY,Title varchar(50),Username varchar(60)) ".format(tablename))
    db.commit()
    db.close()

flag=True
db_name=input("Enter your database name:")
while flag:
   tablename=input("Enter the name of the table you want to create:")
   table_creation(db_name,tablename)
   flag=bool(int(input("Do you want to continue?:")))"""

#3)====================AdditionOfData==============
"""def addition_of_data(db_name,tablename,content):
    db = pymysql.connect("localhost", "root", '', db_name)
    cursor = db.cursor()
    cursor.execute("insert into {} (Title,Username) values (%s,%s)".format(tablename),(content[0][0],content[0][1]))
    db.commit()
    db.close()

db_name=input("Enter your database name:")
tablename=input("Enter your table_name:")
c=1
flag=True
while flag:
    content=[]
    x=input(f"Enter Title {c}:")
    y=input(f"Enter Username {c}:")
    content.append([x,y])
    addition_of_data(db_name,tablename,content)
    c+=1
    flag = bool(int(input("Do you want to continue?:")))
print("THE END")
"""

#4)=======Select data from a data=======
"""def selection_of_data(db_name,tablename,username):
    db = pymysql.connect("localhost", "root", '', db_name)
    cursor = db.cursor()
    cursor.execute("select * from {} where Username=%s".format(tablename),(username))
    data=cursor.fetchone()
    print("Username:",data[1])
    print("Title:",data[0])

    db.close()
db_name=input("Enter your database name:")
tablename=input("Enter your table_name:")
flag=True
while flag:
    x=input("Enter username:")
    selection_of_data(db_name,tablename,x)
    flag=bool(int(input("Do you want to continue?:")))

print("THE END")"""
#5)=============Deletion of data================
"""def deletion_of_data(db_name,tablename,criteria,delete_txt):
    db = pymysql.connect("localhost", "root", '', db_name)
    cursor = db.cursor()
    cursor.execute("delete from {} where {}=%s".format(tablename,criteria),(delete_txt))
    print("Record Deleted")
    db.commit()
    db.close()
db_name=input("Enter your database name:")
tablename=input("Enter your table_name:")
flag=True
while flag:
    x=input("Enter criteria whose record you want to delete:")
    delete_txt=input("Enter the deletion text:")
    deletion_of_data(db_name,tablename,x,delete_txt)
    flag=bool(int(input("Do you want to continue?:")))

print("THE END")
"""




