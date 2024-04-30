from fastapi import FastAPI
from pydantic import BaseModel
from chat import reponse_chat
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
app = FastAPI()
origins = ["*"]  # Ou spécifiez les origines qu'on souhaite autoriser, par exemple ["http://localhost", "http://127.0.0.1"]

# Ajouter le middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
class Question(BaseModel):
    question: str

@app.post('/myapi')
async def my_api(question: Question):
    reponsee = reponse_chat(question.question)
    return reponsee

if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)