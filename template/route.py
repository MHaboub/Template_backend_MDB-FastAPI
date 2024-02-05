from fastapi import APIRouter, HTTPException
from .model import Todo
from .sercives import Services


router = APIRouter(prefix="/route")

@router.post("/api/todo",response_model=Todo)
async def create_todo(todo: Todo):
    todo1=vars(todo)
    created_Todo = await Services.insert_on("todo",todo1)
    if created_Todo:
        # If the insert operation is successful, return the created todo
        print('sa7a')
        return todo
    else:
        # If the insert operation fails, raise an exception or handle accordingly
        raise HTTPException(500, "Failed to create Todo item")



@router.get("/api/todo/")
async def get_todos():
    response =await Services.fetch_all("todo")
    return response

@router.get("/api/todo/{text}",response_model=Todo)
async def get_todo(text):
    response = await Services.fetch_one("todo",{"text":text})
    if response : 
        return response
    raise HTTPException(404,f"there is no todo item with this email{text}")

@router.put("/api/todo/{text}")
async def put_todo(text:str | None,completed:bool  | None):
    response = await Services.update_document("todo",{"text":text},{"text":text | None, "completed":completed  | None})
    if response : 
        return response
    raise HTTPException(404,f"there is no todo item with this text{text}")


@router.put("/api/todo/{text}")
async def update_all(text:str | None,completed:bool  | None):
    response = await Services.update_document("todo",{"text":text | None, "completed":completed  | None})
    if response : 
        return response
    raise HTTPException(404,f"there is no todo item with this text{text}")


@router.delete("/api/todo/{text}")
async def delete(text):
    res= await Services.remove("todo",{"text":text})
    if res : 
        return "successfully deleted"+text
    raise HTTPException(404,f"there is no todo item with this text: {text}")
