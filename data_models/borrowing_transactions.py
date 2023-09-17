class BorrowingTransactions:
    def __init__(self, book, quantity, dew_date, return_date):
        self.book = book
        self.quantity = quantity
        self.dew_date = dew_date
        self.return_date = return_date

    def __repr__(self):
        return f"<Book {self.book}"
    
    def get_book(self):
        return self.book
    
    def get_dew_date(self):
        return self.dew_date
    
    def get_return_date(self):
        return self.return_date
    
    def set_book(self, book):
        self.book = book

    def set_dew_date(self, dew_date):
        self.dew_date = dew_date
    
    def set_return_date(self, return_date):
        self.return_date = return_date
    
    def remove_book(self, book):
        self.book.remove(book)
        