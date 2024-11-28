from fastapi import HTTPException, status
from model.user import CreateUser
from config.connection import prisma_connection
import logging
import bcrypt

class UserRepository:
    @staticmethod
    async def get_all_users():
        return await prisma_connection.prisma.user.find_many()
    
    @staticmethod
    async def create_user(createUser: CreateUser):
        user = await prisma_connection.prisma.user.find_unique(where={"email": createUser.email})

        if user:
            logging.error("E-mail inválido, tente novamente.")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="E-mail inválido, tente novamente."
            )
        
        hashed_password = bcrypt.hashpw(createUser.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        try:
            return await prisma_connection.prisma.user.create(
                data={
                    "name": createUser.name,
                    "email": createUser.email,
                    "password": hashed_password
                }
            )
        except Exception:
            logging.error("Erro ao cadastrar usuário.")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Erro ao cadastrar usuário."
            )
        
    @staticmethod
    async def get_user_by_id(user_id: int):
        return await prisma_connection.prisma.user.find_first(
            where={"id": user_id}
        )
        
    @staticmethod
    async def update_user(user_id: int, user: CreateUser):
        return await prisma_connection.prisma.user.update(
            where={"id": user_id},
            data={
                "name": user.name,
                "email": user.email,
                "password": user.password
            }
        )
