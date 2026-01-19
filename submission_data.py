from dataclasses import dataclass

@dataclass
class SubmissionData:
    name: str
    email: str
    resume_link: str
    repository_link: str
    action_run_link: str
    timestamp: str