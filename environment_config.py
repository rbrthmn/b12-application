import os
from datetime import datetime, timezone
from submission_data import SubmissionData

class EnvironmentConfig:
    def __init__(self):
        self._env = os.environ

    def get(self, key: str, default: str = None) -> str:
        value = self._env.get(key, default)
        if value is None:
            raise ValueError(f"Missing required environment variable: {key}")
        return value

    def build_submission_data(self) -> SubmissionData:
        server_url = self.get("GITHUB_SERVER_URL", "https://github.com")
        repo = self.get("GITHUB_REPOSITORY", "unknown/repo")
        run_id = self.get("GITHUB_RUN_ID", "0")

        timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z"

        return SubmissionData(
            name=self.get("MY_NAME"),
            email=self.get("MY_EMAIL"),
            resume_link=self.get("MY_RESUME"),
            repository_link=f"{server_url}/{repo}",
            action_run_link=f"{server_url}/{repo}/actions/runs/{run_id}",
            timestamp=timestamp
        )