#  need to import from various classes
from client_pet_owner_class import *
from veternarian_class import *
from appointment_class import *
from pet_class import *

# Need to be able to create clients
client1 = Client_Pet_owner("Max", "Speed", "032178998", "max.speed@jmail.com", "Credit Card", "Snuffles")
clent2 = Client_Pet_owner("George", "Best", "459887865", "g.b@coldmail.com", "Cash", "Daisy")


# Need to be able to create pets
pet1 = Pet("Daisy", "Jersey - Cow", "George", "Best")
pet2 = Pet("Steve Jr.", "German Shepard - Dog", "Steve", "Austin")
pet3 = Pet("Snuffles", "Main Coon - Cat", "Max", "Speed")
pet4 = Pet("Baby", "Pit Bull - Dog", "Max", "Speed")
pet5 = Pet("Beelzebub", "Creature Of The Night - Demon", "Mr", "Satan")
pet6 = Pet("Prince", "Golden Eagle - Bird", "George", "Best")

# Need to create Vets
vet1 = Veternarian("Dr", "Dolittle", "032796195", "dr.dolittle@vets.com", "General Practioner")
vet2 = Veternarian("Dr", "Frankenstien", "0000000009", "dr.frankenstien@vets.com", "Surgen")

appointment1 = Appointment("Common Ailments", "01/10/2019", "8-11am", pet1, vet1)
appointment2 = Appointment("Common Ailments", "03/10/2019", "2:00pm-4:00pm", pet3, vet1)
appointment3 = Appointment("Serious Ailment: Surgery Required", "03/10/2019", "8:00am - 12:00pm", pet5, vet2)

# Keep a list of Appointments
appointment_list = []
appointment_list.append(appointment1)
appointment_list.append(appointment2)
appointment_list.append(appointment3)

# keep a list of pets
appointment1.add_pet_to_list(pet2)
appointment1.add_pet_to_list(pet1)

appointment2.add_pet_to_list(pet4)
appointment2.add_pet_to_list(pet3)

appointment3.add_pet_to_list(pet5)
appointment3.add_pet_to_list(pet6)

for appointments in appointment_list:
    print("Pet Name: ", appointments.pet_details()["Pet Name"])
    print("Disease or Issue: ", appointments.pet_details()["Disease or Issue"])
    print("Date: ", appointments.pet_details()["Date"])
    print("Time: ", appointments.pet_details()["Appointment Time"])
    print("Vet: ", appointments.pet_details()["Vet"])
    print("////////////////////////////////////////")

print("*********************************************")

for appointments in appointment_list:
    for pets in (appointments.pet_details()["List of Pets"]):
        print('Pet Name: ', pets.name, "Breed: ", pets.breed, " Owner Name: ", pets.owner_f_name + " " + pets.owner_l_name)
        print("///////////////////////////////////////////////////////////")



# Keep a list of vets
vet1.add_vets_to_list(vet1)
vet2.add_vets_to_list(vet2)
#need to be able to add to details for both pets and owners