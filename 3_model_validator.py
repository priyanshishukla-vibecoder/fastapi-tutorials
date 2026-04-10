from pydantic import BaseModel, EmailStr, model_validator, Field, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    # name: str = Field(max_length=50)
    name: str
    email: EmailStr
    age: int 
    weight: float = Field(gt=0) #kg
    height: float #mtr
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) ->float:
        bmi= round(self.weight/(self.height**2),2)
        return bmi

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model

 
   

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('BMI', patient.calculate_bmi)
    print('Updated')

patient_info={'name':'priyanshi', 'email':'abc@hdfc.com','age':"65.0", 'weight': 75.2, 'height':1.72 , 'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'234556', 'emergency':'9926466308'} }
patient1=Patient(**patient_info)
update_patient_data(patient1)