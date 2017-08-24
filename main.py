import Tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(column=8,rows=8)
        self.createWidgets()
	self.optionA = tk.StringVar()

    def createWidgets(self):
	#Creating the buttons
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.nextButton = tk.Button(self, text='Next')

	#Creating Radio buttons for options
	self.radioButtonA = tk.Radiobutton(self)
	self.radioButtonB = tk.Radiobutton(self)
	self.radioButtonC = tk.Radiobutton(self)
	self.radioButtonD = tk.Radiobutton(self)
	
	#Creating the labels for options and questions
	self.optionA='Hello A!'
        self.label_optionA = tk.Label(text=self.optionA)

	#Packing the widgets in the grid
        self.radioButtonA.grid(column=2,row=4)
	self.label_optionA.grid(column=3,row=4)
	print self.label_optionA.grid_info()
        self.radioButtonB.grid(column=5,row=4)
        self.radioButtonC.grid(column=2,row=6)
        self.radioButtonD.grid(column=5,row=6)
        self.quitButton.grid(column=4,row=8)
	self.nextButton.grid(column=3,row=8)

    def test(self):
        self.nextButton.grid(column=3,row=1)

app = Application()
app.master.title('Sample Application')
app.mainloop()
