from fastapi import FastAPI
import pickle
from fastapi.testclient import TestClient
from pydantic import BaseModel
from fastapi.testclient import TestClient
from typing import Union
import pandas.util.testing as tm

#load modele and data
model = pickle.load(open('lightgbm_DONE.pkl','rb'))
import pandas as pd
X = pd.read_csv('testing_data.csv')

# Création d'une nouvelle instance fastAPI
app = FastAPI()


# Définir un objet ( une classe) pour réaliser des requêtes
# dot notation (.)
class request_body(BaseModel):
    SK_ID_CURR: float

#    class Config:
#        orm_mode = True


# Définition du chemin du point de terminaison (API)
@app.post("/predict")  # local : http://127.0.0.1:8000/predict

# Définition de la fonction de prédiction
def predict(ID: request_body):
        # Nouvelles données sur lesquelles on fait la prédiction
        donnees_client = X[X['SK_ID_CURR'] == ID.SK_ID_CURR]
        # Prédiction
        prevision = model.predict_proba(donnees_client.drop(['SK_ID_CURR'], axis=1))
        classe = model.predict(donnees_client.drop(['SK_ID_CURR'], axis=1))
        print(classe)
        return {"prevision": max(prevision[0]), "classe":str(classe[0])}  #prevision[:, 1][0] "probabilite": prevision[:, 1][0].max()


#Entrer le num client
@app.get("/items/{item_id}")
async def read_user_item(client_id: str):
        item = {"client_id": client_id}
        return item

# uvicorn main:app


#if __name__ == "__main__":
#    app.run(port=5000,debug=True)"""


#Test unitaire
#Mettre code sur Github Dashboard repo apart et APi apart
#Créer un compte azure pour déployment API
#Créer un compte AWS et configurer
