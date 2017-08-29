import Tkinter as tk
import json
import random

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(column=8,rows=8,sticky=tk.N+tk.S+tk.E+tk.W)
	self.grid_rowconfigure(0,weight=1)
	self.grid_columnconfigure(0,weight=1)
	# declaring variables to store question and answer
        self.optionA = tk.StringVar()
	self.optionB = tk.StringVar()
	self.optionC = tk.StringVar()
	self.optionD = tk.StringVar()
	self.selected_answer = tk.StringVar()
	self.correct_answer = ""
	self.question = tk.StringVar()
	self.score = tk.IntVar()
	self.file = open("questions.json","r")
	self.questions = json.loads(self.file.read())
	self.question_index = []
	self.score=0
        self.createWidgets() # call to create the necessary widgets

    def validate_ans(self):
	print "In Validate answer:"
	print "selected:",str(self.selected_answer.get())
	print "Correct:",self.correct_answer
        if str(self.selected_answer.get()) == (self.correct_answer):
	    self.score=self.score+5
	    print "Correct!"
	

    def load_question(self):
	self.validate_ans()
        randomindex = random.randint(0,len(self.questions["results"])-1)
        #self.question.set('Next Clicked')
        if randomindex not in self.question_index:
	    self.question_index.append(randomindex)
	    pass
	else:
            randomindex = random.randint(0,len(self.questions["results"])-1)
	    self.question_index.append(randomindex)
	print "Debug:"
        print self.questions["results"][randomindex]["question"]
	self.correct_answer = self.questions["results"][randomindex]["correct_answer"]
	print self.correct_answer
	self.answers = self.questions["results"][randomindex]["incorrect_answers"]
	self.answers.append(self.correct_answer)
        self.question.set(self.questions["results"][randomindex]["question"])
	self.optionA.set(self.answers.pop(random.randrange(len(self.answers))))
	self.optionB.set(self.answers.pop(random.randrange(len(self.answers))))
	self.optionC.set(self.answers.pop(random.randrange(len(self.answers))))
	self.optionD.set(self.answers.pop(random.randrange(len(self.answers))))
	
        
    def createWidgets(self):
	top = self.winfo_toplevel()
	top.rowconfigure(0,weight=1)
	top.columnconfigure(0, weight=1)

	self.rowconfigure(0,weight=1)
	self.columnconfigure(0, weight=1)

	self.optionA.set('Hello A!')
	self.optionB.set('Hello B!')
	self.optionC.set('Hello C!')
	self.optionD.set('Hello D!')
#	self.score.set(0)
	self.question.set('Demo Question')

	#Creating the buttons
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.nextButton = tk.Button(self, text='Next', command=self.load_question)

	#Creating Radio buttons for options
	self.radioButtonA = tk.Radiobutton(self,anchor='w',textvariable=self.optionA, variable = self.selected_answer, value = self.optionA)
	self.radioButtonB = tk.Radiobutton(self,anchor='w',textvariable=self.optionB, variable = self.selected_answer, value = self.optionB)
	self.radioButtonC = tk.Radiobutton(self,anchor='w',textvariable=self.optionC, variable = self.selected_answer, value = self.optionC)
	self.radioButtonD = tk.Radiobutton(self,anchor='w',textvariable=self.optionD, variable = self.selected_answer, value = self.optionD)
	
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
app = Application()
app.master.title('PyQuiz!')
app.mainloop()
