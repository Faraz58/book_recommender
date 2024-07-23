# Book Recommender System

A Book Recommender System built with Django and PostgreSQL that allows users to view and rate books, and get recommendations based on their previous ratings. This project follows clean code principles and uses RESTful APIs for communication.

## Features

1. **Authentication**
   - Users can log in and only authenticated users have access to the API endpoints.

2. **Book Management**
   - Users can view a list of books along with their ratings.

3. **Rating**
   - Users can rate books with a score between 1 and 5.
   - Users can update or delete their ratings.

4. **Filtering**
   - Users can filter books by genre.

5. **Book Recommendation**
   - The system recommends books based on the user's past ratings. If a user has not rated any books, a message "There is not enough data about you" is shown.

## API Endpoints

- **`/api/login`**: User authentication.
- **`/api/book/list/`**: Display the list of books for users.
- **`/api/book/?genre=<genre>`**: Display books filtered by a specific genre.
- **`/api/review/add/`**: Add a rating to a book.
- **`/api/review/update/`**: Update an existing rating for a book.
- **`/api/review/delete/`**: Delete an existing rating for a book.
- **`/api/suggest/`**: Display recommended books for each user.

## Database Schema

### Books Table
| Column  | Type    | Constraints                       |
|---------|---------|-----------------------------------|
| id      | SERIAL  | PRIMARY KEY                       |
| title   | VARCHAR | NOT NULL, UNIQUE with author, genre|
| author  | VARCHAR | NOT NULL, UNIQUE with title, genre |
| genre   | VARCHAR | NOT NULL, UNIQUE with title, author|

### Users Table
| Column   | Type    | Constraints             |
|----------|---------|-------------------------|
| id       | SERIAL  | PRIMARY KEY             |
| username | VARCHAR | NOT NULL, UNIQUE        |
| password | VARCHAR | NOT NULL                |

### Reviews Table
| Column   | Type    | Constraints                           |
|----------|---------|---------------------------------------|
| id       | SERIAL  | PRIMARY KEY                           |
| book_id  | INTEGER | NOT NULL, FOREIGN KEY (books)         |
| user_id  | INTEGER | NOT NULL, FOREIGN KEY (users)         |
| rating   | INTEGER | CHECK (rating >= 1 AND rating <= 5), UNIQUE (book_id, user_id) |

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL

### Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/book_recommender.git
   cd book_recommender
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies:

pip install -r requirements.txt
Configure the database settings in settings.py:
Update the DATABASES setting with your PostgreSQL credentials.

Run migrations:

python manage.py makemigrations
python manage.py migrate
Create a superuser:

python manage.py createsuperuser
Run the server:

python manage.py runserver
Usage
Use an API client like Postman or cURL to interact with the endpoints.
Log in using the /api/login endpoint to get an authentication token.
Use the token to authenticate subsequent requests to other endpoints.
Contributing
Contributions are welcome! Please create a pull request or open an issue to discuss the changes you would like to make.
