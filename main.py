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

def processar_conversas(conteudo):
    linhas = conteudo.split('\n')  # Divide o conteúdo por linha

    ganhos = 0
    gastos = 0
    categorias_ganhos = {}
    categorias_gastos = {}
    for linha in linhas:
        match = re.search(r'\d{2}/\d{2}/\d{4} \d{2}:\d{2} - (.*?): (.*?),\s*(.*?),\s*([+-]R\$?\d+)', linha)
        if match:
            nome = match.group(1).strip()
            descricao = match.group(2).strip()
            categoria = match.group(3).strip().capitalize()
            valor_bruto = match.group(4).replace('R$', '').replace('.', '').strip()
            valor = int(valor_bruto.replace('+', '').replace(',', '').replace('-', '')) * (-1 if '-' in match.group(4) else 1)
            if categoria in categorias_gastos_fixos or valor < 0:
                gastos += abs(valor)
                categorias_gastos[categoria] = categorias_gastos.get(categoria, 0) + abs(valor)
            elif categoria in categorias_ganhos_fixos or valor > 0:
                ganhos += valor
                categorias_ganhos[categoria] = categorias_ganhos.get(categoria, 0) + valor
    saldo = ganhos - gastos
    return ganhos, gastos, saldo, categorias_ganhos, categorias_gastos