# StockFlow API Documentation

## Base URL

http://127.0.0.1:8000/api/


## Products API

### Get All Products

Method: GET

Endpoint:

/api/products/


Purpose:
Returns all inventory products.


## Dashboard API

Method: GET

Endpoint:

/api/dashboard/


Example Response:

{
    "total_products": 2,
    "total_quantity": 22,
    "low_stock_count": 1
}


## Technologies Used

Frontend:
React + Vite

Backend:
Django REST Framework

Database:
SQLite