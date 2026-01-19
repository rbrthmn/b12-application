import hmac
import hashlib

class HMACSigner:
    def sign(self, payload: str, secret: str) -> str:
        if not secret:
            raise ValueError("Signing secret cannot be empty.")
            
        return hmac.new(
            key=secret.encode('utf-8'),
            msg=payload.encode('utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()