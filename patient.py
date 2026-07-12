def add_patient(patients):
    
    n = int(input("How many patients : "))
    
    for i in range(n):
        p_id = int(input("\nEnter Patient ID : "))

        if p_id in patients:
            print("Patient ID Already Exists")
        else:
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            gender = input("Enter Gender : ")
            disease = input("Enter Disease : ")

            patients[p_id] = {
                "name": name,
                "age": age,
                "gender": gender,
                "disease": disease
            }
        
            print("\nPatient Added Successfully")

def view_patients(patients):
    
    if patients:
        
        print("\nPATIENT DETAILS\n")
        
        for i in patients:
            print("Patient ID :", i)
            print("Name :", patients[i]["name"])
            print("Age :", patients[i]["age"])
            print("Gender :", patients[i]["gender"])
            print("Disease :", patients[i]["disease"])
            print("-" * 30)
      
    else:
        print("No Patients Available")

def search_patient(patients):
    
    search = int(input("Enter Patient ID : "))

    if search in patients:
        print("\nPatient Found")
        print("Name :", patients[search]["name"])
        print("Age :", patients[search]["age"])
        print("Gender :", patients[search]["gender"])
        print("Disease :", patients[search]["disease"])

    else:
        print("Patient Not Found")

def update_patient(patients):
    
    update_id = int(input("Enter Patient ID : "))

    if update_id in patients:
        new_name = input("Enter New Name : ")
        new_age = int(input("Enter New Age : "))
        new_gender = input("Enter New Gender : ")
        new_disease = input("Enter New Disease : ")

        patients[update_id]["name"] = new_name
        patients[update_id]["age"] = new_age
        patients[update_id]["gender"] = new_gender
        patients[update_id]["disease"] = new_disease

        print("Patient Updated Successfully")

    else:
        print("Patient Not Found")

def delete_patient(patients):
    
    delete_id = int(input("Enter Patient ID : "))

    if delete_id in patients:
        del patients[delete_id]
        print("Patient Deleted Successfully")

    else:
        print("Patient Not Found")
