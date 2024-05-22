number = [1,2,3,4,5,6,7,8,9,10]
#a sum of all number
def tambah(number):
    return sum(number)
#b max and min of all number
def maks(number):
    return max(number)
def mins(number):
    return min(number)

#c remove duplicates
def removeDuplicate(number):
    return list(set(number))
print(f"the list with duplicates is: {removeDuplicate(number)}")

def removeDuplicate2(number):
  new = []
  for i in number:
    if i not in new:
      new.append(i)
  return new

#d the the position in the given number
def find(number,target):
    for i in range(len(number)):
        if number[i] == target:
            return i

#e reverse the number
def reverse(number):
    return number[::-1]
  
#f find missing number
def findMissing(number):
    return [x for x in range(number[0], number[-1]+1) if x not in number]
  
def findMissing2(number):
    return number - 55 # 55 is the sum of all numbers in the list
  
#g find the sum of all even number
def evenSum(number):
    return sum([x for x in number if x % 2 == 0])
  
#h find the sum of all odd number
def oddSum(number):
    return sum([x for x in number if x % 2 != 0])
  
#================================================

# create a class Book with attributes title and author
class Book(object):
  """Class Book"""
  def __init__(self, title, author):
    self.title = title
    self.author = author

# create a class Library with attributes books
class Library(object):
  """Class Library"""
  def __init__(self):
    self.books = []
  
  # add a book to the library
  def addBook(self, book):
    self.books.append(book)
    
  # remove a book from the library
  def removeBook(self, title):
    for book in self.books:
      if book.title == title:
        self.books.remove(book)
        break
        
  # show all books in the library
  def showBooks(self):
    if self.books:
      print("book title | book author")
      for book in self.books:
        print(f"{book.title} | {book.author}")
  
  # search for a book by author
  def searchBook(self, author):
    for book in self.books:
      if book.author == author:
        print(f"{book.title} by {book.author}")
        
# library Demo
perpus = Library()
b1 = Book("Harry Potter", "J.K. Rowling")
b2 = Book("The Hobbit", "J.R.R. Tolkien")
b3 = Book("The Da Vinci Code", "Dan Brown")

perpus.addBook(b1)
perpus.addBook(b2)
perpus.addBook(b3)

perpus.showBooks()
perpus.searchBook("J.R.R. Tolkien")
perpus.removeBook("The Hobbit")
perpus.showBooks()
#================================================
        