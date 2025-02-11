# AI Task Planner

An intelligent task management system that uses AI to help users manage tasks, set reminders, and automate email communications.

## Features

- 🤖 AI-powered chat interface for natural language task creation
- 📅 Automated reminder system
- 📧 Email integration for notifications
- 🔄 Daily/weekly task scheduling
- 📚 Learning series email generation
- 🎯 Smart task parsing and categorization

## Tech Stack

### Backend
- Flask (Python web framework)
- SQLAlchemy (ORM)
- OpenAI API (GPT-3.5)
- PostgreSQL (Database)
- Flask-Mail (Email integration)

### Frontend
- React
- Material-UI
- Axios

### Infrastructure
- Docker
- Docker Compose

## Prerequisites

- Docker and Docker Compose
- Node.js (for local development)
- Python 3.9+
- OpenAI API key
- Gmail account (for email notifications)

## Installation

1. Clone the repository:
bash
git clone https://github.com/adit052003/ai-task-planner.git
cd ai-task-planner

2. Create environment files:

Create `.env` in the root directory:
env
OPENAI_API_KEY=your_openai_api_key
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_specific_password
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=taskplanner

3. Build and run with Docker:
bash
docker compose up --build

### Running Locally

Backend:
bash
cd backend
pip install -r requirements.txt
flask run
Frontend:
bash
cd frontend
npm install
npm start
### Database Migrations
## API Endpoints

- `POST /api/chat`: AI chat interface
- `GET /api/test`: Test endpoint
- `GET /tasks`: Get user tasks (requires authentication)

## Environment Variables

### Backend
- `OPENAI_API_KEY`: Your OpenAI API key
- `EMAIL_USER`: Gmail address
- `EMAIL_PASSWORD`: Gmail app-specific password
- `DATABASE_URL`: PostgreSQL connection string

### Frontend
- `REACT_APP_API_URL`: Backend API URL

## Docker Commands

Build and start containers:
## Acknowledgments

- OpenAI for providing the GPT-3.5 API
- Material-UI for the React components
- Flask community for the excellent documentation

