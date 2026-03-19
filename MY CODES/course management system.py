class Book:
    def __init__(self,title,author,copies):
        self.title=title
        self.author=author
        self.copies=0
        
    def borrow(self,copy):
        if copy in self.copies:
            self.copies-=copy
        else:
            return "no available copy"
            
    def return_book(self,copy):
        self.copies+=copy
        
    def display_info(self):
        print(f"title:{self.title}")
        print(f"author:{self.author}")
        print(f"copies:{self.copies}")
        
class Textbook(Book):
    def __init__(self,title,author,copies,subject):
        super().__init__(title,author,copies)
        self.subject=subject
     
def display_info(self):
        print(f"title:{self.title}")
        print(f"author:{self.author}")
        print(f"copies:{self.copies}")
        print(f"subject:{self.subject}")
        
        
class Novel(Book):
    def __init__(self,title,author,copies,genre):
        super().__init__(title,author,copies)
        self.genre=genre
        
    def display_info(self):
        print(f"title:{self.title}")
        print(f"author:{self.author}")
        print(f"copies:{self.copies}")
        print(f"genre:{self.genre}")
        
class Library:
    def __init__(self):
        self.books=[]
        
    def add_book(self,book):
        self.books.append(book)
     
    def list_books(self,book):
        for book in self.books:
            print(book)
            
    def find_book(self,title):
        for title in self.title:
            if title in self.books:
                return title
            else:
                return None
                
    def borrow_book(self,title):
        if find_book==title:
            return borrow
            print("book_borrowed")
        else:
            print("book unavailable")
            
    def return_book(self,title):
        return return_book
        
t1=Textbook("pride","Blue",3,"literature")
t1.append(self.books)
t2=Textbook("Innovation","Thunder",2,"Biology")
t2.append(self.books)

n1=Novel("Justice","Mun Kai",3,"fantasy")
n1.append(self.books)
n2=Novel("Revenge","Bobo",2,"action")
n2.append(self.books)        
        