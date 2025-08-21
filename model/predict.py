import json
import pickle
import pandas as pd
with open("model/Model.pkl","rb") as f:
    model=pickle.load(f)

Model_version="1.0.0"
class_labels=model.classes_.tolist()

def predict_output(user_input : dict):

    input_df=pd.DataFrame([user_input])

    predicted_class=model.predict(input_df)[0]
    probabilities=model.predict_proba(input_df)[0]
    confidence=max(probabilities)
    class_probs=dict(zip(class_labels,map(lambda p:round(p,4),probabilities)))
    return {
        "predicted_class":predicted_class,
        "confidence":round(confidence,4),
        "probabilites":class_probs
        }
    
    return output
