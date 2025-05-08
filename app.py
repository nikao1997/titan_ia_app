import streamlit as st
from PIL import Image
from pathlib import Path
import base64

# Função para tocar som
def play_audio(file_path):
    audio_file = open(file_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

# Layout
st.set_page_config(page_title="TITAN.IA", layout="centered")

# Logo
image = Image.open("IMG_3287.png")
st.image(image, width=300)
st.title("Robô de Trading - TITAN.IA")

# Simulação de leitura de gráfico e entrada
opcao = st.selectbox("Simular leitura de:", ["", "Entrada de Compra", "Entrada de Venda"])

if opcao == "Entrada de Compra":
    st.success("Sinal de COMPRA detectado!")
    play_audio("compra.mp3")
elif opcao == "Entrada de Venda":
    st.error("Sinal de VENDA detectado!")
    play_audio("venda.mp3")