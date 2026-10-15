#!/usr/bin/env python3

"""
Describe the current status of the clinic.
"""

# The overall structure
class Clinic():
    max_capacity_animals = 15
    animals=[]
    veterinarians=[]
    apointments=[]

    def __init__(self, animals, veterinarians, apointments):
        self.animals = list(animals)
        self.veterinarians = list(veterinarians)
        self.apointments = list(apointments)
        pass

    def __str__(self):
        return(f"The clinic is currently holding {len(self.animals)} animal(s) for {len(self.apointments)} apointment(s). {len(self.veterinarians)} veterinarian(s) is/are currently working in this clinic.")
        
"""
Describe animals
"""

# Animals
class Animal():
    medical_history=[]
    def __init__(self, name, age, species, owner, is_admitted, medical_history):
        self.name = name
        self.age = age
        self.species = species
        self.owner = owner
        self.is_admitted = is_admitted
        self.medical_history = medical_history
        pass

    def __str__(self):
        if self.is_admitted == True:
            return(f"The animal is {self.name}, {self.age} years old and owned by {self.owner}. {self.name} is currently admitted for x reason.")
        elif not self.medical_history: # Will return True if list is empty, False is medical_history contains something
            return(f"The animal is {self.name}, {self.age} years old and owned by {self.owner}. {self.name} is not at the clinic. No history of treatment")
        else: return(f"The animal is {self.name}, {self.age} years old and owned by {self.owner}. {self.name} is not at the clinic. Its last apointment was for: {', '.join(self.medical_history)}")
            

    def admit(self):
        if self.is_admitted == False:
            self.is_admitted = True
            return self.is_admitted
        else: 
            return(f"{self.name} is already admitted")

    def discharge(self):
        if self.is_admitted == True:
            self.is_admitted = False
            return self.is_admitted
        else: 
            return(f"{self.name} was already discharged")

    def add_treatment(self, reason):
        self.medical_history.append(str(reason))
        return self.medical_history

"""
Describing Veterinarian: name, speciality, what are the apointments he's in charge for.
"""

# Veterinarian
class Vet():
    apointments=[]
    def __init__(self, name, speciality, apointments, status):
        self.name = name
        self.speciality = speciality
        self.apointments = apointments
        self.status = status
        pass

    def __str__(self):
        if not self.apointments:
            return(f"The veterinarian is named {self.name} and is specialised in {self.speciality}. That person is free of apointment.")
        else: return(f"The veterinarian is named {self.name} and is specialised in {self.speciality}. Here is the next apointment of the veterinarian: {self.apointments}.")

        

"""
Handling apointment.
One apointment for one animal, one vet, one reason, one date. The status is updated manually.
"""

# Appointment
class Apt():
    status = None
    def __init__(self, animal, veterinarian, reason, date, status):
        self.animal = animal
        self.veterinarian = veterinarian
        self.reason = reason
        self.date = date
        self.status = status
        pass

    def __str__(self):
        if self.status == "scheduled":
            return(f"The apointment is fixed at {self.date}.\nThe animal {self.animal.name} will be treated for {self.reason}, by {self.veterinarian.name}.\nThe apointment is not completed yet")
        elif self.status == "cancelled":
            return(f"The apointment has been cancelled.")
        else: return (f"The apointment was completed.")

    def add_apt(self):
        if self.status == "scheduled":
            return(f"An apointment is already schedule for {self.animal.name}.")
        else: 
            self.status = "scheduled"
            return (f"The apointment has been schedule for {self.date}.")

    def complete(self):
        if self.status == "completed":
            return (f"That apointment was already completed")
        elif self.status == 'cancelled':
            return (f"That is impossible, the apointment was cancelled.")
        else: 
            self.animal.add_treatment(self.reason)
            self.status = "completed"
        return (f"The apointment is completed !")
                

    def cancel(self):
        if self.status == "completed":
            return(f"Impossible, the apointment for {self.reason} on {self.animal.name} was already completed.")
        elif self.status == "cancelled":
            return(f"The apointment for {self.reason} on {self.animal.name} was already cancelled.")
        else: 
            self.status = "cancelled"
            return (f"The apointment for {self.reason} on {self.animal.name} has been successfully cancelled.")


