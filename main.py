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

def gerar_grafico(ganhos, gastos):
    labels = ['Ganhos', 'Gastos']
    valores = [ganhos, gastos]
    cores = ['#007acc', '#FFA500'] 
    fig, ax = plt.subplots()
    ax.pie(valores, labels=labels, autopct='%1.1f%%', colors=cores, startangle=90)
    ax.axis('equal') 
    st.pyplot(fig)   


def gerar_insight_ia(ganhos, gastos, saldo, categorias_ganhos, categorias_gastos):
    texto_ganhos = "\n".join([f"- {k}: R$ {v}" for k, v in categorias_ganhos.items()]) or "Nenhum"
    texto_gastos = "\n".join([f"- {k}: R$ {v}" for k, v in categorias_gastos.items()]) or "Nenhum"
    prompt = f"""
    # ROLE & OBJETIVO
    Você é um Consultor Financeiro Sênior e Planejador Financeiro Pessoal (CFP) com vasta experiência em economia comportamental. Seu objetivo é analisar os dados financeiros brutos de um cliente, identificar padrões de comportamento, diagnosticar a saúde financeira e fornecer um plano de ação estratégico e personalizado.

    # DADOS DO CLIENTE
    Abaixo estão os dados financeiros consolidados do período:

    * **Total de Ganhos:** R$ {ganhos:.2f}
    * **Total de Gastos:** R$ {gastos:.2f}
    * **Saldo Final:** R$ {saldo:.2f}
    * **Detalhamento de Ganhos (Fonte e Valor):**
        {texto_ganhos}
    * **Detalhamento de Gastos (Categoria e Valor):**
        {texto_gastos}

    # INSTRUÇÕES DE ANÁLISE
    Não forneça apenas números; forneça inteligência. Sua resposta deve seguir estritamente a estrutura abaixo:

    ## 1. Diagnóstico de Saúde Financeira (Resumo Executivo)
    * Comece com uma frase de impacto sobre a situação atual (ex: "O usuário está vivendo perigosamente acima de seus meios" ou "O usuário demonstra excelente controle, mas baixa rentabilidade").
    * Calcule e apresente a **Taxa de Poupança** ( (Ganhos - Gastos) / Ganhos ).
    * Classifique o perfil financeiro atual: (Endividado / No Limite / Poupador / Investidor).

    ## 2. Análise Profunda de Fluxo de Caixa
    * **Raio-X dos Gastos:** Identifique qual categoria consome a maior fatia do orçamento. Isso é saudável? Compare com a regra ideal de 50-30-20 (50% essenciais, 30% desejos, 20% investimentos) se aplicável.
    * **Análise de Receita:** Avalie se a renda é diversificada ou dependente de uma única fonte. Há risco aqui?

    ## 3. Insights Comportamentais (O "Porquê")
    * Identifique **padrões de consumo**. Existem muitos gastos pequenos que somados viram uma "bola de neve"? Existem gastos supérfluos disfarçados de essenciais?
    * Aponte qualquer "vazamento de dinheiro" óbvio nas categorias fornecidas.

    ## 4. Plano de Ação Tático (Próximos Passos)
    Liste 3 a 5 ações concretas e imediatas que o usuário deve tomar.
    * *Exemplo:* "Reduzir a categoria X em 15% para liberar R$ Y para a reserva de emergência."
    * *Exemplo:* "A categoria 'Lazer' está consumindo 40% da renda; o teto recomendado é X%."

    ## 5. Dica de Ouro
    Uma sugestão final, de alto impacto, baseada em psicologia financeira ou otimização de recursos para este caso específico.

    ---
    **Tom de Voz:** Profissional, empático, direto e focado em soluções. Use formatação Markdown (negrito, listas) para facilitar a leitura.
    """
    resposta = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=2000
    )
    return resposta.choices[0].message.content


st.set_page_config(page_title="Analisador Financeiro de WhatsApp com IA", layout="centered")
st.title("💰 Analisador Financeiro de WhatsApp com IA")
st.write("📄 Envie um arquivo `.txt` com mensagens no formato:")
st.code("16/07/2025 15:04 - Nome: descrição, categoria, +R$3000")
uploaded_file = st.file_uploader("📥 Envie seu arquivo aqui", type=['txt'])
if uploaded_file is not None:
    conteudo = uploaded_file.read().decode('utf-8')
    ganhos, gastos, saldo, categorias_ganhos, categorias_gastos = processar_conversas(conteudo)
    st.subheader("📊 Resumo Financeiro")
    st.write(f"**Saldo atual:** R$ {saldo}")
    st.write(f"**Total de ganhos:** R$ {ganhos}")
    st.write(f"**Total de gastos:** R$ {gastos}")
    st.subheader("🍕 Gráfico de Ganhos vs Gastos")
    gerar_grafico(ganhos, gastos)
    st.subheader("📥 Tabela de Entradas (Ganhos)")
    if categorias_ganhos:
        df_ganhos = pd.DataFrame(list(categorias_ganhos.items()), columns=['Categoria', 'Total ganho'])
        st.table(df_ganhos.sort_values(by='Total ganho', ascending=False))
    else:
        st.write("Nenhuma entrada encontrada.")
    st.subheader("📤 Tabela de Saídas (Gastos)")
    if categorias_gastos:
        df_gastos = pd.DataFrame(list(categorias_gastos.items()), columns=['Categoria', 'Total gasto'])
        st.table(df_gastos.sort_values(by='Total gasto', ascending=False))
    else:
        st.write("Nenhuma saída encontrada.")
    st.subheader("🤖 Insight Gerado por IA")
    with st.spinner("💡 Analisando seus dados e gerando um insight..."):
        insight = gerar_insight_ia(ganhos, gastos, saldo, categorias_ganhos, categorias_gastos)
    st.success(insight)