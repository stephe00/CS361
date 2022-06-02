#STEPHEN OIUM
#CS361
#JOSH GAME CODE
#V1.1
from cryptography.fernet import Fernet
from tkinter import *
import sqlite3
import re
import ctypes
import time
import os
import sys

class Credentials():

	def __init__(self):
		self.__username = ""
		self.__key = ""
		self.__password = ""
		self.__key_file = 'key.key'
		self.__time_of_exp = -1

#----------------------------------------
# Getter setter for attributes
#----------------------------------------

	@property
	def username(self):
		return self.__username

	@username.setter
	def username(self,username):
		while (username == ''):
			username = input('Enter a proper User name, blank is not accepted:')
		self.__username = username

	@property
	def password(self):
		return self.__password

	@password.setter
	def password(self,password):
		self.__key = Fernet.generate_key()
		f = Fernet(self.__key)
		self.__password = f.encrypt(password.encode()).decode()
		del f

	@property
	def expiry_time(self):
		return self.__time_of_exp

	@expiry_time.setter
	def expiry_time(self,exp_time):
		if(exp_time >= 2):
			self.__time_of_exp = exp_time


	def create_cred(self):
		"""
		This function is responsible for encrypting the password and create key file for
		storing the key and create a credential file with user name and password
		"""

		cred_filename = 'CredFile.ini'

		with open(cred_filename,'w') as file_in:
			file_in.write("#Credential file:\nUsername={}\nPassword={}\nExpiry={}\n"
			.format(self.__username,self.__password,self.__time_of_exp))
			file_in.write("++"*20)


		#If there exists an older key file, This will remove it.
		if(os.path.exists(self.__key_file)):
			os.remove(self.__key_file)

		#Open the Key.key file and place the key in it.
		#The key file is hidden.
		try:

			os_type = sys.platform
			if (os_type == 'linux'):
				self.__key_file = '.' + self.__key_file

			with open(self.__key_file,'w') as key_in:
				key_in.write(self.__key.decode())
				#Hidding the key file.
				#The below code snippet finds out which current os the script is running on and does the task base on it.
				if(os_type == 'win32'):
					ctypes.windll.kernel32.SetFileAttributesW(self.__key_file, 2)
				else:
					pass

		except PermissionError:
			os.remove(self.__key_file)
			print("A Permission error occurred.\n Please re run the script")
			sys.exit()

		self.__username = ""
		self.__password = ""
		self.__key = ""
		self.__key_file


root = Tk()
root.title("The Game Library")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
 
#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)
 
#==============================LABELS=========================================
lbl_title = Label(Top, text = "The Game Library, font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)
 
#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)
 
#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)

#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
        conn.commit()

#=====================MAIN==============================================

def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()
 
def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Python: Simple Login Application")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)
 
def Back():
    Home.destroy()
    root.deiconify()

# Creating an object for Credentials class
	creds = Credentials()

	#Accepting credentials
	creds.username = input("Enter UserName:")
	creds.password = input("Enter Password:")
	print("Enter the epiry time for key file in minutes, [default:Will never expire]")
	creds.expiry_time = int(input("Enter time:") or '-1')

	#calling the Credit
	creds.create_cred()
	print("**"*20)
	print("Cred file created successfully at {}"
	.format(time.ctime()))

	if not(creds.expiry_time == -1):
		os.startfile('expire.py')


	print("**"*20)
#===========================================RUN======================
if __name__ == '__main__':
    root.mainloop()
