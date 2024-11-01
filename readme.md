
# Flask REST API Demo

This project demonstrates a simple REST API built with Python's Flask framework. The API performs CRUD (Create, Read, Update, Delete) operations on student data, allowing you to add, retrieve, update, and delete student records.

## Features
- **Retrieve all students**: Fetch a list of all students in the database.
- **Retrieve a specific student by ID**: Fetch details of a single student by their unique ID.
- **Create a new student**: Add a new student to the database.
- **Update an existing student**: Modify details of an existing student by ID.
- **Delete a student**: Remove a student from the database by ID.

## Prerequisites
Before you can run or deploy this app, make sure you have the following installed:
- **Python 3.x**: Required to run the Flask application.
- **pip**: Python's package manager, used to install project dependencies.
- **Flask**: The web framework used in this project (`pip install Flask`).
- **gunicorn**: A production-grade WSGI server (`pip install gunicorn`).
- **Azure CLI** (optional): Needed only if you plan to deploy the app to Azure.

## Project Structure
- **app.py**: Main Flask application file containing all route definitions and CRUD logic.
- **requirements.txt**: Lists all Python dependencies required to run the application.
- **test-api.http**: Contains sample HTTP requests to test the REST API (useful with REST Client extension in VS Code).
- **README.md**: Documentation file explaining setup, configuration, and usage.


## Project Setup

1. Clone the repository:

   git clone https://github.com/KoolestKatEver/rest-api.git

2. Navigate to the project directory:

   cd rest-api

## Environment Configuration

1. Install dependencies needed to run the application 

pip install -r requirements.txt

## Running the Service Locally

1. Start the Flask server:

   python app.py

2. Access the API at http://localhost:8000. Use services like PostMan to test the endpoints.
