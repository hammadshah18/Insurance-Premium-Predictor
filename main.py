from fastapi import FastAPI
from fastapi import HTTPException
from model.predict import predict_output,model,Model_version
from fastapi.responses import JSONResponse
from schema.user_input import userinput
from schema.predicted_respones import prediction_response

app=FastAPI()
    
#Human readable        
@app.get("/")
def home():
    return {"message": "Welcome to the Health Insurance Prediction API! "}
#Machine readable
@app.get("/health")
def health_check():
    return {"Status ":"ok",
            "Version":Model_version,
            "Model_loaded": model is not None}

@app.post('/predict',response_model=prediction_response)
def predict_premium(data:userinput):
    try:
        user_input = {
    "bmi": data.bmi,
    "lifestyle_risk": data.life_risk,  
    "age_group": data.age_grp,         
    "city_tier": data.city_tier,       
    "income_lpa": data.income_lpa,     
    "occupation": data.occupation 
    }

        # input_df=pd.DataFrame([{
        #     "bmi":data.bmi,
        #     "life_risk":data.life_risk,
        #     "Age_Group":data.age_grp,
        #     "city_Tier":data.city_tier,
        #     "Income_LPA":data.income_lpa,
        #     "Occupation":data.occupation
        # }])

        prediction,confidence,probabilities=predict_output(user_input)

        prediction_dict = predict_output(user_input)
        return prediction_response(
            predicted_class=prediction_dict["predicted_class"],
            confidence=prediction_dict["confidence"],
            class_probs=prediction_dict["class_probs"]
        )

    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error during prediction")
        
    #     prediction,confidence,probabilities=predict_output(user_input)
    #     return JSONResponse(status_code=200,content={"Responce": prediction})
    # except Exception as e:
    #     print(f"Error during prediction: {str(e)}")  # This will show in your server logs
        
        # return JSONResponse(
        #     status_code=500,
        #     content={"error": "Internal server error occurred during prediction"}
        # )


# if __name__=="main":
#     import uvicorn
#     uvicorn.run(app,port=8000)
        
