from fastapi import FastAPI

app = FastAPI()

# Создаём маршрут к главной странице:
@app.get("/")
async def get_main_page():
    return {"Главная страница"}

# Создаём маршрут к странице администратора используя параметр в пути:
@app.get("/user/admin")
async def get_admin_page():
    return {"Вы вошли как администратор"}

#Создаём маршрут к страницам пользователей:
@app.get("/user/{user_id}")
async def get_user_number(user_id: int):
    return {f"Вы вошли как пользователь № {user_id}"}

#Создаём маршрут к страницам пользователей передавая данные в адресной строке:
@app.get("/user")
async def get_user_info(username, age: int):
    return {f"Информация о пользователе. Имя: {username}, Возраст {age}."}



