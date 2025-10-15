# Medingen Dev Pancholi

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/Devpancholi04/medingen-dev-pancholi)
[![Default Branch](https://img.shields.io/badge/Branch-main-green?style=flat-square)](https://github.com/Devpancholi04/medingen-dev-pancholi)

## Link for my Self Introduction Video
[![Introduction Video](https://img.shields.io/badge/Watch-Video-red?style=flat-square&logo=youtube)]( link )

## Project Structure

```
medingen-dev-pancholi/
├── images/
├── migrations/
├── routers/
    ├── __init__.py
    ├── api.py
├── .gitignore
├── app.py
├── config.py
└── medingen.sql
├── models.py
├── requirements.txt
├── README.md
```

## Technology Stack
*   **Backend:** 
    *   Python
    *   FastAPI
*   **Database:** 
    *   MySQL

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/Devpancholi04/medingen-dev-pancholi.git
    cd medingen-dev-pancholi
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python app.py
    ```

## API Documentation
The application provides APIs for various functionalities. Here are some of the key endpoints:

*   **User Management:**
    *   `POST /api/register`: Register a new user.
    *   `POST /api/login`: Login for existing users.

*   **Product Management:**
    *   `GET /api/products`: Retrieve a list of products.
    *   `GET /api/products/<product_id>`: Retrieve details of a specific product.

    *   `GET /api/description/<product_id>`: Retrieve description of a specific product.
    *   `GET /api/review/<product_id>`: Retrieve reviews of a specific product.
    *   `GET /api/salt/<product_id>`: Retrieve salt-content of a specific product.
