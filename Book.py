class Book:
    def __init__(self, book_id, name, author, count):
        self._book_id = book_id
        self.name = name
        self.author = author
        self.count = count

    def print_info(self):
        count = self.count
        count_msg = ""
        if count > 0:
            count_msg = f"There {"is" if count == 1 else "are"} {self.count} {"copy" if count == 1 else "copies"} available for checkout."
        else:
            count_msg = "There are no copies of this book available to checkout."

        print(f"\n{self.name} by {self.author}")
        print(count_msg)


b1 = Book(1, "The Hobbit", "J.R.R Tolkien", 2)
b2 = Book(2, "The Lord of the Rings", "J.R.R Tolkien", 1)
b1.print_info()
b2.print_info()
