from fastapi import APIRouter
from typing import List
from models.Customer import Customer

router = APIRouter(prefix="/customers")

customers: List[Customer] = []


@router.get("/")
def get_customers():
    return {"customers": customers}


@router.post("/")
def create_customer(customer: Customer):
    customers.append(customer)
    print(customers)
    return {"customers": customers}
