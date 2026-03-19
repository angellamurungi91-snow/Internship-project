password="admin"
login = input("enter password")
if login==password:
    new_password = input("enter the new password")
    print(new_password)
else:
    print("entered invalid password please check your password")
    
class student:
    def __init__(self,name,date_of_birth,course,reg_number,borrowed_books):
        self.name = name
        self.date_of_birth = date_of_birth
        self.course = course
        self.reg_number = reg_number
        self.borrowed_books = []
        
    def print_details(self):
        print(f"name:{self.name}")
        print(f"date_of_birth:{self.date_of_birth}")
        print(f"course:{self.course}")
        print(f"reg_number:{self.reg_number}")
        
    def add_student(self):
        if student in students:
            print("this student already exists")
        else:
            student=input("enter the student name")
            students.append(student)
            return students
        
class books:
    def __init__(self,ISBN_number,author,year,title,serial_number,number_of_copies,available_copies):
        self.ISBN_number = ISBN_number
        self.author = author
        self.year = year
        self.title = title
        self.serial_number = serial_number
        self.number_of_copies = number_of_copies
        self.available_copies = available_copies
        
    def add_book(self):
        if book in books:
            print("this book already exists")
        else:
            book=input("enter the book to be added")
            books.append(book)
            return books
            
    def rent_book(self):
        if available_copies==0:
            print("not allowed to rent out a book")
            if borrowed_books>3:
                print("not allowed to borrow a book")
            else:
                print("allowed to borrow a book")
        else:
            print("allowed to rent a book")
               
                
            
        