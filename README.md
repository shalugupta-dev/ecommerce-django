# E-Commerce Web Application

A web application project built using Python and Django.

## Tech Stack

- **Backend:** Python, Django
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript (verify based on the actual project files)

## Project Structure

- `accounts/` — Account-related application
- `store/` — Store-related application
- `ecommerce/` — Main Django project configuration
- `manage.py` — Django management utility

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/shalugupta-dev/ecommerce-django.git
   cd ecommerce-django
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install project dependencies after creating or obtaining the project's `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your local database settings and credentials.

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open `http://127.0.0.1:8000/` in your browser.

## Author

**Shalu Gupta**

- GitHub: https://github.com/shalugupta-dev
- LinkedIn: https://www.linkedin.com/in/shalu-gupta76
