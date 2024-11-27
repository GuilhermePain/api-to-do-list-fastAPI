from model.user import CreateUser
from config.connection import prisma_connection

class UserRepository:
    @staticmethod
    async def get_all_users():
        return await prisma_connection.prisma.user.find_many()
    
    @staticmethod
    async def create_user(createUser: CreateUser):
        return await prisma_connection.prisma.user.create(
            data={
                "name": createUser.name,
                "email": createUser.email,
                "password": createUser.password
            }
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
