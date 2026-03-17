class Library:
    def __init__(self):
        self.books = []

    def add_book(self, b):
        self.books.append(b)

    def show_books(self):
        print("Books:", self.books)

    def lend_book(self, b):
        if b in self.books:
            self.books.remove(b)
            print("Book issued")
        else:
            print("Not available")

    def return_book(self, b):
        self.books.append(b)
        print("Book returned")


lib = Library()

while True:
    print("\n1.Add 2.Show 3.Lend 4.Return 5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        b = input("Book name: ")
        lib.add_book(b)

    elif ch == 2:
        lib.show_books()

    elif ch == 3:
        b = input("Book name: ")
        lib.lend_book(b)

    elif ch == 4:
        b = input("Book name: ")
        lib.return_book(b)

    elif ch == 5:
        break