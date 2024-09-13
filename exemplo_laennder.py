import streamlit as st
import time
from openai import OpenAI
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Configuração da API e do ID do Assistente # asst_bWjV0p7J0MUiSt8nbl4TuMhG
ASSISTANT_ID = "asst_mc4rruoiYRzd7KYmDaQQIzGb"
client = OpenAI(api_key=os.getenv("YOUR_OPENAI_API_KEY"))

# Função para enviar a pergunta ao assistente e obter a resposta
def responder_pergunta(pergunta):
    # Cria um novo thread com a mensagem do usuário

    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": f"hoje é dia {datetime.now()} {pergunta}",  # A pergunta do usuário é enviada diretamente
            }
        ]
    )

    # Envia o thread para o assistente (como uma nova execução)
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
    st.write(f"👉 Conversa id: {run.id}")

    # Aguarda a conclusão da execução
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        st.write(f"🏃 Run Status: {run.status}")
        time.sleep(1)

    st.write(f"🏁 Run Completed!")

    # Obtém a última mensagem do thread
    message_response = client.beta.threads.messages.list(thread_id=thread.id)
    messages = message_response.data

    # Extrai e retorna a resposta mais recente
    latest_message = messages[0]
    return latest_message.content[0].text.value.strip()

# Interface do Streamlit
st.title("Agente de Atendimento - Pergunte ao Assistente")

# Caixa de entrada para perguntas
pergunta = st.text_input("Digite sua pergunta:")

# Quando uma pergunta é feita, envia para o assistente e exibe a resposta
if pergunta:
    resposta = responder_pergunta(pergunta)
    st.write(f"💬 Resposta: {resposta}")
