# Create class called client/pet owner
# Import from Human class
from human_class import *

class Client_Pet_owner(Human):
    def __init__(self, f_name, l_name, phone, email, payment, pet_name):
        super().__init__(f_name, l_name, phone, email)
        self.payment_details = payment
        self.pet_name = pet_name

# Payment Details
    def make_payments(self, payment_made):
        if payment_made == 'yes':
            return ("Payment made")

    def client_list_of_pets(self):
        client_list_of_pets = \
            {
            "Name": self.f_name + " " + self.l_name,
            "Phone": self.phone,
            "Email": self.email,
            "Payment": self.payment_details,
            "Pet Name": self.pet_name
        }
        return client_list_of_pets