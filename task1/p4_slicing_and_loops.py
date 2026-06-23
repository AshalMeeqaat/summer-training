"""
Task 1 — Slicing and Loops

Practice slicing, loops, enumerate, zip, and comprehensions.
Complete this file without using AI tools.
"""

patient_ids = [101, 102, 103, 104, 105, 106, 107]
patient_names = ["Ayesha", "Omar", "Sara", "Bilal", "Hina", "Usman", "Maha"]


def slicing_examples():
    """Return examples of list slicing."""
    # TODO: Return first three IDs, last three IDs, and reversed IDs.
    
    first_three = []
    first_three = patient_ids[0:3]
    last_three = []
    last_three = patient_ids[-3:]
    reversed_ids = []
    reversed_ids = patient_ids[::-1]
    # return first_three , last_three , reversed
    print ("First three : " , first_three)
    print ("Last Threee: " , last_three)
    print ("Reversed list: " , reversed_ids)
    

    pass


def loop_examples():
    """Practice range, enumerate, and zip."""
    # TODO: Use enumerate to print numbered patient names.
    for index , patient_name in enumerate(patient_names):
        print ( index , patient_name )
    # TODO: Use zip to pair IDs with names.
    for patient_id , patient_name in zip (patient_ids , patient_names) :
        print ( patient_id , patient_name )
    pass


def comprehension_examples():
    """Return values created using comprehensions."""
    # TODO: Create a list of even patient IDs.
    
    # TODO: Create uppercase patient names.
    pass


if __name__ == "__main__":
    slicing_examples()
    loop_examples()
    comprehension_examples()
