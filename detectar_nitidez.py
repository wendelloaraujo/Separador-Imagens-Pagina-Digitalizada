import cv2

def calcular_nitidez(image_path, limiar=100.0):
    # Carregar a imagem em escala de cinza
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Verificar se a imagem foi carregada corretamente
    if image is None:
        raise ValueError(f"Não foi possível carregar a imagem: {image_path}")

    # Aplicar o operador Laplaciano para calcular a nitidez
    laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()

    # Avaliar se a imagem é nítida ou borrada
    if laplacian_var < limiar:
        return False, laplacian_var  # Imagem borrada (baixa nitidez)
    else:
        return True, laplacian_var  # Imagem nítida

# Exemplo de uso
imagem = 'pagina.jpg'
resultado, nitidez = calcular_nitidez(imagem)

if resultado:
    print(f'A imagem está com boa qualidade. Nitidez: {nitidez:.2f}')
else:
    print(f'A imagem está com baixa qualidade. Nitidez: {nitidez:.2f}')
