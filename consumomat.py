import streamlit as st
import pandas as pd
from datetime import date
import gspread
import json
import os

# Carregar credenciais a partir da variável de ambiente
creds_json = os.environ.get('GOOGLE_SHEETS_CREDENTIALS')
creds_dict = json.loads(creds_json)
gc = gspread.service_account_from_dict(creds_dict)

# Abrir a planilha (substitua pelo ID da sua planilha)
sh = gc.open_by_key('1bt8THai3U3rOcVutZjwDkUm3A-G85MoagYlf6A0bYM0')  
worksheet = sh.sheet1

# Carregar os dados da planilha
try:
    df = pd.DataFrame(worksheet.get_all_records())
except gspread.exceptions.APIError as e:
    st.error(f"Erro ao acessar a planilha: {e}")
    st.stop()  # Interrompe a execução se não conseguir carregar a planilha

# Lista completa de técnicos 
tecnicos = [
    "ALEXANDRE GRANJEIRO VENTURA",
    "CHARLES DOS SANTOS VILHALVA",
    "GUILHERME DUARTE BARBOSA",
    "GUILHERME MATOS ZANDONA",
    "JOSE CARLOS DA SILVA JUNIOR",
    "LUIZ FELIPE BALBUENA ARIA",
    "SAMUEL JUNIOR DE LIMA SCHNEIDER",
    "WELLYNGTON GABRIEL MARTINES PERES",
    "EMERSON DE LIMA COUTRIM",
    "JOAO VITOR DA SILVA OLIVEIRA",
    "ALEXANDRE AGNALDO RAMOS",
    "DANILO VICTOR GARCIA DE CARVALHO",
    "MAICON JUNIOR CORDEIRO DE CARVALHO",
    "MARIO JOHNNY GONCALVES CARDOZO",
    "WILSON JUNIOR ANTUNES DA SILVA",
    "DANIEL ANTUNES SANCHES",
    "ELIMAR SOUZA GODOY",
    "LUIS HENRIQUE ALFONZO GAYOSO",
    "RENATO RUAN SCHNEIDER LIMA",
    "VAGNO PERALTA RODRIGUES"
]

# Material
material = "22061736 - CABO DROP 1FO LOW F FIG8 LOW CINZA"

# Interface Streamlit
st.title("Controle de Material")

nome_tecnico = st.selectbox("Nome Técnico", tecnicos)
st.write(f"Material: {material}")

quantidade_utilizada = st.number_input("Quantidade Utilizada", min_value=0)

if st.button("Enviar"):
    if quantidade_utilizada > 86:
        quantidade_extra = quantidade_utilizada - 86
        nova_linha = [nome_tecnico, date.today(), material, quantidade_utilizada, quantidade_extra]
        try:
            worksheet.append_row(nova_linha)  # Adicionar a linha ao Google Sheets
        except gspread.exceptions.APIError as e:
            st.error(f"Erro ao adicionar dados à planilha: {e}")
        else:
            df = df.append(pd.Series(nova_linha, index=df.columns), ignore_index=True)  # Atualizar o DataFrame local
            st.success(f"Dados adicionados à planilha! Quantidade extra: {quantidade_extra}")
    else:
        st.info("Quantidade dentro do limite.")

# Exibir o DataFrame (opcional)
st.subheader("Dados Atuais:")
st.dataframe(df)
