from fastapi import APIRouter, Path
from schema import ResponseSchema
from service.user import UserService
from model.user import CreateUser

router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.get(path="", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_users():
    result = await UserService.get_all_users_service()
    print(result)
    return ResponseSchema(detail="Sucesso ao buscar todos os usuários!", result=result)

@router.get(path="/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_user_by_id(id: int = Path(...)):
    result = await UserService.get_user_by_id_service(id)
    return ResponseSchema(detail="Sucesso ao buscar usuário!", result=result)

@router.post(path="/signup", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_user(create_data: CreateUser):
    await UserService.create_user_service(create_data)
    return ResponseSchema(detail="Sucesso ao criar usuário!")

@router.patch(path="/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_user(update_data: CreateUser, id: int = Path(...)):
    await UserService.update_user_service(id, update_data)
    return ResponseSchema(detail="Sucesso ao editar usuário!")
