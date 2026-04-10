from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str='Male'
    age:int
    address: Address


address_dict={'city':'indore', 'state':'M.P.', 'pin':'452005'}

address_1= Address(**address_dict)

patient_dict={'name':'priyanshi','age':22, 'address': address_1}

patient1=Patient(**patient_dict)

temp=patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))

# print(patient1)
# print(patient1.name)
# print(patient1.address.city)
# print(patient1.address.pin)


# Better organization of related data (e.g., vitals, address, insurance)

# Reusability : Use vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

#Validation: Nested models are validated automatically-no extra work needed
