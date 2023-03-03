import streamlit as st
import pandas as pd
import numpy as np
import pickle
# import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Agg')
import json
import plotly.express as px
import altair as alt
import seaborn as sns
import requests


def identifiant_client():
    SK_ID_CURR = st.sidebar.selectbox('SK_ID_CURR', (X.SK_ID_CURR))
    data = {'SK_ID_CURR': SK_ID_CURR}
    ID_client = pd.DataFrame(data, index=[0])
    return data , ID_client


#if __name__ == "__main__":
st.set_page_config(
    page_title="Streamlit basics app",
    layout="centered"
)

st.title("Application qui prédit l'accord du crédit")

st.write("Auteur : Alexandre Jacqueline  - Data Scientist")

# Display the LOGO
#    img = Image.open("LOGO.png")
#    st.sidebar.image(img, width=300)

# Collecter le profil d'entrée
st.sidebar.header("Identifiant du client")

X = pd.read_csv('x_test.csv')

# Variables sélectionnées
df_vars_selected = pd.read_csv('df_vars_selected_saved.csv')
vars_selected = df_vars_selected['col_name'].to_list()



# Afficher les données du client:
vars_selected.insert(0, 'SK_ID_CURR')  # Ajout de l'identifiant aux features
st.subheader('1. Les données du client')

data, input_df = identifiant_client() #.iloc[0, 0]
input_df = input_df.iloc[0, 0]
X = X[vars_selected]
donnees_client = X[X['SK_ID_CURR'] == input_df]  # ligne du dataset qui concerne le client
st.write(donnees_client)



vars_selected.insert(0, 'SK_ID_CURR')  # Ajout de l'identifiant aux features
st.subheader('1. Les données du client')
data = {"SK_ID_CURR": float(input_df)}
API_ENDPOINT = "http://127.0.0.1:8000/predict"


#data = {"SK_ID_CURR": float(input_df)}

#st.write(data)
# sending post request and saving response as response object

r = requests.post(url=API_ENDPOINT, json=data).json()
#st.write(r)
classe = r["classe"]
prevision = r['prevision']

st.write(prevision)
st.write(classe)

#prevision = json.loads(prevision)

# st.write(prevision["reponse"])
# st.write(type(prevision))

# Appliquer le modèle sur le profil d'entrée
