# Django JWT Authentication Project

This Django Rest Framework project offers robust JWT-based authentication with features such as user registration, secure login, profile access, and the convenience of email-based password reset. Additionally, it enhances the user experience by implementing login sessions, and to facilitate testing and integration, an API collection is provided for seamless interaction via Postman. Discover a comprehensive solution for user management and authentication within your Django application.

## Features

- **JWT Authentication:** Secure and efficient authentication using JSON Web Tokens.
- **User Registration:** User-friendly registration process.
- **User Login:** Secure and straightforward login mechanism.
- **Profile Access:** User profile management and access.
- **Password Reset:** Reset passwords via email confirmation.
- **Login Sessions:** Enhanced user experience with login sessions.
- **API Collection:** A Postman collection for convenient API testing and integration.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (3.6+)
- Django (3.0+)
- Django Rest Framework
- Postman (for API calling)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/kapil-malviya/JWT-Authentication-DRF/
   cd JWT-Authentication-DRF
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Navigate to the project level directory:
   ```
   cd authapi1
   ```

4. Perform initial database migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Access the admin interface and API collection for testing.

## Usage

- Access the admin interface at `http://localhost:8000/admin/` to manage users and view logs.
- Use the Postman API collection for testing the API endpoints.
- For more detailed API usage,refer the Postman documentation.

## Contributing

We welcome contributions to enhance and expand this project. Feel free to open issues or submit pull requests to improve the project's functionality and codebase.

