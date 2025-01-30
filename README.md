
API Endpoints

![docs](https://github.com/user-attachments/assets/929dc3c0-94cf-491b-bcc8-efd50a35ae4e)

This module contains the API endpoints for the application. The endpoints are defined using the FastAPI framework.

Endpoints:
- GET /items/: Retrieve the contact details.

Each endpoint interacts with the database to perform the necessary CRUD operations.

Dependencies:
- FastAPI: The web framework used to create the API.
- SQLAlchemy: The ORM used for database interactions.
- Pydantic: Used for data validation and serialization.
- JSON

Usage:
1. Start the FastAPI server by running `uvicorn main:app --reload`.
2. Access the API documentation at `http://127.0.0.1:8000/docs`.

Example:
To retrieve contact details GET request to `http://127.0.0.1:8000/info`.
