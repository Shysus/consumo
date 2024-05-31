import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import json
from datetime import datetime

try:
    # Carregar credenciais do Google Sheets a partir dos segredos
    creds_dict = st.secrets["gspread_cred"]
    
    # Definir os escopos necessários
    SCOPE = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    
    # Atualizar as credenciais para incluir os escopos
    creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPE)

    # Autenticar e acessar a planilha
    client = gspread.authorize(creds)
    sheet = client.open_by_key("1bt8THai3U3rOcVutZjwDkUm3A-G85MoagYlf6A0bYM0").worksheet("CABOS")

    # Nome Técnico
    nome_tecnico = st.selectbox(
        "Nome Técnico", [
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
    )

    # Contrato
    contrato = st.text_input("Contrato")

    # Material
    material = st.selectbox("Material", ["22061736 - CABO DROP 1FO LOW F FIG8 LOW CINZA"])

    # Quantidade utilizada
    quantidade_utilizada = st.number_input("Quantidade utilizada", min_value=0)

    # Verificar se a quantidade excede 86
    if quantidade_utilizada > 86:
        resto = quantidade_utilizada - 86
        st.warning(f"A quantidade excede o limite de 86MTS. Restante: {resto}MTS")

        if st.button("Registrar"):
            # Registrar os dados na planilha
            sheet.append_row([
                nome_tecnico,
                contrato,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                resto
            ])
            st.success("Dados registrados com sucesso!")
    else:
        if st.button("Registrar"):
            # Registrar os dados na planilha
            sheet.append_row([
                nome_tecnico,
                contrato,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                quantidade_utilizada
            ])
            st.success("Dados registrados com sucesso!")
except Exception as e:
    st.error(f"Erro ao acessar o Google Sheets: {e}")
