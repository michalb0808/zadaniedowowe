class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class BookCopy:
    def __init__(self, book, year):
        self.book = book
        self.year = year


class Library:
    presentBooks = {}
    presentCopies = []

    def add_book_copy(self, title, author, year):

        if title not in list(self.presentBooks.keys()):
            self.presentBooks[title] = Book(title, author)

        self.presentCopies.append(BookCopy(self.presentBooks[title], year))

    def display_books_info(self):
        tuples_to_display = []

        for title, book in self.presentBooks.items():
            counter = 0
            for item in self.presentCopies:
                if item.book.title == title:
                    counter += 1

            tuples_to_display.append((book.title, book.author, counter))

        tuples_to_display.sort(key=lambda tup: tup[0])

        for bookInfo in tuples_to_display:
            print(bookInfo)


library = Library()
inputNumber = int(input())

for i in range(0, inputNumber):
    tempBookInfo = eval(input())
    library.add_book_copy(tempBookInfo[0], tempBookInfo[1], tempBookInfo[2])

library.display_books_info()



