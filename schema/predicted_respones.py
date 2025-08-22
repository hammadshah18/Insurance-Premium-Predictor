from pydantic import BaseModel,Field
from typing import Dict,AnyStr


class prediction_response(BaseModel):
    predicted_class:str = Field(...,
                                   
        description="The Predict insurance category",

        examples=["High"])

    confidence:float=Field(...,description="Model's Confidence Score for predicted class(range 0 to 1)",examples=[0.832])

    class_probs:Dict[str,float]=Field(...,description="Probabilites distribution for all classes ",examples=[{"low":0.01,"medium":0.8,"high":0.9}])
