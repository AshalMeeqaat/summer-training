"""
Task 1 — Patient Summary

Complete this file without using AI tools.
Use fake/sample data only.
"""

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "condition": "diabetes", "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "condition": "hypertension", "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "condition": "asthma", "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "condition": "diabetes", "active": True},
]


def total_patients(patient_records):
    """Return the total number of patients."""
    print("Total patients are : ")
    return len(patient_records)
    # TODO: Implement this function.
    pass


def average_age(patient_records):
    """Return the average patient age."""
    print("Average age is : ")
    sum_age = 0
    for age in patient_records:
        sum_age += age["age"]

    avg_age = sum_age / len(patient_records)
    return avg_age
    # TODO: Implement this function.
    pass


def count_active_patients(patient_records):
    """Return the number of active patients."""
    active_count = 0
    # TODO: Implement this function.
    for active_patients in patient_records:
        if active_patients["active"] == 1:
            active_count += 1

    print("Active patients are: ")
    return active_count
    pass


def unique_conditions(patient_records):
    """Return a sorted list of unique conditions."""
    print("Unique conditions are : ")
    unique_conditions = []

    for conditions in patient_records:
        unique_cond = conditions["condition"]

        if unique_cond not in unique_conditions:
            unique_conditions.append(unique_cond)

    unique_conditions.sort()
    return unique_conditions
    # TODO: Implement this function.
    pass


def count_by_condition(patient_records):
    """Return a dictionary containing patient count by condition."""
    condition_counted_list = {}
    # TODO: Implement this function.
    for conditions in patient_records:
        unique_cond = conditions["condition"]

        if unique_cond in condition_counted_list:
            condition_counted_list[unique_cond] += 1
        else:
            condition_counted_list[unique_cond] = 1

    return condition_counted_list
    pass


if __name__ == "__main__":
    # TODO: Print the summary results clearly.
    print(total_patients(patients))
    print(average_age(patients))
    print(count_active_patients(patients))
    print(unique_conditions(patients))
    print(count_by_condition(patients))
    pass
