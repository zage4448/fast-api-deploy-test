from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

from loan.loan_router import loan_router
from email_authentication.email_authentication_router import email_authentication_router

app = FastAPI()
load_dotenv()

origins = os.getenv('origins')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(loan_router)
app.include_router(email_authentication_router)
