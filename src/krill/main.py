from fastapi import FastAPI

from .email import send_confirmation_email

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/send-email")
async def send_email(recipient: str, confirmation_url: str):
    await send_confirmation_email(recipient, confirmation_url)
    return {"message": "Email sent successfully"}
