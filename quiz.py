import Tkinter as tk
top = tk.Tk()


        
      
      
	optionA = tk.StringVar()
	optionB = tk.StringVar()
	optionC = tk.StringVar()
	optionD = tk.StringVar()
	questin = tk.StringVar()
	optionA.set('Hello A!')

    quitButton = tk.Button(ext='Quit', command=quit)
    nextButton = tk.Button(text='Next')

	
	radioButtonA = tk.Radiobutton(anchor='w',textvariable=.optionA)
	radioButtonB = tk.Radiobutton(anchor='w')
	radioButtonC = tk.Radiobutton()
	radioButtonD = tk.Radiobutton()
	
	#Creating the labels for options and questions
    label_optionA = tk.Label(text=optionA)
    label_optionB = tk.Label(text='Hello B!')
    label_optionC = tk.Label(text='Hello C!')
    label_optionD = tk.Label(text='Hello D!')
	label_question = tk.Label(text='Demo Question')

	#Packing the widgets in the grid
	radioButtonA.grid(column=2,row=4)
	
	
	label_question.grid(column=4,row=1,columnspan=2)
	
    radioButtonB.grid(column=5,row=4)
    radioButtonC.grid(column=2,row=6)
    radioButtonD.grid(column=5,row=6)
    quitButton.grid(column=4,row=8)
	nextButton.grid(column=3,row=8)

    

top.title('Sample Application')
top.mainloop()
