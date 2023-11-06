# Django_Store

# Django Store

Django Store is an Amazon clone built using Django, Django Rest Framework, and Javascript. It aims to replicate the core functionality of the popular e-commerce platform and serve as a starting point for building similar online stores.

## Tech Stack

The project utilizes the following technologies and frameworks:

- **Django**: A high-level Python web framework that provides a clean and efficient way to design and develop web applications.
- **Django Rest Framework**: A powerful toolkit for building Web APIs using Django, making it easy to create, test, and deploy RESTful services.
- **Javascript**: A programming language commonly used for adding interactivity and dynamic behavior to web pages.
- **jQuery**: A Javascript library that simplifies HTML document traversal, event handling, and animation.
- **Redis**: An open-source, in-memory data structure store that is used as a cache to improve performance.
- **Celery**: A distributed task queue system that allows for the execution of tasks asynchronously.
- **Chart.js**: A JavaScript library for creating interactive and responsive charts on web pages.
- **Postman**: A popular API development and testing tool used to interact with the Django Rest Framework APIs.
- **HTML**: The standard markup language for creating web pages.
- **CSS**: The style sheet language used for describing the look and formatting of a document written in HTML.

## How to Run

To run the Django Store project locally, follow these steps:

1. Clone the repository using Git or download the ZIP file.

   ````shell
   git clone https://github.com/TahaAlothman/Django_Store.git

2. Navigate to the project directory.

   ````shell
   cd Django_Store

3. Set up a virtual environment (optional but recommended).

   ````shell
   python -m venv env
   source env/bin/activate

4. Install the project dependencies.

   ````shell
   pip install -r requirements.txt

5. Run database migrations.

   ````shell
   python manage.py migrate

6. (Optional) Load dummy data for testing.

   ````shell
   python manage.py loaddata dummy_data.json

7. Start the Django development server.

   ````shell
   python manage.py runserver

8. Open your web browser and visit [http://localhost:8000](http://localhost:8000) to access the Django Store.

   **Note:** The project may require additional configuration, such as setting up a database and configuring Redis. Please refer to the project documentation for detailed instructions.

