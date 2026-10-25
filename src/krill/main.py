from fastapi import FastAPI

from .application import Application, ConfirmApplication
from .email import send_confirmation_email

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/verify")
async def verify(token: str):
    print(f"received request for {token}")
    return {"message": "Verification successful"}

@app.post("/apply")
async def apply(application: Application):
    print(f"Received application from {application.name} ({application.email} ): {application.description}")
    return {"message": "Application received successfully"}

# this will be removed, its only a testing endpoint.
@app.post("/send-email")
async def send_email(confirmation: ConfirmApplication):
    await send_confirmation_email(confirmation.recipient)
    return {"message": "Email sent successfully"}
