from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from nitka.app import schemas
from nitka.app.dependencies import get_db
from nitka.app.models import crud
from nitka.app.utils import process_service_config

router = APIRouter()


# ensure the file size is limited by nginx
@router.post("/config/", response_model=schemas.Config)
async def save(file: UploadFile, db: Session = Depends(get_db)):
    content = await file.read()
    try:
        config_info: dict = process_service_config(content)
        return crud.create_config(db, schemas.Config(**config_info))
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Config already exists")
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid config file")


@router.get("/config/", response_model=schemas.Config)
async def get(name: str, db: Session = Depends(get_db)):
    """Get the config by its name (service_name.step_name)"""
    result = crud.get_config(db, name)
    if not result:
        raise HTTPException(status_code=404, detail="Config not found")
    return result
