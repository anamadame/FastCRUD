from fastapi import FastAPI, Depends
from database import SessionLocal, engine
from models import Car, Base
from sqlalchemy.orm import Session
from schema import CarListValidate, CarBetValidate

Base.metadata.create_all(bind=engine)

car_auction = FastAPI(title='Car Auction')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@car_auction.post("/cars/", response_model=CarListValidate)
def create_car(car: CarListValidate, db: Session = Depends(get_db)):
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


@car_auction.get("/cars/{car_id}", response_model=CarListValidate)
def get_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == car_id).first()
    if car is None:
        raise "Product not found"
    return car


@car_auction.put("/cars/{car_id}", response_model=CarListValidate)
def update_car(car_id: int, car: CarListValidate, db: Session = Depends(get_db)):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car is None:
        raise "Product not found"
    for key, value in car.dict().items():
        setattr(db_car, key, value)
    db.commit()
    db.refresh(db_car)
    return db_car


@car_auction.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == car_id).first()
    if car is None:
        raise "Product not found"
    db.delete(car)
    db.commit()
    return "Product deleted successfully"