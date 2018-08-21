## In this Program I have used the random module to share variables between functions.
## I have created custom variables within the module and then append them using random.x = []


import getpass
import random
import config
import sys

## Global Variables
password = '123'
score= []


def config():


# Checks if the user wants to acces to the password manager
     def AG():
          SecureA = input('Welcome to the Secure Password Manager. Would you like to access your secret Passwords? ')
          if SecureA == 'Yes':
              files();
          else:
              print ('GoodBye!'), Start();

#Login function for the password Manager
def login():
    username = "Matthew"
    answer1 = input('User Name: ')
    password1 = input('Password: ')
    if password1 == 'password' and answer1== 'Matthew':
          print('Access Granted. '), files();
    else:
          print ('Access Denied.'), Start();

# Launcher for the ChatBot
def Start():
    random.name = input('Hello, I am S.A.M. What is your name? ')
    selection = input('Hello ' + random.name + '. What would you like to do today? (Type \'?\' for help.) ')

# Add extra arguments for the selction menu below here.
    if selection == 'Grade Checker':

        grade();
        selection = ()

    elif selection == 'Login':

        login();

    elif selection == '?':
         helper();

    elif selection == 'Joke':
         Humour();
    elif selection == 'What does S.A.M stand for?':
          SAM();

    elif selection == 'Console':
         Exit();

    else:
         print ('')
         print ('Please enter a vaild request, type \'?\' for help')
         Start();


def paint():
	print('Welcome to the paint calculator')

	WW = float(input('Please enter the width of the wall that you would like to paint: '))
	WH = float(input('And the height now please: '))
	Wall = WW * WH
	UW = float(input('Please enter the width of any unpaintable surfaces: '))
	UH = float(input('Now enter the height please: '))
	NoPaint = UW * UH
	Coats= int(input('How many coats of paint will be needed? '))
	Final = Wall - NoPaint * Coats
	print(Final)
	Start();



# Simply checks what type of number is entered, +, - or 0.
def checknumber():
    num = float(input('Enter a number: '))
    if num > 0:
        print('Positive Number')
    elif num == 0:
        print ('Zero')
    else:
        print ("Negative Number")

# User enters grade and then program prints out 'Pass', 'Fail' and what grade.
def grade():
    score = float(input('What was your grade? '))
    if 1 <= score <= 100:
        if 50 <= score <= 100:
            print ('')
            print ('You  have Passed!')

            if 50 <= score <= 60:
                 print ('Grade C'), gradeagain();
            elif 61 <= score <= 70:
                 print ('Grade B'), gradeagain();
            elif  71 <= score <= 80:
                 print ('Grade A'), gradeagain();
            elif 81 <= score <= 100:
                 print ('Grade A*'), gradeagain();


        else:
            print ('')
            print ('You have failed')

            if  0 <= score <= 19:
                 print ('Grade G'), gradeagain();
            elif 20 <= score <= 29:
                 print ('Grade F'), gradeagain();
            elif 30 <= score <= 39:
                 print ('Grade E'), gradeagain();
            elif 40 <= score <= 49:
                 print ('Grade D'), gradeagain();



    else:
            print ('Please Enter a Value Between 1 and 100')
            grade();

# Asks the user if they would like to input a second grade
def gradeagain():
     print ('')
     tryAgain = input('Would you like to submit another grade ' +random.name + '? ')
     if tryAgain == 'Yes':
          grade();
     else:
          Start();
#This reveals the password for the chosen user.
def files():
    fileName = input('Who\'s file would you like to view? ')
    if fileName == 'Matthew':
          print ('This user\'s password is ...'  + password), passwordChange();

# Facilitates the changing of the user's password. Will not function without MySQL Module
def passwordChange():
     ChangePwrd = input('Would you like to change this password?')
     if ChangePwrd == 'Yes' or 'yes':
          NP1 = input('Please input the new password: ')
          NP2 = input('Please repeat the password: ')

          if NP1 == NP2:
               NP1 = password
               print ('The Password has been changed.'), Start();
          else:
               print('The passwords do not match'), passwordchange();
     else:
          print('You have been logged out, goodbye!'), Start();

def school():
	#defroutine to display menu and validate choice
	def displayMenu():
	   #display menu of options
		print("1. input data and save to new file")
		print("2. input data and append to existing file")
		print("3. Display data")
		print("4. Quit")
		choice = input("Enter your choice: ")

	#     while choice >=1 and choice <=3:
	 #       try:
	  #          choice = int(choice)


	#        except:
	#            print ("nvailid Choice")
	#            choice = input("Enter your choice: ")
		return choice

	#defroutine to input data and save to a new file
	def saveToFile(openMode):
			textFile = open("studentNamesfile.txt",openMode)
			studentMark = "0"
			studentName = input("Enter a student name, xxx to finish : ")
			while studentName != "xxx":
				studentMark = input("Enter mark : ")
				textFile.write(studentName+","+ studentMark+"\n")
				studentName = input ("Enter a student name, xxx to finish : ")

			textFile.close




	#defroutine to display data
	def displayData():
		testResultsFile = open("studentNamesfile.txt", "r")
		read = testResultsFile.readline()
		field = read.split(",")

		while field[0]!='':
				studentName = field[0]
				result = field[1]
				read = testResultsFile.readline()
				print(studentName,result)
				field = read.split(',')



	#******************* main program starts here *********************
	option = displayMenu()

	while option != "4":
		if option == "1":
			saveToFile("w")
		elif option == "2":
			saveToFile("a")
		elif option == "3":
			displayData();

		option = displayMenu()

	print("You have chosen to quit the program"), Start();

def multiples():
	t = (int(input("Times Table: ")))
	s = (int(input("Start Number: ")))
	e = (int(input("End Number: ")))
	n = (input("Name: "))

	def multiples(t,s,e,n):
		for num in range (s, e+1):
			print (t, "x", num, " = ", t * num)

	multiples(t,s,e,n);
	Start();



def helper():
     print ('')
     print (' There are currently 3 available options:')
     print ('')
     print (' Grade Checker:    A tool to verify your exam grades.')
     print (' Login:            Login to the secure password manager.')
     print (' Help:             This Help toop that you are currently viewing')
     print (' Joke:             Tells you a joke')

     print ('')
     selection = input('What would you like to do? ')

     if selection == 'Grade Checker':
         grade();
         selection = ()

     elif selection == 'Login':
         login();

     elif selection == '?':
          helper();

     elif selection == 'Joke':
          Humour();

     else:
          Start();
# Randomly chooses a joke from the given options and pritns it.
def Humour():
     jokes = ['There are three kinds of people: those who can count and those who can\’t', 'Hand over the calculator, friends don’t let friends derive drunk.', 'If I wanted a warm fuzzy feeling, I’d antialias my graphics!', 'Mac users swear by their Mac, PC users swear at their PC.', 'The truth is out there. Anybody got the URL?']
     print(random.choice(jokes))
     Start();

def SAM():
     print ('S.A.M stands for School Assitance Manager, I am a program intended to help you with your daily school life.')
     start = input('Would you like to return to the start? ')
     if start == 'Yes':
          Start();
def Exit():
     sys.exit()

def varchange():
     random.var1 = input()
     varprint();

def varprint():
     print(random.var1)

def passtest():
    p=getpass.getpass("Enter Password:")
    print (p)
# Calls the 'start' function to start the program

def OutletSales():
	Outlet1Sales = [10, 12,15,10]
	Outlet2Sales = [5,8,3,6]
	Outlet3Sales = [10,12,15,10]

	Q1 = Outlet1Sales[0] + Outlet2Sales[0] + Outlet3Sales[0]
	Q2 = Outlet1Sales[1] + Outlet2Sales[1] + Outlet3Sales[1]
	Q3 = Outlet1Sales[2] + Outlet2Sales[2] + Outlet3Sales[2]
	Q4 = Outlet1Sales[3] + Outlet2Sales[3] + Outlet3Sales[3]

	print('Total for Q1 = ' + str(Q1) + '000')
	print('Total for Q2 = ' + str(Q2)+ '000')
	print('Total for Q3 = ' + str(Q3) + '000')
	print('Total for Q4 = ' + str(Q4) + '000')
	Start();

Start();
