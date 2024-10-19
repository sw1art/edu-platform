from fastapi import FastAPI

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Простой endpoint для тестирования
@app.get("/")
def read_root():
    return {"message": "Welcome to User Service"}