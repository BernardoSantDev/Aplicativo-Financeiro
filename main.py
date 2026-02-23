import streamlit as st               
import pandas as pd                   
import matplotlib.pyplot as plt       
import re                             
import os                             
from dotenv import load_dotenv        
from openai import OpenAI             


load_dotenv()  
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  

categorias_gastos_fixos = [
    'Aluguel', 'Farmacia', 'Padaria', 'Mercado', 'Supermercado',
    'Energia', 'Água', 'Luz', 'Internet', 'Transporte', 'Combustivel', 'Alimentação'
]

categorias_ganhos_fixos = ['Renda']

