import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from config.connection import prisma_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar ao banco de dados na inicialização
    await prisma_connection.connect()
    print("Conexão com o banco de dados iniciada.")
    
    yield  # Aqui o FastAPI executa os endpoints
    
    # Desconectar ao finalizar
    await prisma_connection.disconnect()
    print("Conexão com o banco de dados encerrada.")

app = FastAPI(
    title="To-do List Api",
    description="FastAPI com Prisma",
    version="1.0.0",
    lifespan=lifespan  # Configurando o lifespan
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

from controller import user
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8888, reload=True)
