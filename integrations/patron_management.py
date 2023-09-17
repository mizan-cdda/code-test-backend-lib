import json
from data_models.patrons import Patrons
from utils.data_validation import Validation


class PatronsManagement(Patrons):
    """
    Update Patrons Object as needed
    """
    def __init__(self, name, email, phone_number, address):
        super().__init__(name, email, phone_number, address)

        self.validation = Validation()

    def filed_validation(self):
        """
        Validate fields
        """
        try:
            self.validation.validate_non_empty_string(self.name)
            self.validation.validate_non_empty_string(self.email)
            self.validation.validate_non_empty_string(self.phone_number)
            self.validation.validate_non_empty_string(self.address)
            return True
        except ValueError as e:
            print(e)
            return False
    
    def make_json(self):
        """
        Make json from patrons object
        """
        dictionary  =  {
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'address': self.address
        }

        return dictionary
    
    def get_patron_by_email(self, email):
        """
        Get patron by email
        """
        with open('data/data_patrons.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for patron in data:
                if patron['email'] == email:
                    return patron
                
    def save_to_file(self, update=False):
        """
        Save patron to file
        """
        with open('data/data_patrons.json', 'r+', encoding='utf-8') as file:
            try:
                try:
                    data = json.load(file)
                    file.seek(0) # rewind
                except json.decoder.JSONDecodeError:
                    print('File is empty')
                    data = []
                if update:
                    for patron in data:
                        if patron['email'] == self.email:
                            patron['name'] = self.name
                            patron['phone_number'] = self.phone_number
                            patron['address'] = self.address
                            file.seek(0)
                            json_data = json.dump(data, file, indent=4)
                            
                            file.truncate()
                            # file.write(json_data)
                            return True
                else:
                    print('Saving patron')
                    print(data)
                    data.append(self.make_json())
                    print(data)
                    file.seek(0)
                    json_data = json.dump(data, file, indent=4)
                    print(json_data)
                    file.truncate()

                    # file.write(json_data)
                    file.close()
                    return True
            except Exception as e:
                print(e)
                return False
    
    def save(self):
        """
        Save patron
        """
        if self.filed_validation():
            if self.save_to_file():
                print('Patron saved')
            else:
                print('Patron not saved')
        else:
            print('Patron not saved')
    
    def update(self):
        """
        Update patron
        """
        if self.filed_validation():
            if self.save_to_file(update=True):
                print('Patron updated')
            else:
                print('Patron not updated')
        else:
            print('Patron not updated')
    