class Student:
    def __init__(self,student_ID,name,course,year_of_study,):
        self.student_ID=student_ID
        self.name=name
        self.course=course
        self.year_of_study=year_of_study
        self.marks=[]
        self.subjects=[]

    def display_student_information(self):
        print(f"name:{self.name}")
        print(f"student_ID:{self.student_ID}")
        print(f"course:{self.course}")
        print(f"year_of_study:{self.year_of_study}")
        print(f"marks:{self.marks}")
        print(f"subjects:{self.subjects}")

    def add_marks(self,subject,marks):
        if marks<0 and marks >100:
            print("invalid marks! must be between 0 and 100")
        self.marks.append(marks)
        self.subjects.append(subject)
        
        if marks<40 and marks>0:
            print("F.9") 
        elif marks<50 and marks>40:
            print("P.7")
        elif marks<60 and marks>50:
            print("c.4")
        elif marks<70 and marks>60:
            print("C.3")
        elif marks<80 and marks>70:
            print("D.2")
        elif marks<90 and marks>80:
            print("good D.1")
        elif marks<100 and marks>90:
            print("excellent D.1")

    def calculate_results(student,marks):
        total=sum(marks)
        average=total/len(marks)
        print(average)
Student1=Student("s001","Angella","computer science",2)
Student1.add_marks("Mathematics",75)
Student1.add_marks("programming",88)
Student1.display_student_information()
    


        