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
    # TODO: Implement BMI formula.
    bmi = weight_kg / ( (height_m)*(height_m) )
    return bmi
    pass


def classify_bmi(bmi: float) -> str:
    """Return BMI category."""
    # TODO: Return underweight, normal, overweight, or obese.
    if ( bmi < 18.5):
        return "underweight"
    elif ( bmi  >= 18.5 and bmi <= 24.9):
        return "normal"
    elif (bmi >= 25 and bmi <= 29.9):
        return "overweight"
    else :
        return "obese"
    
    pass


def format_name(name: str) -> str:
    """Convert a name to title case."""
    # TODO: Format name.
    separated_names = name.split()

    titled_names = []

    for word in separated_names:
        titled_name = word[0].upper() + word[1:].lower()
        titled_names.append(titled_name)

    return " ".join(titled_names)

    pass


def get_active_patients(patient_records: list[dict]) -> list[dict]:
    """Return active patients only."""
    # TODO: Filter active patients.
    active_patients = []

    for patient in patient_records:
        if patient["active"] == True:
            active_patients.append(patient)

    return active_patients
            
    pass


def sort_patients_by_weight(patient_records: list[dict]) -> list[dict]:
    """Return patients sorted by weight using a lambda."""
    # TODO: Sort patients by weight_kg.
    data = patient_records.copy()   
    total_items = len(data)

    for i in range(total_items):
        for j in range(total_items - i - 1):

            current_patient = data[j]
            next_patient = data[j + 1]

            if current_patient["weight_kg"] > next_patient["weight_kg"]:

                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

    return data
    pass


if __name__ == "__main__":
    # TODO: Call your functions and print useful output.
    print ( calculate_bmi (58 , 1.6) )
    print ("The BMI falls in " , classify_bmi(15))
    print("Active patients are : ")
    print ( get_active_patients(patients) )
    print ("Name after formating: " ,format_name("ashal meeqaat"))
    print ("Sorted by weights : \n" , sort_patients_by_weight(patients))
    pass
