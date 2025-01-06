from fastapi import FastAPI
import mlflow
import pandas as pd

# Charger le modèle MLflow
model_uri = "./mlflow_model_smote" 
model = mlflow.sklearn.load_model(model_uri)

# Création de l'app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue"}

@app.post("/predict/")
def predict(data: dict): # Convertir les données en DataFrame ou autre format attendu
    
    try :
        input_data = pd.DataFrame([data])

        # Faire des prédictions
        probabilities = model.predict_proba(input_data)[:, 1]
        predictions = (probabilities >= 0.38).astype(int)
        
        return {"predictions": predictions.tolist()}
    
    except ValueError as e:
        # Retourner une erreur 400 si la conversion échoue
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid data type provided: {e}"
        )