from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    # name: str = Field(max_length=50)
    name: str
    email: EmailStr
    age: int 
    weight: float = Field(gt=0)
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains=['hdfc.com','icici.com']
        # abc@gmail.com
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Updated')

patient_info={'name':'priyanshi', 'email':'abc@hdfc.com','age':"16.0", 'weight': 75.2, 'married':'True' ,'allergies':['pollen','dust'],'contact_details':{'phone':'234556'} }
patient1=Patient(**patient_info)
update_patient_data(patient1)