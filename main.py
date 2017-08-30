import Tkinter as tk
import json
import random

class Application(tk.Frame):

    def __init__(self, master=None):
	'''
	Call to the constructor when the object is created.
	Variables initialized and set the grid as per need.
	'''
        tk.Frame.__init__(self, master)
        self.grid(column=8,rows=8,sticky=tk.N+tk.S+tk.E+tk.W)
	self.grid_rowconfigure(0,weight=1)
	self.grid_columnconfigure(0,weight=1)
	# declaring variables to store question and answer
        self.optionA = tk.StringVar() # control variable for option A
	self.optionB = tk.StringVar() # control variable for option B
	self.optionC = tk.StringVar() # control variable for option C
	self.optionD = tk.StringVar() # control variable for option D
	self.selected_answer = tk.StringVar() # variable to get the selected answer
	self.correct_answer = "" # to store the correct answer before randomizing options
	self.question = tk.StringVar() # control variable for the question to be loaded
	self.file = open("questions.json","r")
	self.questions = json.loads(self.file.read())
	self.question_index = []
	self.score = tk.IntVar() # to hold the score 
        self.createWidgets() # call to create the necessary widgets
	self.load_question() # load the first question

    def set_ans(self,answer):
	'''
	Function to set the 'selected_answer' variable to the selected option label to compare with correct answer later.
	Args: answer - gets the option number which calls this function.
	'''
	if answer==1:
	    self.selected_answer = self.optionA.get()
	elif answer==2:
	    self.selected_answer = self.optionB.get()
	elif answer == 3:
	    self.selected_answer = self.optionC.get()
	elif answer == 4:
	    self.selected_answer = self.optionD.get()

    def validate_ans(self):
	'''
	Function to validate the selected answer with the correct answer. If they match, increase the score by 5.
	'''
	print "In Validate answer:"
	print "selected:",self.selected_answer
	print "Correct:",self.correct_answer
	self.py_var = ["PY_VAR1","PY_VAR2","PY_VAR3","PY_VAR4"]
        if (self.selected_answer) == (self.correct_answer):
	    self.score.set(int(self.score.get()) + 5)
	    print "Correct!"
	elif str(self.selected_answer) in self.py_var :
	    print "IN py var if"
	    pass
	else:
	    self.score.set(int(self.score.get()) - 5)
	    print "Correct!"
	   
	

    def load_question(self):
	'''
	Function to load a new question set with options. The question is randomly picked from the JSON file for questions.
	The options to that questions are also randomized and loaded.
	'''
	self.validate_ans() # call to check the answer before loading the next question
        randomindex = random.randint(0,len(self.questions["results"])-1) # generate random index to be picked from list
        if randomindex not in self.question_index: # only proceed if the question has not already been picked up.
	    self.question_index.append(randomindex) # keep a track of the question indices.
	    pass
	else:
            randomindex = random.randint(0,len(self.questions["results"])-1)
	    self.question_index.append(randomindex)
	print "Debug:"
        print self.questions["results"][randomindex]["question"] 
	self.correct_answer = self.questions["results"][randomindex]["correct_answer"] # parse the correct answer from JSON file and store it.
	print self.correct_answer
	self.answers = self.questions["results"][randomindex]["incorrect_answers"] # parse the other incorrect answers
	self.answers.append(self.correct_answer) # add all the answers to the list. 
        self.question.set(self.questions["results"][randomindex]["question"]) # set the question label
	self.optionA.set(self.answers.pop(random.randrange(len(self.answers)))) # randomly set the option label from the answers list and then remove from that list to avoid repetition
	self.optionB.set(self.answers.pop(random.randrange(len(self.answers))))
	self.optionC.set(self.answers.pop(random.randrange(len(self.answers))))
	self.optionD.set(self.answers.pop(random.randrange(len(self.answers))))
	
        
    def createWidgets(self):
	'''
	Function that creates all the necessary Tkinter widgets. All the widgets are specified here while creation.
	'''
	top = self.winfo_toplevel()
	top.rowconfigure(0,weight=1)
	top.columnconfigure(0, weight=1)

	self.rowconfigure(0,weight=1)
	self.columnconfigure(0, weight=1)

	self.optionA.set('Hello A!')
	self.optionB.set('Hello B!')
	self.optionC.set('Hello C!')
	self.optionD.set('Hello D!')
	self.question.set('Demo Question')

	#Creating the buttons
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.nextButton = tk.Button(self, text='Next', command=self.load_question)

	#Creating Radio buttons for options
	self.radioButtonA = tk.Radiobutton(self,anchor='w',textvariable=self.optionA, variable = self.selected_answer, value = 'A',command = lambda: self.set_ans(1)) # the radio button call 'set_ans()' with the number to set the 'selected_answer' variable
	self.radioButtonB = tk.Radiobutton(self,anchor='w',textvariable=self.optionB, variable = self.selected_answer, value = 'B', command = lambda: self.set_ans(2))
	self.radioButtonC = tk.Radiobutton(self,anchor='w',textvariable=self.optionC, variable = self.selected_answer, value = 'C', command = lambda: self.set_ans(3))
	self.radioButtonD = tk.Radiobutton(self,anchor='w',textvariable=self.optionD, variable = self.selected_answer, value = 'D', command = lambda: self.set_ans(4))
	
	#Creating the labels for options and questions
	self.label_question = tk.Label(self,textvariable=self.question)
	self.label_score = tk.Label(self,text='Score:')
	self.label_score_value = tk.Label(self,textvariable=self.score,anchor='e')

	#Packing the widgets in the grid
	self.label_question.grid(column=3,row=1,columnspan=4,sticky=tk.N+tk.S+tk.E+tk.W)

	self.label_score.grid(column=7,row=3,sticky=tk.N+tk.S+tk.E+tk.W)
	self.label_score_value.grid(column=8,row=3,sticky=tk.N+tk.S+tk.E+tk.W)
        
	self.radioButtonA.grid(column=2,row=4,sticky=tk.N+tk.S+tk.E+tk.W)
        self.radioButtonB.grid(column=5,row=4,sticky=tk.N+tk.S+tk.E+tk.W)
        self.radioButtonC.grid(column=2,row=6,sticky=tk.N+tk.S+tk.E+tk.W)
        self.radioButtonD.grid(column=5,row=6,sticky=tk.N+tk.S+tk.E+tk.W)
        
	self.quitButton.grid(column=4,row=8,sticky=tk.N+tk.S+tk.E+tk.W)
	self.nextButton.grid(column=3,row=8,sticky=tk.N+tk.S+tk.E+tk.W)

    def test(self):
        self.nextButton.grid(column=3,row=1)

        

def SplashScreen():
    root = tk.Tk()
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d'%(width*0.8,height*0.8,width*0.1,height*0.1))

    image_file = 'test.gif'
    image = tk.PhotoImage(file=image_file)
    canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="brown")
    canvas.create_image(width*0.8/2, height*0.8/2, image=image)
    canvas.grid()
# show the splash screen for 5000 milliseconds then destroy
    root.after(5000, root.destroy)


#SplashScreen()
app = Application() # creating the object for Application class()
app.master.title('PyQuiz!')
app.mainloop()
