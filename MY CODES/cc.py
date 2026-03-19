class Student:
    def __init__(self,id_number,registration_number,student_number,full_name):
        self.id_number=id_number
        self.registration_number=registration_number
        self.student_number=student_number
        self.full_name=full_name
        
    def print_statement(self):
        print(f"name:{self.full_name}")
        print(f"university:{self.university}")
        print(f"college:{self.college}")
        print(f"reg no:{self.registration_number}")
        print(f"student_number:{self.regiatration_number}")
        print(f"id_no:{self.id_number}")
        print(f"total_students:{self.total_students}")
        
class CEDAT_student(Student):
    def __init__(self,id_number,registration_number,student_number,full_name,college,university):                   
        self.college="CEDAT"
        self.university="MAKERERE"
        super().__init__(self,id_number,registration_number,student_number,full_name,college,university)
            
            
class COCIS_student(Student):
    def __init__(self,id_number,registration_number,student_number,full_name,college,university):
        self.college="COCIS"
        self.university="MAKERERE"
        super().__init__(self,id_number,registration_number,student_number,full_name,college,university)
        
        
class EDUC_student(Student):
    def __init__(self,id_number,registration_name,student_name,full_name,college,university):
        self.college="Education college"
        self.university="MAKERERE"
        super().__init__(self,id_number,registration_number,student_name,full_name,college,university)
        
class EASLIS_student(COCIS_student):
    def __init__(self,id_number,registration_number,student_number,full_name,college,university):
        self.college="COCIS-EASLIS"
        self.university="MAKERERE" 
        super().__init__(self,id_number,registration_number,student_number,full_name,college,university)
        
class SCIT_student(COCIS_student):
    def __init__(self,id_number,registration_number,student_number,full_name,college,university):
        self.college="COCIS-SCIT"
        self.university="MAKERERE" 
        super().__init__(self,id_number,registration_number,student_number,full_name,college,university)
        
        
class Cs_student(COCIS_student):
    def __init__(self,full_name,registration_number,student_number):
        super.__init__(self,full_name,registration_number,student_number)
        self.department="Computer science"
        
    def print_statement(self):
        print(f"Name:{self.full_name}")
        print(f"university:{self.university}")
        print(f"college:{self.college}")
        print(f"registration_number:{self.registration_number}")
        print(f"student_number:{self.student_number}")
        print(f"department:{self.department}")
        print(f"id_number:{self.id_number}")
        print(f"total students:{self.total_student}")
        
class SE_student(COCIS_student):
    def __init__(self,full_name,registration_number,student_number):
        super.__init__(self,full_name,registration_number,student_number)
        self.department="Networks"
        
    def print_student(self):
        print(f"Name:{self.full_name}")
        print(f"university:{self.university}")
        print(f"college:{self.college}")
        print(f"registration_number:{self.registration_number}")
        print(f"student_number:{self.student_number}")
        print(f"department:{self.department}")
        print(f"id_number:{self.id_number}")
        print(f"total students:{self.total_student}")
        
s1=Student("KAYIWA JOHN","2020/U/345",2020345)
S2=Student("LUMU MUSA","2020/U/456/EVE",2020456,"SE_student")
S3=Student("ADONGO DIANA","2020/U/789",2020789,"Cs_student")
        
        
        
        
        
        
        
        
      
           
           
        
        
    
    