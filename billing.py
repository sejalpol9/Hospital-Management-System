def generate_bill(appointments, doctors, billings):
    
    p_id = int(input("Enter Patient ID : "))

    if p_id in appointments:
        medicine_fee = int(input("Enter Medicine Fee : "))
        doctor_name = appointments[p_id]["doctor_name"]

        doctor_fee = 0

        for i in doctors:
            if doctors[i]["name"] == doctor_name:
                doctor_fee = doctors[i]["fee"]

        total = doctor_fee + medicine_fee

        billings[p_id] = {
            "doctor_fee": doctor_fee,
            "medicine_fee": medicine_fee,
            "total": total
        }

        print("\n------ BILL ------")
        print("Patient Name :", appointments[p_id]["patient_name"])
        print("Doctor Fee :", doctor_fee)
        print("Medicine Fee :", medicine_fee)
        print("Total Bill :", total)

    else:
        print("Appointment Not Found")


