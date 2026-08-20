from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="BIBLEMIND",
    version="0.2.0"
)


class Pergunta(BaseModel):
    mensagem: str


@app.get("/")
def inicio():
    return {
        "aplicativo": "BIBLEMIND",
        "versao": "0.2.0",
        "status": "online"
    }


@app.post("/chat")
def chat(pergunta: Pergunta):

    mensagem = pergunta.mensagem.lower()

    if "deus" in mensagem and "nome" in mensagem:
        return {
            "resposta": "Sim. A Bíblia apresenta o nome pessoal de Deus como Jeová.",
            "referencia": "Salmos 83:18"
        }

    if "oracao" in mensagem or "oração" in mensagem:
        return {
            "resposta": "A Bíblia incentiva seus servos a orar regularmente.",
            "referencia": "1 Tessalonicenses 5:17"
        }

    if "esperanca" in mensagem or "esperança" in mensagem:
        return {
            "resposta": "A Bíblia apresenta a esperança como uma expectativa segura baseada nas promessas de Deus.",
            "referencia": "Romanos 15:13"
        }

    return {
        "resposta": "Ainda estou aprendendo a pesquisar esse assunto.",
        "referencia": None
    }
