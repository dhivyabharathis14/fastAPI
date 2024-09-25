from fastapi import FastAPI
from models import User,Gender,Roles
from uuid import UUID, uuid4

app=FastAPI()

db = [
    User(
    id = uuid4(),
    first_name= "Dhivya",
    last_name= "Bharathi",
    gender=Gender.female,
    roles= Roles.user,
    )
]

@app.get("/")
def root():
    return {"Hello" "world"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_users(user: User):
     db.append(user) 
     return {"id" : user.id}  

@app.delete("/api/v1/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return