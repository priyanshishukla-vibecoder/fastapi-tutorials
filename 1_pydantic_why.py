# def insert_patient_data(name:str, age:int):

#     if type(name)==str and type(age)==int:
#         if age<0:
#             raise ValueError("Age can't be zero")
#         print(name)
#         print(age)
#         print('inserted into database')
#     else:
#         raise TypeError('Incorrect datatype')

# insert_patient_data('priyanshi','22')

# def update_patient_data(name:str, age:int):

#     if type(name)==str and type(age)==int:
#         print(name)
#         print(age)
#         print('inserted into database')
#     else:
#         raise TypeError('Incorrect datatype')

# update_patient_data('priyanshi','22')


from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

#field - datavalidation+attach metadata 1.custom datavalidation 2. metadata 3.  default values
class Patient(BaseModel):

    # name: str = Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title = 'Name of the patient', description='Give the name of the patient in less than 50 characters', example=['Priyanshi','Shreya'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: float = Annotated[float, Field(gt=0, strict=True)]
    married: bool = Annotated[bool, Field(default=None, description='Is the patient married')]
    allergies: Optional[List[str]]=Field(max_length=5)
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.linkedin_url)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('Updated')

patient_info={'name':'priyanshi', 'email':'abc@gmail.com', 'linkedin_url':'https://www.linkedin.com/in/priyanshishukla27/','age':"-16.0", 'weight': -75.2, 'contact_details':{'phone':'234556'} }

patient1=Patient(**patient_info)

update_patient_data(patient1)