from tkinter.tix import Form
from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends, Request,Form
from app.config import SessionLocal
from sqlalchemy.orm import Session
from app.schemas import itemSchema
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app import curd


router = APIRouter()
templates=Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

 
@router.post("/summary", response_class=HTMLResponse)
async def submit(request: Request, dictdata: dict, db: Session = Depends(get_db)):
     _items = curd.get_all_items(db)
     TotalCost=0
     for item in _items:
        TotalCost +=item.cost
     return templates.TemplateResponse("summary.html",{"request":request, 'total_cost': TotalCost })

@router.get("/get")
async def get_items(request: Request):
    return templates.TemplateResponse("home.html", {"request":request})