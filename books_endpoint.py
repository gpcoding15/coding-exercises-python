# Ejercicio 3 (10 min)

# Creá este endpoint:

# GET /books?author=Stephen King

# Que devuelva:

# {
#   "author": "Stephen King"
# }

from fastapi import FastAPI

app = FastAPI()

@app.get("/books")
def get_books(author: str):
    return {"author": author}