# Create a class called Appointments

class Appointment():

    def __init__(self, disease, date,time, pet, vet ):
        self.disease = disease
        self.date = date
        self.appointment_time = time
        self.pet = pet,
        self.vet = vet
        self.list_appointments = []
        self.list_of_pets = []

    def add_to_appointments(self, appointment):
        if self.list_appointments.append(appointment):
            return True
        else:
            return False


