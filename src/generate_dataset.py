import pandas as pd
import random

students = []

for i in range(5000):

    # ---------------- CGPA ----------------
    cgpa = round(random.uniform(5.0, 10.0), 2)

    # ---------------- Aptitude ----------------
    if cgpa >= 9:
        aptitude_score = random.randint(85, 100)
    elif cgpa >= 8:
        aptitude_score = random.randint(75, 95)
    elif cgpa >= 7:
        aptitude_score = random.randint(65, 85)
    elif cgpa >= 6:
        aptitude_score = random.randint(50, 75)
    else:
        aptitude_score = random.randint(40, 65)

    # ---------------- Internship ----------------
    if cgpa >= 9:
        internship_experience = 1 if random.random() < 0.8 else 0
    elif cgpa >= 8:
        internship_experience = 1 if random.random() < 0.6 else 0
    elif cgpa >= 7:
        internship_experience = 1 if random.random() < 0.4 else 0
    elif cgpa >= 6:
        internship_experience = 1 if random.random() < 0.2 else 0
    else:
        internship_experience = 1 if random.random() < 0.1 else 0

    # ---------------- Projects ----------------
    if internship_experience == 1:
        if cgpa >= 9:
            projects_completed = random.randint(4, 5)
        elif cgpa >= 8:
            projects_completed = random.randint(3, 5)
        elif cgpa >= 7:
            projects_completed = random.randint(2, 4)
        else:
            projects_completed = random.randint(1, 3)
    else:
        if cgpa >= 9:
            projects_completed = random.randint(3, 4)
        elif cgpa >= 8:
            projects_completed = random.randint(2, 4)
        elif cgpa >= 7:
            projects_completed = random.randint(1, 3)
        else:
            projects_completed = random.randint(0, 2)

    # ---------------- Backlogs ----------------
    if cgpa >= 9:
        active_backlogs = random.randint(0, 0)
    elif cgpa >= 8:
        active_backlogs = random.randint(0, 1)
    elif cgpa >= 7:
        active_backlogs = random.randint(0, 2)
    elif cgpa >= 6:
        active_backlogs = random.randint(0, 3)
    else:
        active_backlogs = random.randint(1, 3)

    # ---------------- Placement Probability ----------------

    cgpa_score = (cgpa / 10) * 35

    aptitude_points = (aptitude_score / 100) * 30

    internship_points = 20 if internship_experience == 1 else 0

    projects_points = projects_completed * 4

    backlog_penalty = active_backlogs * 10

    variation = random.randint(-3, 3)

    placement_probability = (
        cgpa_score
        + aptitude_points
        + internship_points
        + projects_points
        - backlog_penalty
        + variation
    )

    # Keep probability between 0 and 99
    placement_probability = max(0, min(placement_probability, 99))

    students.append({
        "CGPA": cgpa,
        "Aptitude_score": aptitude_score,
        "internship_experience": internship_experience,
        "projects_completed": projects_completed,
        "active_backlogs": active_backlogs,
        "placement_probability": round(placement_probability, 2)
    })

df = pd.DataFrame(students)

print(df.head())

print(df.shape)

df.to_csv("data/placement_data.csv", index=False)

print("\nDataset generated successfully!")