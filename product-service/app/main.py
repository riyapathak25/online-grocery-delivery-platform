from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Online Grocery Delivery - Product Service",
    description="Product Microservice",
    version="1.0.0"
)


class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float
    stock: int
    description: str


products = [
    Product(
        id=1,
        name="Rice",
        category="Grains",
        price=60.0,
        stock=100,
        description="Premium quality rice"
    ),
    Product(
        id=2,
        name="Milk",
        category="Dairy",
        price=30.0,
        stock=50,
        description="Fresh dairy milk"
    ),
    Product(
        id=3,
        name="Apples",
        category="Fruits",
        price=120.0,
        stock=40,
        description="Fresh red apples"
    ),
    Product(
        id=4,
        name="Tomatoes",
        category="Vegetables",
        price=40.0,
        stock=80,
        description="Fresh tomatoes"
    ),
    Product(
        id=5,
        name="Bread",
        category="Bakery",
        price=45.0,
        stock=30,
        description="Fresh white bread"
    )
]


@app.get("/")
def home():
    return {
        "service": "Product Service",
        "status": "running",
        "message": "Online Grocery Delivery Platform"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "product-service"
    }


@app.get("/products", response_model=List[Product])
def get_products():
    return products


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):

    for product in products:
        if product.id == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@app.post("/products", response_model=Product)
def create_product(product: Product):

    for existing_product in products:
        if existing_product.id == product.id:
            raise HTTPException(
                status_code=400,
                detail="Product ID already exists"
            )

    products.append(product)

    return product


@app.put("/products/{product_id}", response_model=Product)
def update_product(
    product_id: int,
    updated_product: Product
):

    for index, product in enumerate(products):

        if product.id == product_id:
            products[index] = updated_product
            return updated_product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    for index, product in enumerate(products):

        if product.id == product_id:
            products.pop(index)

            return {
                "message": "Product deleted successfully",
                "product_id": product_id
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)