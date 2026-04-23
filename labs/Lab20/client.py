"""Lab 20: Build the Other Side — Client

Client functions that talk to your FastAPI server. Each task adds
a new function that handles a more realistic scenario.
"""

import requests
import time


def submit(student: str, lab: int, base_url: str = "http://localhost:8000") -> dict:
    """Task 1: Submit a grading request and return the result.

    POST to {base_url}/grade with {"student": student, "lab": lab}.
    Raise RuntimeError if the status code is not 200.
    Return the response as a dictionary.
    """
    # TODO: Implement

    url = f"{base_url}/grade"

    response = requests.post(

        url,

        json = {"student": student, "lab": lab})

    if response.status_code != 200:

        raise RuntimeError(f"Request failed with status code {response.status_code}")

    return response.json()


def submit_with_retry(
    student: str,
    lab: int,
    base_url: str = "http://localhost:8000",
    timeout: float = 2,
    max_retries: int = 3,
) -> dict:
    """Task 2: Submit with timeout and retry logic.

    POST to /grade with {"student": student, "lab": lab, "slow": True}.
    Use the timeout parameter in requests.post().
    On requests.exceptions.Timeout, retry up to max_retries times.
    Raise RuntimeError("all retries failed") if every attempt times out.
    Return the response dictionary on success.
    """
    # TODO: Implement

    url = f"{base_url}/grade"

    data = {

        "student": student,

        "lab": lab,

        "slow": True

    }

    for attempt in range(max_retries):

        try:

            response = requests.post(url, json=data, timeout=timeout)

            if response.status_code != 200:

                raise RuntimeError(f"Request failed with status code {response.status_code}")

            return response.json()

        except requests.exceptions.Timeout:

            if attempt == max_retries - 1:

                raise RuntimeError("all retries failed")
    


def submit_idempotent(
    student: str,
    lab: int,
    base_url: str = "http://localhost:8000",
    timeout: float = 2,
    max_retries: int = 3,
) -> dict:
    """Task 3: Submit with an idempotency key.

    Same as submit_with_retry, but include a stable submission_id
    in the request body: f"{student}-lab{lab}"
    """
    # TODO: Implement

    url = f"{base_url}/grade"

    submission_id = f"{student}-lab{lab}"

    data = {"student": student, "lab": lab, "slow": True, "submission_id": submission_id}

    for attempt in range(max_retries):

        try:

            response = requests.post(url, json=data, timeout=timeout)

            if response.status_code != 200:

                raise RuntimeError(f"Request failed with status code {response.status_code}")

            return response.json()

        except requests.exceptions.Timeout:
            if attempt == max_retries - 1:
                raise RuntimeError("all retries failed")


def submit_async(
    student: str,
    lab: int,
    base_url: str = "http://localhost:8000",
    poll_interval: float = 0.5,
    max_polls: int = 20,
) -> dict:
    """Task 4: Async submission with polling.

    POST to /grade-async with student, lab, and a stable submission_id.
    Expect a 202 response with a job_id.
    Poll GET /grade-jobs/{job_id} every poll_interval seconds.
    When status is "complete", return the result dictionary.
    Raise RuntimeError("polling timed out") if max_polls is exceeded.
    """
    # TODO: Implement

    submission_id = f"{student}-lab{lab}"

    response = requests.post(

        f"{base_url}/grade-async",

        json={"student": student, "lab": lab, "submission_id": submission_id})

    if response.status_code != 202:

        raise RuntimeError(f"Request failed with status code {response.status_code}")

    job_id = response.json()["job_id"]

    for _ in range(max_polls):

        poll_response = requests.get(f"{base_url}/grade-jobs/{job_id}")

        poll_data = poll_response.json()

        if poll_data["status"] == "complete":

            return poll_data["result"]

        time.sleep(poll_interval)

    raise RuntimeError("polling timed out")


# ---------------------------------------------------------------------------
# Bonus Task 5: The Smart Client
# ---------------------------------------------------------------------------


class SmartClient:
    """A client that tries sync first and falls back to async.

    Usage:
        client = SmartClient(base_url="http://localhost:8000")
        result = client.submit("alice", 19)
    """

    def __init__(self, base_url: str = "http://localhost:8000", timeout: float = 2, poll_interval: float = 0.5, max_polls: int = 20, ):

        self.base_url = base_url

        self.timeout = timeout

        self.poll_interval = poll_interval

        self.max_polls = max_polls

    def submit(self, student: str, lab: int) -> dict:
        """Submit a grading request. Tries sync first, falls back to async."""
        # TODO: Implement

        submission_id = f"{student}-lab{lab}"

        try:

            response = requests.post(

                f"{self.base_url}/grade",

                json={"student": student, "lab": lab, "submission_id": submission_id, "slow": True}, timeout=self.timeout)

            if response.status_code == 200:

                return response.json()

            raise RuntimeError(f"Request failed with status code {response.status_code}")

        except requests.exceptions.Timeout:

            async_response = requests.post(

                f"{self.base_url}/grade-async",

                json={"student": student, "lab": lab, "submission_id": submission_id})

            if async_response.status_code != 202:

                raise RuntimeError(f"Request failed with status code {async_response.status_code}")

            job_id = async_response.json()["job_id"]

            for _ in range(self.max_polls):

                poll_response = requests.get(f"{self.base_url}/grade-jobs/{job_id}")

                poll_data = poll_response.json()

                if poll_data["status"] == "complete":

                    return poll_data["result"]

                time.sleep(self.poll_interval)

            raise RuntimeError("polling timed out")
        