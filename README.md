# Web Application Project -
## - Session 4 Graded TP -Machine learning in Production
## Overview
This project is a e-commerce web application encompassing backend development, frontend interfaces, and database integration. It's a complete showcase demonstrating the integration of multiple technologies including Docker, comprehensive testing strategies, and CI/CD automation using GitHub Actions.

### Backend Development: 
- Language & Framework: **Python & Django.**
- Responsible for handling business logic, data processing, and server-side operations.

### Frontend Development
-Language & Framework: **CSS&HTML&JAVASCRIPTS**
- Provides a basic but intuitive user interface to interact with the backend.

### Database Integration
- Implementation using **SQLite** 
- Handles data storage and retrieval for backend processes.

### Docker Containers
- Application containerized using Docker for enhanced portability and deployment ease.
- Docker Compose utilized for managing multi-container setups.

### Testing
To do the test, at the root library, run:
    ```pytest```
or
    ```python manage.py test```

- Unit tests for component reliability.
- Integration tests for system cohesiveness.
- End-to-end tests for overall system validation.

### Automation Pipeline

Development workflow automated with **Git Actions**.
Ensures continuous integration and delivery for the project.

### Deployment

Docker images deployed to GitHub Container Registry, enabling easy version control and distribution.


# Setup and Installation
If you would like to use github clone:
        git clone https://github.com/wuqianma2024/e-commerce-CI-CD.git

Or you could choose to pull from docker image:
    docker pull ghcr.io/wuqianma2024/ecommerce-web:v0.1

Then run it:

    cd e-commerce-CI-CD
    docker-compose up --build

After running, access the application from your browser:
    http://localhost:8000






Contributing: WUQIAN MA
