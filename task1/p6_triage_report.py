"""
Task 1 — Final Problem: Triage triage_triage_report

Complete this file without using AI tools.
Use fake/sample data only.

Tip: collections.Counter can make counting by risk label easier, but a
plain dictionary works too — import it yourself if you want to use it.
"""

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "risk_score": 72, "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "risk_score": 88, "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "risk_score": 35, "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "risk_score": 91, "active": True},
]


def label_risk(risk_score: int) -> str:
    """Return low, medium, or high based on risk score."""
    # TODO: Define thresholds and return label.
    if risk_score < 0:
        return "invalid"
    elif risk_score < 50:
        return "low"
    elif risk_score >= 50 and risk_score <= 74:
        return "medium"
    elif risk_score >= 75:
        return "high"
    pass


def add_risk_labels(patient_records: list[dict]) -> list[dict]:
    """Return copies of patient records with a risk_label field added."""
    patient_with_risk_label = []

    for patient in patient_records:
        new_patient = patient.copy()

        new_patient["risk_label"] = label_risk(new_patient["risk_score"])

        patient_with_risk_label.append(new_patient)

    return patient_with_risk_label

    # TODO: Add risk labels without modifying original records.
    pass


def build_triage_report(patient_records: list[dict]) -> dict:
    """Build a triage triage_triage_report from patient records."""
    # TODO: Build and return final triage_triage_report.

    labels_of_risk = add_risk_labels(patient_records)

    triage_report = {
        "summary": {"total_patients": len(labels_of_risk)},
        "risk_counts": {"low": 0, "medium": 0, "high": 0},
        "active_high_risk_patients": [],
    }

    for patient in labels_of_risk:
        label = patient["risk_label"]
        triage_report["risk_counts"][label] += 1
        if patient["active"] and label == "high":
            triage_report["active_high_risk_patients"].append(patient)

    return triage_report

    pass


if __name__ == "__main__":
    triage_report = build_triage_report(patients)
    print("Triage report :")
    print(triage_report)
    risk_count = 67
    print("\nThe risk status at ", risk_count, " is: ", label_risk(risk_count))
    print("\nPatient list with risk labels: \n", add_risk_labels(patients))
    # TODO: Add assertions after implementing the functions.
    print("\n\nchecking assertions... ")
    assert label_risk(10) == "Low"
    assert label_risk(50) == "Medium"
    assert label_risk(90) == "High"
    print("Completed ")
