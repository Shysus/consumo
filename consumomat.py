import streamlit as st
import json
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Verificar segredos
try:
    st.write(st.secrets["gspread_cred"])
except Exception as e:
    st.error(f"Erro ao acessar o segredo: {e}")

# Configurações para Google Sheets
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = json.loads(st.secrets["gspread_cred"])
credentials = Credentials.from_service_account_info(creds_dict, scopes=SCOPE)

# Autenticando e acessando a planilha
try:
    client = gspread.authorize(credentials)
    sheet = client.open_by_key("1bt8THai3U3rOcVutZjwDkUm3A-G85MoagYlf6A0bYM0").worksheet("CABOS")
    st.write("Conectado ao Google Sheets com sucesso.")
except Exception as e:
    st.error(f"Erro ao acessar o Google Sheets: {e}")

# Função para registrar os dados
def registrar_consumo(nome_tecnico, contrato, quantidade_usada, data_registro):
    try:
        sheet.append_row([data_registro, nome_tecnico, contrato, quantidade_usada])
        st.success("Dados registrados com sucesso!")
    except Exception as e:
        st.error(f"Erro ao registrar os dados: {e}")

# Interface do Streamlit
st.title("Registro de Consumo de Cabos")

# Campo de seleção para nome do técnico
tecnicos = [
    "ALEXANDRE GRANJEIRO VENTURA", "CHARLES DOS SANTOS VILHALVA", "GUILHERME DUARTE BARBOSA", 
    "GUILHERME MATOS ZANDONA", "JOSE CARLOS DA SILVA JUNIOR", "LUIZ FELIPE BALBUENA ARIA", 
    "SAMUEL JUNIOR DE LIMA SCHNEIDER", "WELLYNGTON GABRIEL MARTINES PERES", "EMERSON DE LIMA COUTRIM", 
    "JOAO VITOR DA SILVA OLIVEIRA", "ALEXANDRE AGNALDO RAMOS", "DANILO VICTOR GARCIA DE CARVALHO", 
    "MAICON JUNIOR CORDEIRO DE CARVALHO", "MARIO JOHNNY GONCALVES CARDOZO", "WILSON JUNIOR ANTUNES DA SILVA", 
    "DANIEL ANTUNES SANCHES", "ELIMAR SOUZA GODOY", "LUIS HENRIQUE ALFONZO GAYOSO", 
    "RENATO RUAN SCHNEIDER LIMA", "VAGNO PERALTA RODRIGUES"
]
nome_tecnico = st.selectbox("Nome Técnico", tecnicos)

# Campo para contrato
contrato = st.text_input("Contrato")

# Campo de seleção para material
material = "22061736 - CABO DROP 1FO LOW F FIG8 LOW CINZA"
st.write(f"Material: {material}")

# Campo para quantidade utilizada
quantidade_utilizada = st.number_input("Quantidade utilizada (em MTS)", min_value=0, max_value=86, step=1)

# Botão para registrar
if st.button("Registrar"):
    data_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if quantidade_utilizada <= 86:
        registrar_consumo(nome_tecnico, contrato, quantidade_utilizada, data_registro)
    else:
        resto = quantidade_utilizada - 86
        registrar_consumo(nome_tecnico, contrato, 86, data_registro)
        st.warning(f"A quantidade utilizada excede o limite. Resto: {resto} MTS")
