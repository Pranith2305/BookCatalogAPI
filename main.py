from fastapi import FastAPI, HTTPException
from typing import List
from model import Book

app = FastAPI()

books_db : List[Book]= []

@app.post('/books', response_model=Book)
def add_books(book : Book):
    for existing_book in books_db:
        if existing_book.id == book.id :
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
        books_db.append(book)
        return book
        

@app.get('/books', response_model=Book)
def get_books():
    return books_db

@app.get('/books/{book_id}', response_model=Book)
def get_book(book_id : int):
    for book in books_db:
        if book.id == books_db:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete('/books/{book_id}')
def del_book(book_id : int):
    for index, book in enumerate(books_db):
        if book.id == book_id :
            del books_db[index]
            return {"Msg" : "Book has been deleted succesfully"}
    raise HTTPException(status_code=404, detail="Book not found")

