import os

from groq import Groq

from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def minha_pergunta_pro_groq(pergunta: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": pergunta,
            }
        ],
        model="llama3-8b-8192",
    )

    return (chat_completion.choices[0].message.content)

pergunta = "Quanto eu vendi ontem?"
resposta = minha_pergunta_pro_groq(pergunta)
print(resposta)