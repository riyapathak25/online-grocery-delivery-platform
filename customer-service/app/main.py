from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Online Grocery Delivery - Customer Service",
    description="Customer Microservice",
    version="1.0.0"
)


class Customer(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str


customers = [
    Customer(
        id=1,
        name="Riya",
        email="riya@example.com",
        phone="9876543210",
        address="Mumbai"
    ),
    Customer(
        id=2,
        name="Amit",
        email="amit@example.com",
        phone="9876543211",
        address="Vasai"
    ),
    Customer(
        id=3,
        name="Priya",
        email="priya@example.com",
        phone="9876543212",
        address="Mira Road"
    )
]


@app.get("/")
def home():
    return {
        "service": "Customer Service",
        "status": "running",
        "message": "Online Grocery Delivery Platform"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "customer-service"
    }


@app.get("/customers", response_model=List[Customer])
def get_customers():
    return customers


@app.get("/customers/{customer_id}", response_model=Customer)
def get_customer(customer_id: int):

    for customer in customers:
        if customer.id == customer_id:
            return customer

    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )


@app.post("/customers", response_model=Customer)
def create_customer(customer: Customer):

    for existing_customer in customers:
        if existing_customer.id == customer.id:
            raise HTTPException(
                status_code=400,
                detail="Customer ID already exists"
            )

    customers.append(customer)

    return customer


@app.put("/customers/{customer_id}", response_model=Customer)
def update_customer(
    customer_id: int,
    updated_customer: Customer
):

    for index, customer in enumerate(customers):

        if customer.id == customer_id:
            customers[index] = updated_customer
            return updated_customer

    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )


@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):

    for index, customer in enumerate(customers):

        if customer.id == customer_id:
            customers.pop(index)

            return {
                "message": "Customer deleted successfully",
                "customer_id": customer_id
            }

    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)