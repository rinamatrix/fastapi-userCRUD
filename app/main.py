from fastapi import FastAPI, Depends
from app.routes import user_routes
from app.core.database import Base, engine
from app.core.deps import get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes.router, prefix="/api", tags=["Users"])
