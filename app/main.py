from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from httpx import request
from sqlalchemy.orm import Session
from . import models, database, utils
from fastapi.templating import Jinja2Templates
from fastapi import Request, Depends
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
# This creates the actual database file and tables
models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def serve_home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/shorten")
def shorten(url: str, req: Request, db: Session = Depends(database.get_db)):
    try:
        # Create entry
        db_url = models.URL(long_url=url)
        db.add(db_url)
        db.commit()
        db.refresh(db_url)
        
        # Base62 logic
        code = utils.encode_base62(db_url.id)
        db_url.short_code = code
        db.commit()
        
        # Dynamic URL construction
        base_url = str(req.base_url).rstrip("/")
        return {"short_url": f"{base_url}/{code}"}
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": "Internal Server Error"}

@app.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(database.get_db)):
    db_url = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if db_url:
        db_url.clicks += 1
        db.commit()
        return RedirectResponse(url=db_url.long_url)
    raise HTTPException(status_code=404, detail="URL not found")