"""Name:Angie Snow
Reg_no:2233
Student_no:22u33"""

class CourseResult:
    def __init__(self,course_code,mark,grade_point):
        self.course_code=course_code
        self.mark=mark
        self.grade_point=grade_point
        
    def grade_point(self):
        if self.mark>80 and self.mark<100:
            return 5.0
        elif self.mark>70 and self.mark<79:
            return 4.0
        elif self.mark>60 and slf.mark<69:
            return 3.0
        elif self.mark>50 and self.mark<59:
            return 2.0
        elif self.mark>0 and self.mark<49:
            return 1.0
        else:
            print("invalid entry")
                
class Student:
    def __init__(self,name,reg_no,student_no):
        self.name=name
        self.reg_no=reg_no
        self.student_no=student_no
        self.results=results
        
    def print_details(self):
        print(f"Name:{self.name}")
        print(f"Reg_no:{self.Reg_no}")
        print(f"student_no:{self.reg_no}")
        print(f"result:{self.result}")
        
    def add_result(course_code,mark):
        for course_code in self.course_code:
        if self.course_code<5:
            self.course_code.add(course_code)
        else:
           print("system allows only 5 course codes")
           
    def compute_CGPA(self):
        total=add(self.grade_point)
        return total/len(self.course_code)
        
    def get_passed_courses(student):
        for course_code in self.course_code:
            if mark>=50:
                return []
            else:
                print("there is no course_code")
                
               
        