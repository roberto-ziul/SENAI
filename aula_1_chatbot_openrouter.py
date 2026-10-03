from google.colab import userdata
import openai

# Configuração da chave do OpenRouter
chave_api = userdata.get('OPENROUTER_API_KEY')

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=chave_api
)

# Definir o modelo a ser utilizado
modelo_ia = "nousresearch/hermes-3-llama-3.1-405b"

while True:
    pergunta = input("\nPergunta: ")
    if pergunta.lower() in ['sair', 'exit']:
        break

    resposta = client.chat.completions.create(
        model=modelo_ia,
        messages=[
            {"role": "user", "content": pergunta}
        ]
    )

    print(resposta.choices[0].message.content)
