import openai
import requests

openai.api_key = "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"

imagine = input("PROMPT-:>Imagine: ")

response = requests.post(
    "https://api.openai.com/v1/images/generations",
    headers={"Content-Type": "application/json",
             "Authorization": f"Bearer {openai.api_key}"},
    json={
        # modelo de imagem que será usado, nesse caso é o modelo image-alpha-001
        "model": "image-alpha-001",
        # texto de entrada para o modelo gerar a imagem
        "prompt": imagine,
        "num_images": 1,  # quantidade de imagens que serão geradas
        "size": "1024x1024",  # tamanho da imagem
        "response_format": "url"  # formato de resposta, nesse caso uma URL para a imagem gerada
    },

    timeout=10
)

# Extrai a URL da imagem da resposta JSON
data = response.json()
url = data["data"][0]["url"]

# Baixa a imagem e salva em um arquivo
response = requests.get(url, timeout=10)
with open(f"{imagine}.png", "wb") as f:
    f.write(response.content)
