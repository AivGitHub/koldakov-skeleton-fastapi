from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.configs import settings
from app.routers.root import router as common_router

app = FastAPI()

# Routers
app.include_router(common_router)

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allow_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
