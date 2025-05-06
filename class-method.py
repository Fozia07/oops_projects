#Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_book=0

    @classmethod
    def increment_book_count(cls):
        cls.total_book += 1

    def __init__(self,tittle,authorname):
      self.title=tittle
      self.authorname=authorname

      Book.increment_book_count()

book1=Book("The Great Gatsby","F.scott fitzgerald")
book2=Book("1984","Gorge Orwell")      

print(f"the total book count is : {Book.total_book}")