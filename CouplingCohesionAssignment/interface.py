import classExample as cl

'''
This example allows you to make multiple exams and allows you to have multiple professors with multiple exams with multiple students subscribing to that professor.
'''


questions = ["what is a goose?"]
answers = ["it's a goose"]

Alex = cl.professor() # This just in a new professor came in
Exam1 = cl.Exam(questions, answers)

Alex.newExam(Exam1)
Alex.setFlag() #Dr.Alex set the flag for the exam to be viewed   

Travis = cl.Student() # This just in a wild Student appeared 

Travis.subscribe(Alex) #Travis is now a student of Alex
Alex.notifySubscribedStudents(Travis) #notified student that it can be viewed
Travis.retrieveFromProfessor() # retrieve the exam
Travis.sendAnswers(answers) #send the answers over
Alex.gradeExam() #alex grades the exam
Travis.getGrade() #Travis gets the grade

