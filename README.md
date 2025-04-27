# 🛒 Advanced Multi-Tenant E-commerce API with Role-Based Access Control (RBAC)

An advanced Django Rest Framework (DRF) based e-commerce backend system supporting multiple vendors, customers, and an admin dashboard, with secure role-based access control and JWT authentication.

---

## 📊 ERD (Entity Relationship Diagram)

![ERD Diagram](path/to/your/erd-image.png)

> This diagram shows the relationships between Users, Vendors, Products, Orders, and OrderItems.

---
## 📑 Postman Documentation
Test all API endpoints easily through the Postman collection:
- 🔗 Postman Collection Download
---

## 🚀 Features

- JWT Authentication (djangorestframework-simplejwt)
- Role-Based Access Control (Admin, Vendor, Customer)
- Vendors manage their own products and view their orders
- Customers can browse products and place orders
- Admins can view/manage everything
- Throttling and Rate Limiting
- Pagination, Search, and Filtering
- Optimized queries (no N+1 problems)
- Django Signals to notify vendors on new orders

---

## 🛠️ Tech Stack

- Python
- Django
- Django Rest Framework (DRF)
- SimpleJWT
- SQLite

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shifat025/ecommerce_task
   cd your-repo-name
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate    # For Windows
   source venv/bin/activate  # For Linux/Mac
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Apply database migrations**
   ```bash
   python manage.py migrate
5. **Apply database migrations**
   ```bash
   python manage.py createsuperuser
6. **Apply database migrations**
   ```bash
   python manage.py runserver
---

## 📚 API Endpoints

### 🔐 Authentication APIs

| Method | Endpoint                   | Description                                 |
|:------:|:----------------------------|:--------------------------------------------|
| <kbd>POST</kbd> | `/user/register/`        | Register a new user (Customer )    |
| <kbd>POST</kbd> | `/vendor/register/`           | Register a new user ( Vendor) |
| <kbd>POST</kbd> | `/user/login`           | Login user (returns some user data, access and refresh token) |
| <kbd>POST</kbd> | `/user/token/`           | Obtain JWT token pair (access and refresh)  |
| <kbd>POST</kbd> | `/user/token/refresh/`   | Refresh the access token                   |

### 🏪 Vendor APIs
| Method | Endpoint                   | Description                                 |
|:------:|:----------------------------|:--------------------------------------------|
| <kbd>POST</kbd> | `/vendor/register/`        | Register a new user (Customer or Vendor)    |
| <kbd>GET</kbd> | `vendor/all/`           | List all registered vendors (Admin access) |
| <kbd>GET</kbd> | `/vendor/get/`           | Retrieve current vendor profile (Vendor access)  |
| <kbd>POST</kbd> | `vendor/get/`   | Retrieve current vendor profile (Vendor access)                   |

### 📦 Product APIs
| Method | Endpoint                   | Description                                 |
|:------:|:----------------------------|:--------------------------------------------|
| <kbd>GET</kbd> | `/products/product/`            | List all products    |
| <kbd>POST</kbd> | `/products/product/`           | Create a new product (Vendor only) |
| <kbd>GET</kbd> | `/products/product/{id}/`       | Retrieve single product details  |
| <kbd>PUT</kbd> | `/products/product/{id}/`       | Update a product (Vendor only)   |
| <kbd>PATCH</kbd> | `/products/product/{id}/`     | Partial update a product (Vendor only)  |
| <kbd>DELETE</kbd> | `/products/product/{id}/`    | Delete a product (Vendor only)  |
| Product Search & Filters |
| <kbd>GET</kbd> | `/products/product/?search={query}`      | Search products by name or description  |
| <kbd>GET</kbd> | `/products/product/?price={min,max}`      | Filter products by price  |
| <kbd>GET</kbd> | `/products/product/?stock={min,max}`      | Filter products by stock |
| <kbd>GET</kbd> | `/products/product/?ordering={field}`      | Order products by field, e.g., 'price' or 'created_at' |


### 🛒 Order APIs
| Method | Endpoint                   | Description                                 |
|:------:|:----------------------------|:--------------------------------------------|
| <kbd>GET</kbd> | `/order/orders/`        | List all orders (Vendor sees orders containing their products, Customer sees their own orders)    |
| <kbd>POST</kbd> | `/order/orders/`           | Place a new order (Customer only) |
| <kbd>GET</kbd> | `/order/orders/{id}/`           | Retrieve a specific order (Vendor/Customer depending on ownership)  |
| <kbd>POST</kbd> | `/order/orders/{id}/`   |Update an order (optional, based on project rules)                 |
| <kbd>POST</kbd> | `/order/orders/{id}/`   | Refresh the access token                   |

---
# ✅ Notes
- All protected endpoints require JWT token in the request headers:
   ```bash 
     Authorization: Bearer <your_access_token>

- Pagination will be applied to lists with large datasets.
- The filter parameters are available for searching and filtering products.
- Vendors can only manage their products and view orders that contain their products.



---

# ⚙️ Advanced Features
- Pagination on list endpoints
- Search & Filter support for products
- Rate limiting and throttling
- Signals for vendor notifications
