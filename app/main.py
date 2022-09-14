from fastapi import FastAPI, Request
from app import models
from app.routes import router
from app.config import engine
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static",StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory='templates')

app.include_router(router, prefix="/items", tags=["items"])


	