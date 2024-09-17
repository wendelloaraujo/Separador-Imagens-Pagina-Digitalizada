import cv2
import numpy as np

# Carregar a imagem da página digitalizada que tenha as imagens com contorno para serem extraidas
image = cv2.imread('pagina_2.png')

# Converte para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplica blur para suavizar a imagem e remover ruído
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Aplicar Canny para detectar as bordas
edges = cv2.Canny(blurred, 50, 150)

# Dilatação para conectar áreas desconectadas e remover pequenas imperfeições
kernel = np.ones((5,5), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=2)

# Encontrar contornos
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Definir um tamanho mínimo de área para evitar contornos pequenos, um valor muito baixo pode gerar imagens desnecessárias tipo a captura de uma letra de um documento.
min_area = 50000  # Ajuste conforme necessário para filtrar contornos pequenos

# Iteraa sobre os contornos encontrados
for i, contour in enumerate(contours):
    # Ignora contornos pequenos
    if cv2.contourArea(contour) < min_area:
        continue

    # Obtem a área delimitadora do contorno
    x, y, w, h = cv2.boundingRect(contour)

    # Extrai a região do contorno da imagem original
    doc_image = image[y:y+h, x:x+w]

    # Salvar a imagem separada
    img_path = f'documento_{i+1}.png'
    cv2.imwrite(img_path, doc_image)
    print(f'Imagem salva em: {img_path}')
