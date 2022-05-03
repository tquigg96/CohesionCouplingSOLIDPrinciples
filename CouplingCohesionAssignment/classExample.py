#protected variables labeled as 1 _
#private variables labeled as 2 _
#public variables labeled as 0 _

class Exam:
    _notifyflag = 0 #protected to make it so no student can access it but professor can turn it on or off
   
    def __init__(self, questionArray, _answerArray):
        self._questionArray = questionArray
        self._answerArray = _answerArray
    
    def setupQuestions(self, question): #pretty self explanatory
        self._questionArray.append(question)
        return self._questionArray
    
    def setupAnswers(self, answer):
        self._answerArray.append(answer)
        return self._answerArray

class professor:
    __score = 0 #private variable score no need to initialize cuz it can't be set for student
    __answerNotify = 0 #private member so that students cant grab it
    studentAnswers = []
    #initialized so that I can grab it for student
    def newExam(self,Exam): #professor will be called as a polymorphic call and set to individual students when they call this class and method
        self.__Exam = Exam

    def setQuestions(self):  #only professor can set the questions
        for i in self.__question:
           self.__Exam.setupQuestions(i) #array for question

    def setAnswers(self): #only professor can set the answers 
        for i in self.__answer:
            self.__Exam.setupAnswers(i) #array for answer
    
    def getQuestions(self): #for the student to grab for exam
        return self.__Exam._questionArray

    def getAnswers(self): #student can grab the true answers after they submit the answers
        if self.__answerNotify == 1:
            return self._answerArray
        else:
            print("unauthorized access from student")

    def gradeExam(self): #grabbing the students answers and comparing them to professors answer and setting them
        score = 0
        for i in range(0, len(self.studentAnswers)):
            if(self.studentAnswers[i] == self.__Exam._answerArray[i]):
                score += 1
        self.__score = (score / len(self.studentAnswers))*100
        return self.__score
        
    def getScore(self): #for the student to grab but not set
        return self.__score
    
    def setFlag(self): #option to setflag if exam is ready then notify students it is ready
        self.__Exam._notifyflag = 1 

    def notifySubscribedStudents(self, student):#seperated setFlag and notify so that professor can decide if he is ready to make it visible
        if self.__Exam._notifyflag == 1:
            student.notify = 1
            print("hey your exam is ready!")
        else:
            print("set Notify flag")

    
    def retrieveFromStudent(self, answer): #retieve answers from the student
        for i in range (0, len(answer)):
             self.studentAnswers.append(answer[i])
        self.__answerNotify = 1 #done with exam so student can now get the correct answers
        return self.studentAnswers

class Student:

    notify = 0

    def subscribe(self,professor): #professor will be called as a polymorphic call and set to individual students when they call this class and method
        self.professor = professor

    def retrieveFromProfessor(self): #grab the exam questions when the exam is ready
        if self.notify == 1:
            questions = self.professor.getQuestions()
            print(questions)

    def sendAnswers(self,answers): #plug in the answers and then send it over to professor
        self.professor.retrieveFromStudent(answers)
    
    def getGrade(self):
        grade = self.professor.getScore()
        print(grade)

    
    def retrieveAnswers(self): #retrieve the correct answers but only after the student has finished the exam 
        if self.answerNotify == 1:
            answers = self.professor.getAnswers()
            print(answers)
        else:
            print("unauthorized access")