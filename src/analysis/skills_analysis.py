import json
from pathlib import Path
from collections import Counter

BASE_DIRECTION = Path("../../")
CLEAN_PATH = BASE_DIRECTION / "data" / "processed" / "jobs_cleaned.json"

def load_data():
    with open(CLEAN_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def count_skills(jobs):
    skill_counter = Counter()

    for job in jobs:
        skills = job.get("skills", [])
        skill_counter.update(skills)

    return skill_counter

def get_top_skills(skill_counter, top_n=10):
    return skill_counter.most_common(top_n)

def print_top_skills(top_skills):
    print("\nTop Skills in job market:\n")

    for i, (skill, count) in enumerate(top_skills, start=1):
        print(f"{i}. {skill} ({count})")

def main():
    jobs = load_data()
    skill_counter = count_skills(jobs)
    top_skills = get_top_skills(skill_counter)

    print_top_skills(top_skills)


if __name__ == "__main__":
    main()