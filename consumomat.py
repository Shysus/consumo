import streamlit as st
from datetime import date

st.title("Sistema de Controle de Material")

# Dados dos técnicos e materiais (completos)
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
    "VAGNO PERALTA RODRIGUES",
]

materiais = {
    "22061736 - CABO DROP 1FO LOW F FIG8 LOW CINZA": 86,  # Limite em metros
}

# Seleção do técnico
tecnico_selecionado = st.selectbox("Nome Técnico:", tecnicos)

# Seleção do material
material_selecionado = st.selectbox("Material:", list(materiais.keys()))

# Quantidade utilizada
quantidade_utilizada = st.number_input(
    "Quantidade utilizada (metros):", min_value=0
)

# Contrato
contrato = st.text_input("Contrato:")

# Botão para calcular
if st.button("Calcular"):
    # Verificar se a quantidade excede o limite
    limite_material = materiais[material_selecionado]
    if quantidade_utilizada > limite_material:
        resto = quantidade_utilizada - limite_material
        st.warning(f"A quantidade utilizada excede o limite de {limite_material} metros.")
        st.write(
            f"**Técnico:** {tecnico_selecionado}\n"
            f"**Data:** {date.today().strftime('%d/%m/%Y')}\n"
            f"**Resto:** {resto} metros\n"
            f"**Contrato:** {contrato}"
        )
    else:
        st.success("Quantidade dentro do limite.")
