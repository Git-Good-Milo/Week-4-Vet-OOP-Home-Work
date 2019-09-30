# Create class for Veternarian
# Import all from Human Class
from human_class import *

class Veternarian(Human):
    def __init__(self, f_name, l_name, phone, email, specilisation):
        super().__init__(f_name, l_name,  phone, email)
        self.name = f_name
        self.name = l_name
        self.phone = phone
        self.email = email
        self.specilisation = specilisation
        self.list_of_vets = []

    def add_vets_to_list(self, vets):
        if self.list_of_vets.append(vets):
            return True
        else:
            return False


