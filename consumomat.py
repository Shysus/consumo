import streamlit as st
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Configurações do Google Sheets a partir dos segredos do Streamlit
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = json.loads(st.secrets["gspread_cred"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1bt8THai3U3rOcVutZjwDkUm3A-G85MoagYlf6A0bYM0").worksheet("CABOS")

# Lista de nomes técnicos
nomes_tecnicos = [
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

# Limite de quantidade
limite_quantidade = 86

# Interface do usuário
st.title("Controle de Material Utilizado")

# Seleção do Nome Técnico
nome_tecnico = st.selectbox("Nome Técnico", nomes_tecnicos)

# Campo para inserir o Contrato
contrato = st.text_input("Contrato")

# Seleção do Material
st.write("Material:", material)

# Entrada da Quantidade Utilizada
quantidade_utilizada = st.number_input("Quantidade utilizada (em metros)", min_value=0, max_value=1000, step=1)

# Verificação e cálculo do excedente
if st.button("Enviar"):
  data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  if quantidade_utilizada > limite_quantidade:
    excedente = quantidade_utilizada - limite_quantidade
    st.warning(f"Excedente detectado! O limite de {limite_quantidade} metros foi ultrapassado.")
    st.write(f"Nome Técnico: {nome_tecnico}")
    st.write(f"Contrato: {contrato}")
    st.write(f"Data: {data_atual}")
    st.write(f"Excedente: {excedente} metros")
    # Inserir dados no Google Sheets
    sheet.append_row([data_atual, nome_tecnico, contrato, quantidade_utilizada, excedente])
  else:
    st.success(f"A quantidade utilizada de {quantidade_utilizada} metros está dentro do limite de {limite_quantidade} metros.")
    # Inserir dados no Google Sheets sem excedente
    sheet.append_row([data_atual, nome_tecnico, contrato, quantidade_utilizada, 0])
