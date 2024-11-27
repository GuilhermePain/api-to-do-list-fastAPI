from model.user import CreateUser
from repository.user import UserRepository

class UserService:
    @staticmethod
    async def get_all_users_service():
        return await UserRepository.get_all_users()
    
    @staticmethod
    async def get_user_by_id_service(user_id: int):
        return await UserRepository.get_user_by_id(user_id)
    
    @staticmethod
    async def create_user_service(data: CreateUser):
        return await UserRepository.create_user(data)
    
    @staticmethod
    async def update_user_service(user_id: int, data: CreateUser):
        return await UserRepository.update_user(user_id, data)