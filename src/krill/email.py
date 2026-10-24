import os

from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import SecretStr
from pydantic.networks import NameEmail

load_dotenv()

config = ConnectionConfig(
    MAIL_USERNAME=os.environ["MAIL_USERNAME"],
    MAIL_PASSWORD=SecretStr(os.environ["MAIL_PASSWORD"]),
    MAIL_FROM=os.environ["MAIL_FROM"],
    MAIL_PORT=int(os.environ.get("MAIL_PORT", "587")),
    MAIL_SERVER=os.environ["MAIL_SERVER"],
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)

mailer = FastMail(config)


async def send_confirmation_email(
    recipient: str,
    confirmation_url: str,
) -> None:
    message = MessageSchema(
        subject="Confirm your application",
        recipients=[NameEmail(name=recipient, email=recipient)],
        body=(
            "Confirm your application by visiting:\n"
            f"{confirmation_url}\n\n"
            "If you did not submit an application, ignore this email."
        ),
        subtype=MessageType.plain,
    )

    await mailer.send_message(message)
