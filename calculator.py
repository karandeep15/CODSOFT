# importing Tkinter and math
from tkinter import *
import tkinter as tk
import math

# creating a class calculator
class calc:

	def getandreplace(self):

		# this is for replacing x for * and / for divide
		self.expression = self.e.get()
		self.newtext=self.expression.replace('/','/')
		self.newtext=self.newtext.replace('x','*')


	def equals(self):
		self.getandreplace()
		try:
			# evaluate the expression using the eval function
			self.value= eval(self.newtext) 
		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.e.delete(0,END)
			self.e.insert(0,self.value)

	def squareroot(self):
		self.getandreplace()
		try:
			# evaluate the expression using the eval function
			self.value= eval(self.newtext) 
		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.sqrtval=math.sqrt(self.value)
			self.e.delete(0,END)
			self.e.insert(0,self.sqrtval)

	def square(self):
		self.getandreplace()
		try:
			#evaluate the expression using the eval function
			self.value= eval(self.newtext) 
		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.sqval=math.pow(self.value,2)
			self.e.delete(0,END)
			self.e.insert(0,self.sqval)

	def clearall(self):
			self.e.delete(0,END)

	def clear1(self):
			self.txt=self.e.get()[:-1]
			self.e.delete(0,END)
			self.e.insert(0,self.txt)

	def action(self,argi):
			self.e.insert(END,argi)


	def __init__(self,master):
			master.title('Python Calculator Task 2')
			master.geometry()
			Label(master, text="Simple Calculator", font="Arial")	
			self.e = Entry(master)
			self.e.grid(row=0,column=0,columnspan=7,pady=6)
			self.e.focus_set() 

			# Generating Buttons
			Button(master,text="=",width=17,height=4,fg="black",
				bg="light blue",command=lambda:self.equals(), font="Arial").grid(
									row=4, column=4,columnspan=2)

			Button(master,text='AC',width=8,height=4,
						fg="black", bg="light blue",
			command=lambda:self.clearall(), font="Arial").grid(row=1, column=4)

			Button(master,text='C',width=8,height=4,
				fg="black",bg="light blue",
				command=lambda:self.clear1(),font="Arial").grid(row=1, column=5)

			Button(master,text="+",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action('+'), font="Arial").grid(row=4, column=3)

			Button(master,text="X",width=8,height=4,
					fg="black",bg="light green",
					command=lambda:self.action('x'), font="Arial").grid(row=2, column=3)

			Button(master,text="_",width=8,height=4,
					fg="black",bg="light green",
					command=lambda:self.action('-'), font="Arial").grid(row=3, column=3)

			Button(master,text="Divide",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action('/'), font="Arial").grid(row=1, column=3)

			Button(master,text="%",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action('%'), font="Arial").grid(row=4, column=2)

			Button(master,text="7",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action(7),font="Arial").grid(row=1, column=0)

			Button(master,text="8",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action(8),font="Arial").grid(row=1, column=1)

			Button(master,text="9",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action(9),font="Arial").grid(row=1, column=2)

			Button(master,text="4",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action(4),font="Arial").grid(row=2, column=0)

			Button(master,text="5",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action(5),font="Arial").grid(row=2, column=1)

			Button(master,text="6",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action(6),font="Arial").grid(row=2, column=2)

			Button(master,text="1",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action(1), font="Arial").grid(row=3, column=0)

			Button(master,text="2",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action(2), font="Arial").grid(row=3, column=1)

			Button(master,text="3",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action(3),font="Arial").grid(row=3, column=2)

			Button(master,text="0",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action(0), font="Arial").grid(row=4, column=0)

			Button(master,text="Decimal",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action('.'),font="Arial").grid(row=4, column=1)

			Button(master,text="(",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action('('),font="Arial").grid(row=2, column=4)

			Button(master,text=")",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.action(')'), font="Arial").grid(row=2, column=5)

			Button(master,text="Root",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.squareroot() ,font="Arial").grid(row=3, column=4)

			Button(master,text="x²",width=8,height=4,
				fg="black",bg="light green",
				command=lambda:self.square(),font="Arial").grid(row=3, column=5)

			

root = tk.Tk()

obj=calc(root)

root.mainloop()

