# Separador de Imagens de Página Digitalizada

Este programa em Python tem como objetivo ler uma página digitalizada que pode conter várias imagens e separá-las automaticamente. Ele utiliza a biblioteca OpenCV para detectar contornos e extrair as imagens encontradas na página.

## Funcionalidades

- Carrega uma página digitalizada em formato de imagem.
- Detecta contornos e separa as áreas que contêm imagens.
- Salva cada imagem separadamente como um arquivo PNG.
- Possui um filtro de tamanho mínimo para evitar a captura de contornos pequenos e irrelevantes, como pedaços de texto.

## Requisitos

Certifique-se de que as seguintes bibliotecas estão instaladas no seu ambiente Python:

- opencv-python
- numpy

### Instalando as dependências

Crie um ambiente virtual e instale as dependências:

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows
venv\Scripts\activate

# No Linux/MacOS
source venv/bin/activate

# Instalar as dependências
pip install opencv-python numpy
```

## Como Usar

1. Coloque a imagem digitalizada (.png) na pasta do projeto.
2. Edite o nome da imagem no código se necessário:

```python
image = cv2.imread('pagina_2.png')
```

3. Execute o script Python:

```bash
python separar_imagens.py
```

4. O programa irá processar a imagem e salvar cada documento ou imagem detectada em arquivos PNG separados no diretório do projeto. Os arquivos terão o nome `documento_X.png`, onde X é o número do contorno detectado.

## Verificação de Nitidez

O repositório também inclui uma função para verificar a nitidez da imagem antes de realizar o processamento. Isso é útil para garantir que a imagem tem qualidade suficiente para ser usada. Consulte o código `detectar_nitidez.py` no repositório para mais detalhes sobre como implementar e usar a função de verificação de nitidez.

## Ajuste de Parâmetros

- `min_area`: O parâmetro `min_area` define o tamanho mínimo para que uma área detectada seja considerada uma imagem válida. Aumente ou diminua este valor conforme necessário, dependendo do tamanho dos documentos que você deseja extrair.
- **Canny e Dilatação**: Se o programa estiver capturando ruídos ou detalhes pequenos, ajuste os parâmetros do detector de bordas (Canny) ou aumente a dilatação.
- `limiar`: O parâmetro `limiar` no cálculo da nitidez determina o valor mínimo para que uma imagem seja considerada nítida. Ajuste este valor conforme necessário para garantir que as imagens processadas tenham qualidade.

## Exemplo de Saída

O programa salva as imagens separadas com nomes como `documento_1.png`, `documento_2.png`, etc., de acordo com os contornos detectados na imagem original.
