import os
import random
import string
from urllib.parse import urljoin, urlparse


async def generate_random_string() -> str:
    characters = string.ascii_letters + string.digits

    return ''.join(random.choices(characters, k=64))

async def create_verification_url() -> str:
    token = await generate_random_string()
    domain = os.environ.get("DOMAIN", "localhost:8000").strip()

    if not urlparse(domain).scheme:
        if "localhost" in domain or "127.0.0.1" in domain:
            domain = f"http://{domain}"
        else:
            domain = f"https://{domain}"

    if not domain.endswith("/"):
        domain += "/"

    path = f"verify?token={token}"
    verification_url = urljoin(domain, path)

    return verification_url
