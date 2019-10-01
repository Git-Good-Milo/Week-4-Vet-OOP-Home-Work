# Create a class called Appointments

class Appointment():

    def __init__(self, disease, date, time, pet, vet ):
        self.disease = disease
        self.date = date
        self.appointment_time = time
        self.pet = pet
        self.vet = vet
        self.list_of_pets = []


    def add_pet_to_list(self, pets):
        if self.list_of_pets.append(pets):
            return True
        else:
            return  False

    def pet_details(self):
        pet_details = {
            "Pet Name": self.pet.name,
            "Disease or Issue": self.disease,
            "Date": self.date,
            "Appointment Time": self.appointment_time,
            "Vet": self.vet.name,
            "List of Pets": self.list_of_pets

        }
        return pet_details

