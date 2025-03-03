import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.generate_users import generate_user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://172.28.192.1:3000",  # Ваш текущий адрес
        "http://localhost:3000"      # Для локальной разработки
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get('/contacts')
def contacts():
    users = generate_user(168)
    return users

if __name__ == "__main__":
    uvicorn.run("main:app", port=8888, reload=True)
