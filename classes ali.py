#Project Classes - Ali Hussain


class Patient:
    def searchPatientbyID(self):
        file2 = open('patients.txt', 'r')
        patient_id = input("Enter the Patient Id:")
        id_dict = {}
        id_list = []
        for line in file2:
            key_id = line[:2]
            id_dict[key_id] = line
            id_list.append(line[:2])
        if patient_id in id_list:
            print(id_dict[patient_id].replace('_', ' '))
        else:
            print("Can't find the Patient with the same id on the system")
        file2.close()

    def enterPatientInfo(self):
        new_patient_info = []
        print("Enter Patient ID:")
        new_id = input("")
        print("Enter Patient name:")
        new_name = input("")
        print("Enter Patient disease:")
        new_disease = input("")
        print("Enter Patient gender:")
        new_gender = input("")
        print("Enter Patient age:")
        new_age = input("")
        new_patient_info.append(new_id)
        new_patient_info.append(new_name)
        new_patient_info.append(new_disease)
        new_patient_info.append(new_gender)
        new_patient_info.append(new_age)
        patient_str = "_".join(new_patient_info)
        return patient_str

    def enterPatientEdit(self, patient_id):
        new_patient_info = []
        print("Enter new patient name:")
        new_name = input("")
        print("Enter new patient disease:")
        new_disease = input("")
        print("Enter new patient gender:")
        new_gender = input("")
        print("Enter new patient age:")
        new_age = input("")
        new_patient_info.append(patient_id)
        new_patient_info.append(new_name)
        new_patient_info.append(new_disease)
        new_patient_info.append(new_gender)
        new_patient_info.append(new_age + "\n")
        patient_str = "_".join(new_patient_info)
        return patient_str

    def formatPatientInfo(self, new_patient_info):
        file2 = open('patients.txt', 'r')
        patient_info = []
        for line in file2:
            patient_info.append(line)
        patient_info[-1] = patient_info[-1] + "\n"
        patient_info.append(new_patient_info)
        file2.close
        return patient_info




    def addPatientToFile(self):
        new_patient_info = self.enterPatientInfo()
        patient_info = self.formatPatientInfo(new_patient_info)
        print(patient_info)
        self.writeListOfPatientsToFile(patient_info)


    def writeListOfPatientsToFile(self, patient_info):
        file2 = open('patients.txt', 'w')
        for x in patient_info:
            file2.write(x)
        file2.close()

    def readPatientFile(self):
        file2 = open('patients.txt', 'r')
        patient_list = []
        for line in file2:
            patient_list.append((str(line.replace('_', ' ')).replace('id', 'ID')))
        file2.close()
        return patient_list


    def editPatientInfo(self):
        file2 = open('patients.txt', mode='r')
        print("Enter the Patient Id:")
        patient_id = input("")
        id_dict = {}
        id_list = []
        patient_list = []
        for line in file2:
            key_id = line[:2]
            id_dict[key_id] = line
            id_list.append(line[:2])

        if patient_id in id_list:
            new_patient_info = self.enterPatientEdit(patient_id)
            patient_info = "".join(new_patient_info)
            patient_info.replace(" ", "_")
            id_dict[patient_id] = patient_info
            dict_keys = id_dict.keys()
            for x in dict_keys:
                patient_list.append(id_dict[x])
        else:
            print("Can't find the Patient with the same id on the system")
        print(patient_list)
        file2.close()
        self.writeListOfPatientsToFile(patient_list)
        file2.close()

    def displayPatientInfo(self):
        patient_list = self.readPatientFile()
        for x in patient_list:
            print(x)
        pass






print("Welcome to Alberta Hospital (AH) Managment system\n Select from the following options, or select 0 to stop:\n"
      "1 - 	Doctors\n"
      "2 - 	Facilities\n"
      "3 - 	Laboratories\n"
      "4 - 	Patients\n")
user_input = input("")
active = True
while active:
    if user_input == "1":
        pass
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        patientMenu = (input("Patients Menu:\n"
                             "1 - Display patients list\n"
                             "2 - Search for patient by ID\n"
                             "3 - Add patient\n"
                             "4 - Edit patient info\n"
                             "5 - Back to the Main Menu\n"))
        if patientMenu == "1":
            Patient().displayPatientInfo()
            print('Back to previous menu')

        elif patientMenu == "2":
            Patient().searchPatientbyID()
            print('Back to previous menu')

        elif patientMenu == "3":
            Patient().addPatientToFile()
            print('Back to previous menu')

        elif patientMenu == "4":
            Patient().editPatientInfo()
            Patient().writeListOfPatientsToFile()
        elif patientMenu == "5":
            print('Back to the Main Menu')
