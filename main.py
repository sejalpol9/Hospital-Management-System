# ---------------- HOSPITAL MANAGEMENT SYSTEM ---------------- #
import patient
import doctor
import appointment
import billing

patients = {}
doctors = {}
appointments = {}
billings = {}

# ---------------- LOGIN SYSTEM ---------------- #

username = input("Enter Username : ")
password = input("Enter Password : ")

if username == "admin" and password == "1234":
    print("\nLogin Successful...!")
    
    while True:
        
        print("\n" + "-" * 40)

        print("""
        1. Patient Management
        2. Doctor Management
        3. Appointment Management
        4. Billing
        5. Exit
        """)
        
        choice = int(input("Enter Choice : "))
        
        if choice == 1:
            
            print("""
            1. Patient Registration
            2. View Patients
            3. Search Patient
            4. Update Patient
            5. Delete Patient
            """)

            p_choice = int(input("Enter Choice : "))

            if p_choice == 1:
                patient.add_patient(patients)
            
            elif p_choice == 2:
                patient.view_patients(patients)

            elif p_choice == 3:
                patient.search_patient(patients)

            elif p_choice == 4:
                patient.update_patient(patients)
                
            elif p_choice == 5:
                patient.delete_patient(patients)

            else:
                print("Invalid Choice")

        elif choice == 2:
            
            print("""
            1. Doctor Registration
            2. View Doctors
            """)

            d_choice = int(input("Enter Choice : "))

            if d_choice == 1:
                doctor.add_doctor(doctors)

            elif d_choice == 2:
                doctor.view_doctors(doctors)

            else:
                print("Invalid Choice")

        elif choice == 3:
            appointment.book_appointment(patients, doctors, appointments)

        elif choice == 4:
            billing.generate_bill(appointments, doctors, billings)

        elif choice == 5:
            print("Thank You")
            break

        else:
            print("Invalid Choice")

else:
    print("\nInvalid Username or Password")
