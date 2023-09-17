from integrations import BookManagement, BorrowingTransactionsManagement, PatronsManagement


def add_book():
    """
    Add a book to the library
    """
    print('Please enter the following information:')
    # title = input('Title: ')
    # author = input('Author: ')
    # isbn = input('ISBN: ')
    # quantity = input('Quantity: ')
    # patrons = input('Patrons: ').split(',')

    # Test data
    title = "The Alchemist"
    author = "Paulo Coelho"
    isbn = "978-0062315007"
    quantity = 10
    patrons = ["test", "test2"]

    book = BookManagement(title, author, isbn, quantity, patrons)
    book.save()

def update_book():
    """
    Update a book in the library
    """
    print('Please enter the following information:')
    # isbn = input('ISBN: ')
    # title = input('Title: ')
    # author = input('Author: ')
    # quantity = input('Quantity: ')
    # patrons = input('Patrons: ').split(',')

    # Test data
    title = "The Alchemist"
    author = "Paulo Coelho"
    isbn = "978-0062315007"
    quantity = 9
    patrons = ["Sonic2", "Sonic1"]

    if isbn:
        book = BookManagement(title, author, isbn, quantity, patrons)
        book.update()
    else:
        print('ISBN is required')


def delete_book():
    """
    Delete a book from the library
    """
    print('Please enter the following information:')
    # isbn = input('ISBN: ')
    isbn = "978-0062315007"

    if isbn:
        book = BookManagement('', '', isbn, '', '')
        book.delete()
    else:
        print('ISBN is required')

def add_patron():
    """
    Add a patron to the library
    """
    print('Please enter the following information:')
    # name = input('Name: ')
    # email = input('Email: ')
    # phone_number = input('Phone Number: ')
    # address = input('Address: ')
    name = "Sonic"
    email = "sonic@sonic.com"
    phone_number = "1234567890"
    address = "1234 Main St"

    patron = PatronsManagement(name, email, phone_number, address)
    patron.save()

def update_patron():
    """
    Update a patron in the library
    """
    print('Please enter the following information:')
    # email = input('Email: ')
    # name = input('Name: ')
    # phone_number = input('Phone Number: ')
    # address = input('Address: ')
    email = "sonic@sonic.com"
    name = "Shams"
    phone_number = "1234567890"
    address = "1234 Main St"

    if email:
        patron = PatronsManagement(name, email, phone_number, address)
        patron.update()
    else:
        print('Email is required')

def delete_patron():
    """
    Delete a patron from the library
    """
    print('Please enter the following information:')
    # email = input('Email: ')
    email = "sonic@sonic.com"

    if email:
        patron = PatronsManagement('', email, '', '')
        patron.delete()
    else:
        print('Email is required')


def borrow_book():
    """
    Borrow a book from the library
    """
    pass

def return_book():
    """
    Return a book to the library
    """
    pass

def search_book():
    """
    Search for a book in the library
    """
    pass

def exit():
    """
    Exit the program
    """
    pass


def main():
    print('Welcome to the Library Management System')
    print('Please select what you want to do:')
    print('1. Add a book')
    print('2. Update a book')
    print('3. Delete a book')
    print('4. Add a patron')
    print('5. Update a patron')
    print('6. Delete a patron')
    print('7. Borrow a book')
    print('8. Return a book')
    print('0. Search for a book')
    print('9. Exit')

    choice = input('Enter your choice: ')
    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        add_patron()
    elif choice == '5':
        update_patron()
    elif choice == '6':
        delete_patron()
    elif choice == '7':
        borrow_book()
    elif choice == '8':
        return_book()
    elif choice == '0':
        search_book()
    elif choice == '9':
        exit()
    else:
        print('Invalid choice')
    

if __name__ == '__main__':
    main()