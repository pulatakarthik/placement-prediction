import joblib
import pandas as pd

# ---------------- Load Model ----------------

model = joblib.load("models/placement_model.pkl")

print("=" * 40)
print("      PLACEMENT PREDICTION")
print("=" * 40)

# ---------------- User Input ----------------

cgpa = float(input("Enter CGPA (0-10): "))
aptitude_score = int(input("Enter Aptitude Score (0-100): "))
internship_experience = int(input("Internship Experience (0 = No, 1 = Yes): "))
projects_completed = int(input("Projects Completed (0-5): "))
active_backlogs = int(input("Active Backlogs (0-3): "))

# ---------------- Create DataFrame ----------------

student = pd.DataFrame([{
    "CGPA": cgpa,
    "Aptitude_score": aptitude_score,
    "internship_experience": internship_experience,
    "projects_completed": projects_completed,
    "active_backlogs": active_backlogs
}])

# ---------------- Predict Probability ----------------

placement_probability = model.predict(student)[0]

# Safety check
placement_probability = max(0, min(placement_probability, 99))

# ---------------- Result ----------------

print("\n" + "=" * 40)
print("RESULT")
print("=" * 40)

print(f"Placement Probability : {placement_probability:.2f}%")

if placement_probability >= 85:
    print("Status : 🌟 Excellent Chance of Placement")

elif placement_probability >= 70:
    print("Status : ✅ High Chance of Placement")

elif placement_probability >= 50:
    print("Status : 🟡 Moderate Chance of Placement")

else:
    print("Status : ❌ Needs Improvement")

print("=" * 40)