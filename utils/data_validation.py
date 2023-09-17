import datetime

class Validation:
    
    @staticmethod
    def isValidISBN(isbn):
  
    # check for length
        if len(isbn) <= 10:
            return False
        else:
            return True
    @staticmethod
    def validate_non_empty_string(value):
        if not value:
            raise ValueError("Value cannot be empty or None")
        
    @staticmethod
    def validate_date(date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    
