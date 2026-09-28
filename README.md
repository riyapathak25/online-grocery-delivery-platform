\# Online Grocery Delivery Platform



A Cloud Native Online Grocery Delivery Platform built using microservices, Docker, Kubernetes, API Gateway, HPA, ConfigMap, Secrets, monitoring, logging, and GitHub Actions CI/CD.



\## Microservices



\* Product Service - Port 8001

\* Customer Service - Port 8002

\* Cart Service - Port 8003

\* Order Service - Port 8004

\* Delivery Service - Port 8005



\## Technologies



\* Python

\* FastAPI

\* Flask

\* Docker

\* Docker Compose

\* Kubernetes

\* Minikube

\* NGINX API Gateway

\* ConfigMap

\* Kubernetes Secrets

\* Horizontal Pod Autoscaler (HPA)

\* Metrics Server

\* Kubernetes Dashboard

\* GitHub Actions



\## Architecture



Client

→ API Gateway

→ Product / Customer / Cart / Order / Delivery Services



\## Docker Compose



Start all services locally:



```bash

docker compose up --build

```



\## Kubernetes



Start Minikube:



```bash

minikube start --driver=docker

```



Apply Kubernetes configuration:



```bash

kubectl apply -f k8s/

```



Check pods:



```bash

kubectl get pods

```



Check services:



```bash

kubectl get services

```



\## API Gateway



The NGINX API Gateway provides a single entry point for the microservices.



Example:



```text

/product/

/customer/

/cart/

/order/

/delivery/

```



\## HPA



Product Service uses Horizontal Pod Autoscaler.



```text

Minimum replicas: 1

Maximum replicas: 3

CPU target: 70%

```



\## Monitoring



Metrics Server:



```bash

kubectl top pods

```



Kubernetes Dashboard:



```bash

minikube dashboard

```



\## Logging



Example:



```bash

kubectl logs deployment/product-service

kubectl logs deployment/order-service

kubectl logs deployment/api-gateway

```
## Frontend

The project includes a web-based grocery frontend built using:

- HTML
- CSS
- JavaScript
- NGINX

The frontend communicates with the backend through the API Gateway.

### Frontend Flow

Browser
↓
Frontend
↓
NGINX API Gateway
↓
Microservices

### Frontend Features

- Grocery platform home page
- Product service integration
- Customer section
- Cart section
- Order section
- Delivery section
- Responsive user interface

### Frontend Docker

Build:

```bash
docker build -t grocery-frontend:latest ./frontend


\## CI/CD



GitHub Actions automatically builds all five Docker services whenever code is pushed to the `main` branch.



\## GitHub Repository



https://github.com/riyapathak25/online-grocery-delivery-platform



