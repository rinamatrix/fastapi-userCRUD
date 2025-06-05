# FastAPI MVC App

## Setup

1. Clone this repo
2. Create `.env` file (see `.env` sample)
3. Create a virtual env and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run PostgreSQL and create the database
6. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```
