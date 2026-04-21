import json
from pathlib import Path

RAW_DATA_PATH = Path("../../data/raw/jobs_raw.json")
PROCESSED_DATA_PATH = Path("../../data/processed/jobs_cleaned.json")
KNOWN_SKILLS = ["python", "java", "javascript", "typescript", "sql", "docker",
                "kubernetes", "aws", "azure", "gcp", "react", "angular", "node", "pandas"]


def load_raw_data():
    with open(RAW_DATA_PATH) as file:
        data = json.load(file)
    return data

def inspect_data(data):
    jobs = data["data"]
    print("Total jobs:", len(jobs))
    print("Keys in one job:", jobs[0].keys())


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in KNOWN_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


def transform_job(job):
    description = job.get("description", "")

    skills = extract_skills(description)

    return {
        "title": job.get("title"),
        "company": job.get("company_name"),
        "location": job.get("location"),
        "remote": job.get("remote"),
        "skills": skills,
    }


def process_jobs(data):
    jobs = data["data"]

    cleaned_jobs = []

    for job in jobs:
        cleaned = transform_job(job)
        cleaned_jobs.append(cleaned)

    return cleaned_jobs

def save_clean_data(cleaned_jobs):
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(PROCESSED_DATA_PATH, "w") as file:
        json.dump(cleaned_jobs, file, indent = 2, ensure_ascii = False)

    print(f"Saved cleaned jobs to {PROCESSED_DATA_PATH}")

def main():
    data = load_raw_data()
    inspect_data(data)

    cleaned_jobs = process_jobs(data)

    save_clean_data(cleaned_jobs)

if __name__ == "__main__":
    main()