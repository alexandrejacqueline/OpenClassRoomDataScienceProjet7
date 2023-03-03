from fastapi.testclient import TestClient
from fastapi import status
import streamlit as st
from main import app
from fastapi import FastAPI
client = TestClient(app)

def test_correct():

    response=client.get( "/")
    assert response.status_code == 200
    assert response.json()=={'msg':"Hello World"}

#def test id client int or float

#when i use pytest is return a error 404 but the API work