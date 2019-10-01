# Create Class called Pet
class Pet():

    def __init__(self, name, breed, owner_f_name, owner_l_name):
        self.name = name
        self.breed = breed
        self.owner_f_name = owner_f_name
        self.owner_l_name = owner_l_name


    # def add_pet_to_list(self, pets):
    #     if self.list_of_pets.append((pets)):
    #         return True
    #     else:
    #         return  False

    def pet_details(self):
        pet_details = \
            {
            "Pet Name": self.name,
            "Breed": self.breed,
            "Owner Name": self.owner_f_name + " " + self.owner_l_name,

        }
        return pet_details