from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from scripts.services.user_service import 
from scripts.services.product_service import products_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.include_router(users_router)
app.include_router(products_router)
# app.include_router(notes_router,tags=["Notes"])
