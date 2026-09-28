from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Online Grocery Delivery - Cart Service",
    description="Shopping Cart Microservice",
    version="1.0.0"
)


class CartItem(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: float


class Cart(BaseModel):
    id: int
    customer_id: int
    items: List[CartItem]
    total: float


carts = [
    Cart(
        id=1,
        customer_id=1,
        items=[
            CartItem(
                product_id=1,
                product_name="Rice",
                quantity=2,
                price=60.0
            ),
            CartItem(
                product_id=2,
                product_name="Milk",
                quantity=1,
                price=30.0
            )
        ],
        total=150.0
    )
]


@app.get("/")
def home():
    return {
        "service": "Cart Service",
        "status": "running",
        "message": "Online Grocery Delivery Platform"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "cart-service"
    }


@app.get("/carts", response_model=List[Cart])
def get_carts():
    return carts


@app.get("/carts/{cart_id}", response_model=Cart)
def get_cart(cart_id: int):

    for cart in carts:
        if cart.id == cart_id:
            return cart

    raise HTTPException(
        status_code=404,
        detail="Cart not found"
    )


@app.post("/carts", response_model=Cart)
def create_cart(cart: Cart):

    for existing_cart in carts:
        if existing_cart.id == cart.id:
            raise HTTPException(
                status_code=400,
                detail="Cart ID already exists"
            )

    carts.append(cart)

    return cart


@app.put("/carts/{cart_id}", response_model=Cart)
def update_cart(
    cart_id: int,
    updated_cart: Cart
):

    for index, cart in enumerate(carts):

        if cart.id == cart_id:
            carts[index] = updated_cart
            return updated_cart

    raise HTTPException(
        status_code=404,
        detail="Cart not found"
    )


@app.delete("/carts/{cart_id}")
def delete_cart(cart_id: int):

    for index, cart in enumerate(carts):

        if cart.id == cart_id:
            carts.pop(index)

            return {
                "message": "Cart deleted successfully",
                "cart_id": cart_id
            }

    raise HTTPException(
        status_code=404,
        detail="Cart not found"
    )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)