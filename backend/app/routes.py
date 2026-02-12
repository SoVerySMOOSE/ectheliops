from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from .session import get_db
from .models import Monitor
from .schemas import MonitorCreate, MonitorUpdate, MonitorOut

router = APIRouter(prefix="/monitors", tags=["monitors"])

@router.post("", response_model=MonitorOut, status_code=status.HTTP_201_CREATED)
def create_monitor(payload: MonitorCreate, db: Session = Depends(get_db)):
    m = Monitor(name=payload.name, url=str(payload.url))
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

@router.get("", response_model=list[MonitorOut])
def list_monitors(db: Session = Depends(get_db)):
    return list(db.scalars(select(Monitor).order_by(Monitor.id.desc())).all())

@router.get("/{monitor_id}", response_model=MonitorOut)
def get_monitor(monitor_id: int, db: Session = Depends(get_db)):
    m = db.get(Monitor, monitor_id)
    if not m:
        raise HTTPException(status_code=404, detail="Monitor not found")
    return m

@router.patch("/{monitor_id}", response_model=MonitorOut)
def update_monitor(monitor_id: int, payload: MonitorUpdate, db: Session = Depends(get_db)):
    m = db.get(Monitor, monitor_id)
    if not m:
        raise HTTPException(status_code=404, detail="Monitor not found")

    if payload.name is not None:
        m.name = payload.name
    if payload.url is not None:
        m.url = str(payload.url)

    db.commit()
    db.refresh(m)
    return m

@router.delete("/{monitor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_monitor(monitor_id: int, db: Session = Depends(get_db)):
    m = db.get(Monitor, monitor_id)
    if not m:
        raise HTTPException(status_code=404, detail="Monitor not found")
    db.delete(m)
    db.commit()
    return None