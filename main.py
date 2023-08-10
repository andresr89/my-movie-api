from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicacion con Fastapi"
app.version = "0.0.1"

movies = [
   {
      "id":1,
      "overview": "En un planeta donde viven los navi",
      "year": "2090",
      "rating": 7.8,
      "category" : "Accion"
    },

    {
      "id":2,
      "overview": "En un planeta donde viven los navi",
      "year": "2090",
      "rating": 7.8,
      "category" : "Accion"
    }
]


@app.get('/', tags= ['home'])
def message():
    return HTMLResponse ('<h1>hello world</h1>')

@app.get('/movies', tags =['movies'])
def get_movies():
    return movies

@app.get ('/movies/{id}',tags= ['movies'])
def get_movie(id:int):
    for item in movies:
        if item["id"]==id:
            return item
    return []

@app.get ('/movies/', tags = ['movies'])
def get_movies_By_Category(category:str, year :int):
    return [item for item in movies if item['category']==category]

@app.post ('/movies',tags= ['movies'])
def creae_movie(id:int = Body(), title: str= Body(), overview:str= Body(), year: int = Body(), rating: float = Body(), category : str = Body()):
    movies.append({
        "id": id,
        "title":title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category":category
    })
    return movies

@app.put ('/movies/{id}', tags= ['movies'])
def update_movie(id:int , title: str= Body(), overview:str= Body(), year: int = Body(), rating: float = Body(), category : str = Body()):
    for item in movies:
        if item["id"]==id:
            item['title']= title,
            item['overview']= overview,
            item['year']= year,
            item['rating']= rating,
            item['category']= category,
            return movies
            
            
@app.delete ('/movies/{id}', tags= ['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"]==id:
            movies.remove(item)
            return movies