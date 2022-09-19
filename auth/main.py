from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scripts.services.product_service import product_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)
