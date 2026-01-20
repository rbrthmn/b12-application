import requests
import logging
from typing import Protocol
from submission_data import SubmissionData
from payload_formatter import PayloadFormatter

logger = logging.getLogger(__name__)

class Signer(Protocol):
    def sign(self, payload: str, secret: str) -> str:
        ...

class B12Client:
    def __init__(self, signer: Signer):
        self.signer = signer

    def submit(self, url: str, secret: str, data: SubmissionData) -> None:
        json_payload = PayloadFormatter.to_canonical_json(data)
        signature = self.signer.sign(json_payload, secret)
        
        headers = {
            "Content-Type": "application/json",
            "X-Signature-256": f"sha256={signature}"
        }

        logger.info(f"Submitting payload {data}")
        logger.info(f"To {url}")
        
        try:
            response = requests.post(url, data=json_payload, headers=headers)
            response.raise_for_status()
            logger.info("Submission successful!")
            logger.info(f"Server Response: {response.text}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Submission failed: {e}")
            if 'response' in locals() and response is not None:
                logger.error(f"Response Body: {response.text}")
            raise