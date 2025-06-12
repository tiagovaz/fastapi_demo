from fastapi import APIRouter, Request, Header, HTTPException
import subprocess
import hmac
import hashlib
import os
from dotenv import load_dotenv

router = APIRouter()

load_dotenv()

# Replace with your GitHub webhook secret
GITHUB_SECRET = os.getenv("GITHUB_SECRET")

def verify_signature(payload: bytes, signature: str) -> bool:
    mac = hmac.new(GITHUB_SECRET.encode(), msg=payload, digestmod=hashlib.sha256)
    expected_signature = f"sha256={mac.hexdigest()}"
    return hmac.compare_digest(expected_signature, signature)

@router.post("/webhook")
async def github_webhook(
    request: Request,
    x_hub_signature_256: str = Header(None)
):
    # Pause here and wait for this operation to complete, but don’t block the
    # entire application while waiting
    body = await request.body()

    if not x_hub_signature_256 or not verify_signature(body, x_hub_signature_256):
        raise HTTPException(status_code=403, detail="Invalid signature")

    # Trigger deployment script
    subprocess.Popen(["/home/debian/deploy.sh"])

    return {"message": "Deployment triggered"}
