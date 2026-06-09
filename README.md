# 📸 SpaceData Triage - Módulo ACV (Visão Computacional)

Bem-vindo ao repositório de Applied Computer Vision (ACV) do projeto **SpaceData Triage**. 

Como estudante de Engenharia de Software, desenvolvi este módulo para resolver o problema de transmissão de dados visuais inúteis na nova economia espacial. Satélites capturam milhares de imagens por dia, mas muitas delas estão completamente obstruídas por nuvens densas ou ruído nos sensores. Nossa solução utiliza Redes Neurais Convolucionais (CNNs) para classificar imagens em "Limpas" (terreno visível) ou "Obstruídas" (nuvens/ruído), descartando o lixo na própria órbita para economizar banda e processamento na Terra.

---

## 1. O Dataset Sintético
Para treinar as redes neurais e demonstrar o conceito, criei um pipeline de geração de dados sintéticos. O código constrói proceduralmente abstrações de terrenos espaciais (tons de verde/marrom) e sobrepõe obstruções simuladas (círculos brancos representando cobertura de nuvens).

## 2. Arquitetura das Redes Neurais (CNN)
Para garantir a melhor performance técnica, construí e comparei duas arquiteturas de Redes Neurais Convolucionais (CNN) totalmente do zero usando **TensorFlow/Keras**:

* **CNN Simples (Baseline):** Arquitetura com duas camadas convolucionais básicas e MaxPooling.
* **CNN Robusta:** Adição de mais filtros convolucionais (32 -> 64 -> 64) e uma camada de `Dropout (0.5)` para forçar a rede a generalizar e evitar o overfitting das formas geradas.

## 3. Comparação e Resultados

<img width="1018" height="473" alt="image" src="https://github.com/user-attachments/assets/ded49c69-8f2d-423e-989c-36108717baf5" />


**Análise Técnica:**
O modelo "CNN Robusta" provou ser imensamente superior. Como demonstrado no gráfico de perda (Loss), a rede robusta minimizou o erro quase a zero logo na primeira época de treinamento, extraindo os padrões das nuvens com alta eficácia, enquanto a arquitetura simples levou muito mais tempo para estabilizar. A acurácia atingiu a métrica exigida com folga. O modelo robusto foi salvo como `.h5` para o deploy.

## 4. Deploy da Aplicação Visual
Desenvolvi uma interface interativa com **Streamlit** para o consumo do modelo treinado. O usuário pode fazer o upload de uma imagem capturada e a IA embarcada retorna a classificação instantaneamente, simulando o ambiente do satélite.

<img width="1116" height="924" alt="image" src="https://github.com/user-attachments/assets/532ebbb8-abfb-4cb6-aa0c-d498500eeddb" />


<img width="1112" height="911" alt="image" src="https://github.com/user-attachments/assets/4a318156-580f-42e3-8be7-65229b379f93" />

⚠️ **ATENÇÃO PROFESSOR:** Como as imagens não foram subidas para o repositório por questões de otimização de espaço, **é obrigatório rodar o script `gerar_imagens.py`** localizado na raiz do projeto. Ele criará a pasta `dataset/` com as 200 imagens sintéticas de treino/teste necessárias antes de prosseguir com a arquitetura neural.
---

## 💻 Instruções para Execução

Para testar este projeto localmente, siga os passos estritamente na ordem abaixo:

**1. Instale as dependências:**
`bash
pip install tensorflow matplotlib opencv-python pillow numpy streamlit
`

**2. Gere o Dataset de Imagens:**
No terminal, execute o script de geração. Ele criará as pastas e as imagens automaticamente:
`bash
python gerar_imagens.py
`

**3. Treine a Rede Neural:**
Abra o arquivo `notebook/acv_cnn_triagem.ipynb` e execute todas as células para treinar a CNN. O modelo será salvo como `modelo_acv_robusto.h5` fisicamente na pasta.

**4. Execute a Interface de Triagem:**
No terminal (na raiz do projeto), execute o comando apontando para a porta 8502 (para evitar conflitos):
`bash
python -m streamlit run app/app_acv.py --server.port 8502
`

O aplicativo abrirá no navegador pronto para receber uploads e realizar a triagem visual.


**Integrantes:**
Guilherme Alves de Lima Rm 550433
Bruno Venturi Lopes Vieira Rm 99431
Leonardo Ruiz Rm 98901
