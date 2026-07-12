"""
Task 1 — Functions and Lambda Functions

Practice reusable functions, type hints, and lambda functions.
Complete this file without using AI tools.
"""

patients = [
    {"name": "ayesha khan", "height_m": 1.65, "weight_kg": 68, "active": True},
    {"name": "omar ali", "height_m": 1.78, "weight_kg": 82, "active": False},
    {"name": "sara ahmed", "height_m": 1.60, "weight_kg": 54, "active": True},
]


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI."""
    bmi = weight_kg / ((height_m) * (height_m))
    return bmi


def classify_bmi(bmi: float) -> str:
    """Return BMI category."""
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


def format_name(name: str) -> str:
    """Convert a name to title case."""
    separated_names = name.split()

    titled_names = []

    for word in separated_names:
        titled_name = word[0].upper() + word[1:].lower()
        titled_names.append(titled_name)

    return " ".join(titled_names)


def get_active_patients(patient_records: list[dict]) -> list[dict]:
    """Return active patients only."""
    active_patients = []

    for patient in patient_records:
        if patient["active"]:
            active_patients.append(patient)

    return active_patients


def sort_patients_by_weight(patient_records: list[dict]) -> list[dict]:
    """Return patients sorted by weight using a lambda."""
    return sorted(patient_records, key=lambda patient: patient["weight_kg"])


if __name__ == "__main__":
    # TODO: Call your functions and print useful output.
    print(calculate_bmi(58, 1.6))
    print("The BMI falls in ", classify_bmi(15))
    print("Active patients are : ")
    print(get_active_patients(patients))
    print("Name after formating: ", format_name("ashal meeqaat"))
    print("Sorted by weights : \n", sort_patients_by_weight(patients))
