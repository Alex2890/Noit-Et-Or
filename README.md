# Noir et Or Restaurant

A modern restaurant website featuring menu display, reservations, and user authentication.

## Project Structure

- **Frontend**: Vue.js 3 with Vue Router and Pinia
- **Backend**: Flask with SQLAlchemy and JWT authentication

## Setup Instructions

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Create environment file:
   ```
   cp .env.example .env
   ```
   
4. Edit `.env` and add your Google OAuth Client ID.

5. Run the development server:
   ```
   npm run dev
   ```

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create environment file:
   ```
   cp .env.example .env
   ```
   
5. Edit `.env` with your configuration settings.

6. Run the development server:
   ```
   python app.py
   ```

## Authentication

The application supports multiple authentication methods:
- Email/Password
- Google OAuth
- Facebook OAuth (planned)

## Features

- User authentication and profile management
- Menu display
- Table reservations
- Private event booking
- Contact information

## Google OAuth Setup

1. Go to the Google Cloud Console
2. Create a new project
3. Configure the OAuth consent screen
4. Create OAuth credentials (Web application type)
5. Add authorized JavaScript origins:
   - http://localhost:5173 (for development)
   - Your production domain (for production)
6. Add authorized redirect URIs:
   - http://localhost:5173 (for development)
   - Your production domain (for production)
7. Copy the Client ID and Client Secret to your .env files

## Database

The application uses SQLite for development and can be configured to use PostgreSQL for production.

## License

[MIT License](LICENSE)