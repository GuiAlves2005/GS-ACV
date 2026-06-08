import streamlit as st
from PIL import Image
import numpy as np
import os

st.set_page_config(page_title="SpaceData Triage - Visão", page_icon="📸")

st.title("📸 SpaceData Triage - Visão Computacional")
st.markdown("### Módulo ACV: Triagem de Imagens Orbitais")
st.info("A interface carregou com sucesso! O sistema está pronto para receber a imagem.")

# O upload vem primeiro
uploaded_file = st.file_uploader("Escolha uma imagem JPG", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem Satelital", width=300)
    
    # Só tenta carregar o peso do modelo SE o botão for apertado
    if st.button("Executar Triagem Visual", use_container_width=True):
        with st.spinner("Acordando a Inteligência Artificial e processando os filtros convolucionais..."):
            
            import tensorflow as tf
            DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
            CAMINHO_MODELO = os.path.join(DIRETORIO_ATUAL, '..', 'notebook', 'modelo_acv_robusto.h5')
            
            try:
                modelo = tf.keras.models.load_model(CAMINHO_MODELO)
                
                img_array = np.array(image.resize((64, 64))) / 255.0 
                img_array = np.expand_dims(img_array, axis=0) 
                
                predicao = modelo.predict(img_array)[0][0]
                
                if predicao > 0.5:
                    st.error(f"🚨 **IMAGEM DESCARTADA (OBSTRUÍDA)** | Confiança: {predicao*100:.1f}%")
                else:
                    st.success(f"✅ **IMAGEM APROVADA (LIMPA)** | Confiança: {(1-predicao)*100:.1f}%")
                    
            except Exception as e:
                st.error(f"Erro interno do modelo: {e}")