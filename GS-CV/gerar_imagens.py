import os
import numpy as np
import cv2

# ==========================================
# 1. CONFIGURAÇÃO DAS PASTAS E PARÂMETROS
# ==========================================
base_dir = 'dataset'
limpas_dir = os.path.join(base_dir, 'imagens_limpas')
obstruidas_dir = os.path.join(base_dir, 'imagens_obstruidas')

# Cria as pastas automaticamente
os.makedirs(limpas_dir, exist_ok=True)
os.makedirs(obstruidas_dir, exist_ok=True)

num_images = 100  # Quantidade de imagens por classe
img_size = 64     # Tamanho da imagem (64x64 pixels para treinar rápido)

print("Gerando dataset sintético de imagens espaciais...")

# ==========================================
# 2. GERAÇÃO DAS IMAGENS
# ==========================================
for i in range(num_images):
    # --- A. Gerando Imagem "Limpa" (Simulando terreno visto do espaço) ---
    # OpenCV usa o padrão BGR (Blue, Green, Red)
    img_limpa = np.zeros((img_size, img_size, 3), dtype=np.uint8)
    img_limpa[:, :, 0] = np.random.randint(20, 50)   # Azul baixo
    img_limpa[:, :, 1] = np.random.randint(100, 180) # Verde predominante (Vegetação)
    img_limpa[:, :, 2] = np.random.randint(20, 100)  # Vermelho/Marrom (Terra)
    
    # Adicionando um ruído aleatório para simular a textura do solo
    noise = np.random.randint(-20, 20, (img_size, img_size, 3))
    img_limpa = np.clip(img_limpa + noise, 0, 255).astype(np.uint8)
    
    cv2.imwrite(os.path.join(limpas_dir, f'limpa_{i}.jpg'), img_limpa)

    # --- B. Gerando Imagem "Obstruída" (Simulando nuvens/ruído) ---
    # Copiamos o terreno base para adicionar a obstrução por cima
    img_obstruida = img_limpa.copy()
    
    # Adicionando de 3 a 8 "nuvens" (círculos brancos ou cinza claro)
    num_clouds = np.random.randint(3, 8)
    for _ in range(num_clouds):
        center_x = np.random.randint(0, img_size)
        center_y = np.random.randint(0, img_size)
        radius = np.random.randint(10, 25)
        # Desenhando o círculo: (imagem, centro, raio, cor BGR, espessura -1 preenche tudo)
        cv2.circle(img_obstruida, (center_x, center_y), radius, (240, 240, 240), -1)
        
    cv2.imwrite(os.path.join(obstruidas_dir, f'obstruida_{i}.jpg'), img_obstruida)

print(f"Sucesso! 200 imagens geradas dentro de '{base_dir}'.")