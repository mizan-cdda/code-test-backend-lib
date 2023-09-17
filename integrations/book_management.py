import json
from data_models.books import Books
from utils.data_validation import Validation


class BookManagement(Books):
    """
    Update Book Object as needed
    """
    def __init__(self, title, author, isbn, quantity, patrons):
        super().__init__(title, author, isbn, quantity, patrons)

        self.validation = Validation()

    def filed_validation(self):
        """
        Validate fields
        """
        try:
            self.validation.validate_non_empty_string(self.title)
            self.validation.validate_non_empty_string(self.author)
            self.validation.validate_non_empty_string(self.isbn)
            self.validation.validate_non_empty_string(self.quantity)
            self.validation.validate_non_empty_string(self.patrons)
            return True
        except ValueError as e:
            print(e)
            return False

    def make_json(self):
        """
        Make json from book object
        """
        dictionary  =  {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'quantity': self.quantity,
            'patrons': self.patrons
        }

        return dictionary
    
    def get_book_by_isbn(self, isbn):
        """
        Get book by isbn
        """
        with open('data/data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for book in data:
                if book['isbn'] == isbn:
                    return book

    def save_to_file(self, update=False):
        """
        Save book to file
        """
        with open('data/data.json', 'r+', encoding='utf-8') as file:
            try:
                data = json.load(file)
                file.seek(0) # rewind
            except json.decoder.JSONDecodeError:
                print('File is empty')
                data = []
            if update:
                print('Updating book')
                data.pop()         
            data.append(self.make_json())

            json_data = json.dumps(data)
            print(json_data)
            file.write(json_data)
            file.close()
        

    def save(self):
        """
        Save book to database
        """
        flag_isbn = False
        check_isbn = self.validation.isValidISBN(self.isbn)
        if check_isbn:
            flag_isbn = True

        if self.filed_validation() and flag_isbn:
            self.save_to_file()
        else:
            print('Invalid book information')

    def update(self):
        """
        Update book in database
        """
        if self.validation.isValidISBN(self.isbn):
            current_book = self.get_book_by_isbn(self.isbn)
            if current_book:
                if self.title:
                    current_book['title'] = self.title
                if self.author:
                    current_book['author'] = self.author
                if self.quantity:
                    current_book['quantity'] = self.quantity
                if self.patrons:
                    current_book['patrons'] = self.patrons
                
                self.set_title(current_book['title'])
                self.set_author(current_book['author'])
                self.set_isbn(current_book['isbn'])
                self.set_quantity(current_book['quantity'])
                self.set_patrons(current_book['patrons'])
                self.save_to_file(update=True)
            else:
                print('Book does not exist')
        else:
            print('Invalid book information')

    def delete(self):
        """
        Delete book from database
        """
        if self.validation.isValidISBN(self.isbn):
            current_book = self.get_book_by_isbn(self.isbn)
            if current_book:
                self.save_to_file(update=True)
            else:
                print('Book does not exist')
        else:
            print('Invalid book information')
