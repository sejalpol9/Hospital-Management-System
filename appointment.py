def book_appointment(patients, doctors, appointments):

    p_id = int(input("Enter Patient ID : "))
    d_id = int(input("Enter Doctor ID : "))
    time = input("Enter Appointment Time : ")

    if p_id in patients and d_id in doctors:
        appointments[p_id] = {
            "patient_name": patients[p_id]["name"],
            "doctor_name": doctors[d_id]["name"],
            "time": time
        }

        print("\nAppointment Booked Successfully")

    else:
        print("Invalid Patient ID or Doctor ID")
