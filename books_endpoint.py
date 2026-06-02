from fastapi import FastAPI

app = FastAPI()

@app.get("/books")
def get_books(author: str):
    return {"author": author}