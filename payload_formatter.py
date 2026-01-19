import json
from dataclasses import asdict
from submission_data import SubmissionData

class PayloadFormatter:
    @staticmethod
    def to_canonical_json(data: SubmissionData) -> str:
        data_dict = asdict(data)
        return json.dumps(data_dict, sort_keys=True, separators=(',', ':'))