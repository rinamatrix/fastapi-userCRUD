# FastAPI MVC App using Psql  local Setup process 
1. Clone this repo
2. Create `.env` file
3. Create a virtual env and activate it:  
   python3 -m venv venv
   source venv/bin/activate   ```
4. Install dependencies: 
   pip install -r requirements.txt   
5. Run PostgreSQL and create the database
6. Start the server: 
   uvicorn app.main:app --reload

