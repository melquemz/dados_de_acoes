from datetime import date
import datetime as dt
from pandas_datareader import data as web
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


st.title("Historico Das Ações")

st.markdown("Preenchar os campos para ter acesso aos dados da ação desejada")

dataStart = st.date_input(
     "Qual a data de inicio ?",
     dt.date(2020, 2, 2))

dataEnd = st.date_input(
     "Qual a data de encerramento ?",
     dt.date(2021, 12, 12))

empresa = st.text_input('Digite o nome da ação')

st.title('Dados Da Ação')
st.markdown('---')



if len(empresa) > 0:

    cotacao_bovespa = web.DataReader(f'{empresa}.SA', data_source = 'yahoo', start = f"{dataStart}", end = f"{dataEnd}")
    st.dataframe(cotacao_bovespa)

    st.line_chart (cotacao_bovespa["Adj Close"])

image = Image.open('acoes.jpg')
st.sidebar.image(image,caption='Mercado Financeiro',use_column_width=True)

st.sidebar.markdown('Feito por : Melquezedeque Lima')

st.sidebar.markdown("Redes Sociais :")
st.sidebar.markdown("- [Linkedin](https://www.linkedin.com/in/melquezedeque-lima-4056231b2/)")
st.sidebar.markdown("- [Github](https://github.com/melquemz)")    
  

