# Blog Application

## Project Overview

This project is developed using Python 3.12.3, Django, and Pillow. It is aimed to accomplish [briefly describe the main functionality or goal of the project].

## Prerequisites

Ensure that you have the following installed:

- Python 3.12.3
- pip (Python Package Installer)

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/jagadeesh-sagar/Blog-cms-using-Django.git
   
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install django pillow
    ```

## Running the Project

1. Apply database migrations:
    ```sh
    python manage.py migrate
    ```

2. Start the development server:
    ```sh
    python manage.py runserver
    ```

3. Open your browser and visit `http://127.0.0.1:8000/` to see the application in action.

## Main Features

- User authentication (login, logout, signup)
- Create, edit, delete blog posts
- Upload images for posts
- Admin interface for managing content
- Category selection for posts

## Technologies Used

- **Django**: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Pillow**: Python Imaging Library (Fork) that adds image processing capabilities to your Python interpreter.

## Contributing

1. Fork the repository
2. Create a new branch for the feature (`git checkout -b feature-xyz`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-xyz`)
5. Create a new Pull Request

