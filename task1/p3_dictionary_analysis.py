"""
Task 1 — Dictionary Analysis

Practice dictionaries and nested dictionaries.
Complete this file without using AI tools.
"""

patients = {
    1: {
        "name": "Ayesha Khan",
        "age": 32,
        "contact": {"city": "Karachi", "phone": "000-000"},
        "condition": "diabetes",
    },
    2: {
        "name": "Omar Ali",
        "age": 45,
        "contact": {"city": "Lahore", "phone": "111-111"},
        "condition": "hypertension",
    },
}


def get_patient_city(patient_id):
    """Return the city for a given patient ID."""

    
    # TODO: Safely return the city.
    patient = patients.get(patient_id)
    if patient is None :
        return None
    else :
        return patients[patient_id]["contact"]["city"]
    pass


def update_patient_condition(patient_id, new_condition):
    """Update a patient's condition."""
    # TODO: Update the condition for the patient.
    patients[patient_id]["condition"] = new_condition
    return ( patients)
    pass


def build_patient_summary():
    """Build and return a summary dictionary."""
    # TODO: Return useful summary information.
    
    patient_summary = {}

    total_patients = 0
    all_cities = []
    all_conditions = []

    for patient_id in patients:
        patient = patients[patient_id]

        total_patients += 1

        city = patient["contact"]["city"]
        condition = patient["condition"]

        if city not in all_cities:
            all_cities.append(city)

        if condition not in all_conditions:
            all_conditions.append(condition)

    patient_summary["total_patients"] = total_patients
    patient_summary["cities"] = all_cities
    patient_summary["conditions"] = all_conditions
    return patient_summary
    pass


if __name__ == "__main__":
    # TODO: Call your functions and print results.
    print ("City of patient 2: ")
    print ( get_patient_city(2) )
    print ( "After updating condition: ")
    print ( update_patient_condition(1 , "asthma") )
    print ( "Summary: ")
    print (build_patient_summary())
    pass
