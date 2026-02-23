# 💰 Analisador Financeiro de WhatsApp com IA

Uma aplicação web interativa construída com **Streamlit** que lê, processa e analisa registros financeiros formatados em texto (como exportações de mensagens do WhatsApp). 

O grande diferencial do projeto é a integração com a **API da OpenAI (GPT-4o)**, que atua como um Consultor Financeiro Sênior. A IA não apenas faz contas, mas analisa seu comportamento financeiro, diagnostica sua saúde financeira e gera um plano de ação tático baseado nos seus dados.

---

## ✨ Funcionalidades

* **Processamento Automático:** Lê arquivos `.txt` e extrai automaticamente datas, descrições, categorias e valores usando Expressões Regulares (Regex).
* **Dashboard Visual:** Apresenta o saldo atual, total de ganhos e gastos de forma clara.
* **Gráficos Interativos:** Gera um gráfico de pizza mostrando a proporção entre ganhos e gastos.
* **Tabelas de Categoria:** Agrupa e soma seus ganhos e gastos por categoria, ordenando do maior para o menor.
* **Consultoria com IA (GPT-4o):** Gera um relatório profundo contendo:
    * Diagnóstico de Saúde Financeira e Taxa de Poupança.
    * Análise de Fluxo de Caixa (Regra 50-30-20).
    * Insights Comportamentais (identificação de vazamento de dinheiro).
    * Plano de Ação Tático (passos práticos para melhorar as finanças).
    * Uma "Dica de Ouro" personalizada.

---

## 📸 Capturas de Tela


### 1. Tela Inicial e Upload de Arquivo
<img width="1747" height="820" alt="telainicial" src="https://github.com/user-attachments/assets/50b93ad9-9a7d-4dfa-b88a-625fee845bf2" />

*Interface simples e intuitiva para envio do arquivo de texto.*

### 2. Resumo Financeiro e Gráficos
<img width="1743" height="812" alt="Captura de tela 2026-02-23 160238" src="https://github.com/user-attachments/assets/ed546e02-7a71-485f-b32c-c9a59c9e1836" />

*Visão geral do saldo e gráfico comparativo gerado automaticamente.*

### 3. Tabelas de Categorias
<img width="1749" height="820" alt="Captura de tela 2026-02-23 160248" src="https://github.com/user-attachments/assets/83c13f95-d481-40d1-bf4f-19ed8048dacf" />

*Detalhamento de onde o dinheiro está vindo e para onde está indo.*

### 4. Consultoria Gerada por IA
<img width="1753" height="815" alt="Captura de tela 2026-02-23 160257" src="https://github.com/user-attachments/assets/5c023d2a-71bb-4b93-a89a-0d17ad8503e6" />
<img width="1750" height="646" alt="Captura de tela 2026-02-23 160307" src="https://github.com/user-attachments/assets/0c0909f3-b8b4-4bf7-b91e-1ada1289e797" />

*Relatório detalhado gerado pelo modelo GPT-4o da OpenAI.*

---

## 📝 Como formatar o arquivo `.txt`

Para que o sistema leia seus dados corretamente, cada linha do arquivo de texto deve seguir **exatamente** o padrão abaixo (muito comum em anotações rápidas ou mensagens de WhatsApp):

`DD/MM/AAAA HH:MM - Nome: descrição, Categoria, +/-R$Valor`

**Exemplos Válidos:**
```text
01/03/2026 09:00 - Bernardo: Bolsa estágio, Receita, +R$1200.00
10/03/2026 18:45 - Bernardo: Mensalidade Faculdade, Educação, -R$300.00
15/03/2026 11:20 - Bernardo: Uniforme Basquete, Esportes, -R$120.00
```

---

## 🚀 Como instalar e rodar o projeto localmente

### 1. Pré-requisitos
* Python 3.8 ou superior instalado.
* Uma chave de API da OpenAI.

### 2. Clonando o Repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
```

### 3. Criando o Ambiente Virtual (Recomendado)
```Bash
python -m venv venv

# No Windows:
venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate
```

### 4. Instalando as Dependências
Crie um arquivo chamado requirements.txt na raiz do projeto com as bibliotecas listadas (Streamlit, Pandas, Matplotlib, OpenAI, etc) e rode:
```Bash
pip install -r requirements.txt
```

### 5. Configurando Variáveis de Ambiente
Crie um arquivo chamado .env na raiz do projeto e insira a sua chave da OpenAI:
```Bash
OPENAI_API_KEY=sk-sua_chave_aqui_...
```

### 6. Executando a Aplicação
```Bash
streamlit run app.py
```
O aplicativo abrirá automaticamente no seu navegador.

---

## 🛠️ Tecnologias Utilizadas

* **Streamlit:** Criação da interface web frontend e roteamento.

* **OpenAI API (GPT-4o):** Motor de Inteligência Artificial para análise semântica e financeira.

* **Pandas:** Manipulação e estruturação de dados em DataFrames para tabelas.

* **Matplotlib:** Geração do gráfico de pizza.

* **Python re (Regex):** Extração de dados brutos a partir das strings de texto.

---

Desenvolvido por Bernardo Silva Sant Ana de Oliveira como projeto do Módulo 2 do curso de Data Science da Codi Academy.
