class Books:
    def __init__(self, title, author, isbn, quantity, patrons):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
        self.patrons = patrons


    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"
    
    def get_patrons(self):
        return self.patrons
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_quantity(self):
        return self.quantity
    
    def get_ISBN(self):
        return self.isbn
    
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author
        
    def set_quantity(self, quantity):
        self.quantity = quantity
    
    def set_patrons(self, patrons):
        self.patrons = patrons
    
    def set_isbn(self, isbn):
        self.isbn = isbn

    def add_patron(self, patron):
        self.patrons.append(patron)
    
    def get_patron_count(self):
        return len(self.patrons)
    