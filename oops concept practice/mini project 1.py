# create a library class
# display book
# lended book {dictionary of book name and his owner}
# added book
# returned book

all_books = []
lended_books = {}

class Library:
    def __init__(self, library_name, book_detail):
        self.library_name = library_name
        self.book_detail = book_detail
    
    def add_book(self):
        book_name = input('Write the book name.Which you want to add:\n')
        all_books.append(book_name)
        print("Thanks for adding books")

    def return_book(self):
        re_book = input("Name the book, Which you want to return:\n")
        all_books.append(re_book)
        print("Thanks for returning the book")
    
    def lend_book(self):
        print('lend book')
        book_own = input('Enter your name:\n')
        book_name = input('Enter the book name:\n')
        lended_books.update({book_name:book_own})
        print(lended_books)
        if book_name in all_books:
            all_books.remove(book_name)


    def display_book(self):
        for i in all_books:
            print(i)

rohan = Library('Universal Library', 'available books')

print('Select action from below\nWrite the number against each action to perform the action:')

print("1. Add or Donate Book")
print("2. Return Book")
print("3. Lend Book")
print("4. Display All Available Books")
print("5. Exit")

while True:
    user_input = int(input("Enter Action Number:\n"))
    if user_input == 1:
        rohan.add_book()
    if user_input == 2:
        rohan.return_book()
    if user_input == 3 :
        rohan.lend_book()
    if user_input == 4:
        rohan.display_book()
    if user_input==5:
        break