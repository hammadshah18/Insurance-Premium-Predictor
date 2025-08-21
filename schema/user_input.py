
from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Dict,List,Literal,Annotated
from config.city_tier import tier_1_cities,tier_2_cities

class userinput(BaseModel):
    age: Annotated[int, Field(gt=0, lt=120, description='Enter your age')]
    weight: Annotated[float, Field(gt=0, description="Enter your weight")]
    height: Annotated[float, Field(gt=0, description="Enter you height")]
    income_lpa: Annotated[float, Field(gt=0, description="Enter Your Income in LPA")]
    smoker: Annotated[bool, Field(description="are you a smoker")]
    city: Annotated[str, Field(description="Enter your City")]
    occupation: Annotated[Literal["retired","freelancer","student","government_job","business_owner","unemployed","private_job"], Field(..., description="Enter Your Occupation")]


    @computed_field
    @property
    def bmi(self)->float:
        return (self.weight/self.height**2)
    
    @computed_field
    @property
    def life_risk(self)->str:
        if self.age and self.bmi > 30:
            return "high"
        elif self.age and self.bmi > 27:
            return  "medium"
        else :
            return "low"
        
    @field_validator('city')
    @classmethod
    def normalized_city(cls,v:str)->str:
        v=v.strip().title()
        return v
    
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3    
        

    @computed_field
    @property
    def age_grp(self)->str :
        if self.age <20:
            return "young"
        elif self.age <45:
            return "adult"   
        elif self.age <60:
            return "middle_aged"
        return "senior"
