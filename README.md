
# Sticky Notes – Django Application

## Overview
- Sticky notes application built with Django.
- Create, view, update and delete notes.
- SQLite for data storage.
- Includes Sphinx documentation.
- Supports Docker deployment.

## Requirements
- Python 3.10 or later.
- Git.
- Docker Desktop (for container deployment).

## Installation
1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd sticky_notes
   ```

3. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the application:

   ```bash
   python manage.py runserver
   ```

7. Open http://127.0.0.1:8000/ in your browser.

## Configuration Files
- **requirements.txt:** Install Python dependencies.
- **.env:** Create locally and add the Django secret key and environment settings.
- **Dockerfile:** Builds the application container.
- **docker-compose.yml:** Configures and runs the Docker application.
- **.dockerignore:** Excludes unnecessary files from the Docker image.

## Docker Deployment
1. Install and start Docker Desktop.
2. Ensure the Docker configuration files are present.
3. Build the Docker image:

   ```bash
   docker compose build
   ```

4. Start the application:

   ```bash
   docker compose up -d
   ```

5. Access http://localhost:8000/.

## Get Documentation

- Open `docs/_build/html/index.html` in a browser.


