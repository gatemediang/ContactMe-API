"""
API Endpoints

This module contains the API endpoints for the application. The endpoints are defined using the FastAPI framework.

Endpoints:
- GET /items/: Retrieve the contact details.

Each endpoint interacts with the database to perform the necessary CRUD operations.

Dependencies:
- FastAPI: The web framework used to create the API.
- SQLAlchemy: The ORM used for database interactions.
- Pydantic: Used for data validation and serialization.

Usage:
1. Start the FastAPI server by running `uvicorn main:app --reload`.
2. Access the API documentation at `http://127.0.0.1:8000/docs`.

Example:
To retrieve an item with ID 1, send a GET request to `http://127.0.0.1:8000/items/1`.

"""