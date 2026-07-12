def add_doctor(doctors):
    
    n = int(input("How many doctors : "))
    
    for i in range(n):
        d_id = int(input("\nEnter Doctor ID : "))

        if d_id in doctors:
            print("Doctor ID Already Exists")
        else:
            name = input("Enter Doctor Name : ")
            specialist = input("Enter Specialization : ")
            fee = int(input("Enter Consultation Fee : "))

            doctors[d_id] = {
                "name": name,
                "specialist": specialist,
                "fee": fee
            }

            print("\nDoctor Added Successfully")

def view_doctors(doctors):
    
    if doctors:
        
        print("\nDOCTOR DETAILS\n")

        for i in doctors:
            print("Doctor ID :", i)
            print("Doctor Name :", doctors[i]["name"])
            print("Specialist :", doctors[i]["specialist"])
            print("Fee :", doctors[i]["fee"])
            print("-" * 30)

    else:
        print("No Doctors Available")