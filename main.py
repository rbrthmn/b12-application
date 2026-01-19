import logging
from submission_data import SubmissionData
from environment_config import EnvironmentConfig
from hmac_signer import HMACSigner
from b12_client import B12Client

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    try:
        config = EnvironmentConfig()
        signer = HMACSigner()
        client = B12Client(signer=signer)

        submission_url = "https://b12.io/apply/submission"
        signing_secret = config.get("B12_SECRET")
        
        submission_data = config.build_submission_data()
        client.submit(url=submission_url, secret=signing_secret, data=submission_data)

    except Exception as e:
        logger.error(f"Fatal error: {e}")
        exit(1)

if __name__ == "__main__":
    main()