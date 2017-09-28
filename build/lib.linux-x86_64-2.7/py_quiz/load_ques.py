import json
import random

with open('questions.json') as file:
    ques = json.load(file)

def load_ques():
    data  =ques["results"]
    aux = range(len(data))
    while aux:
        posit = random.randrange(len(aux))
        index = aux[posit]
        elem = data[index]
        del aux[posit]
        print ".Question:",data["question"]
        print "Correct  Options: ",data["correct_answer"]
        for i in (data["incorrect_answers"]):
            print "Incorrect: ", i
        print("\n")

#print data
