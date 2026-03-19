password ="admin"
if password=="admin":
    new_password=input("enter the new password\n")
else:
    print("invalid password,please check your password")
#log in
log_in=input("enter the new password\n")
if log_in==new_password:
    print("log in is successful")
else:
    print("invalid log in,check your password")

class student:
    def __init__(self,name,D_O_B,course,reg_no,borrowed_books):
        self.name=name
        self.D_O_B=D_O_B
        self.course=course
        self.reg_no=reg_no
        self.borrowed_books=borrowed_books

class book:
    def __init__(self,ISBN_no,author,year,title,serial_no,number_of_copies,available_copies):
        self.ISBN_no=ISBN_no
        self.author=author
        self.year=year
        self.title=title
        self.serial_no=serial_no
        self.number_of_copies=number_of_copies
        self.available_copies=available_copies

    students=[]
    def add_student(self):
        def __init__(self,name,D_O_B,course,reg_no,borrowed_books):
            super.__init__(self,name,D_O_B,course,reg_no,borrowed_books)
        if student not in students:
            return students.append(student)
        else:
             print("name already exists")
    
    books=[]
    def add_book(self):
        def __init__(self,ISBN_no,author,year,title,serial_no,number_of_copies,available_copies):
            super.__init__(self,ISBN_no,author,year,title,serial_no,number_of_copies,available_copies)
        if book not in books:
            return books.append(book)
        else:
            print("book already exists")

    def rent_book(self):
        def __init__(self,student_no,ISBN_no,serial_no):
            super.__init__(self,ISBN_no,serial_no)
            self.student_no=student_no
        if available_copies==0:
           print("not allowed to rent out a book")
        else:
            print("rent out the book")

    def print_details(self):
        def __init__(self,ISBN_no,serial_no):
            super.__init__(self,ISBN_no,serial_no)
            
    
    
    


            