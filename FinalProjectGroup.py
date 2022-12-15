# Assignment: Classes Final Project
# Date Submitted: 15-December-2022
# Authors: John Chernoff, Ali Hussain, Kyle Castillo
# Program Description:
# This program serves as a management system application for Alberta Hospital (AH).
# Allows user to enter data and generate reports.
# Uses the following classes throughout the application:
#  #1 - 	Doctor
#  #2 - 	Facility
#  #3 - 	Laboratory
#  #4 - 	Patient
#  #5 - 	Management

# Class for doctor objects with attributes.
class Doctor:
    # Define the attributes for doctor objects
    def __init__(self, id, name, specialization, working_time, qualification, room_number):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
    # Format doctor info into text strings with the correct format for the text file

    def format_doctor_info(self):
        if self == title:
            self.room_number = 'roomNb'
        doc = self.id + "_" + self.name + "_" + self.specialization + "_" + self.working_time + "_" + self.qualification + "_" + self.room_number
        doc = str(doc)
        return doc
    # Allows user to enter information for new doctor and assigns it to the object

    def enter_doctor_info(self):
        id = str(input("Enter the doctor ID: \n"))
        name = str(input("Enter the doctor Name: \n"))
        spec = str(input("Enter the doctor Specialization: \n"))
        time = str(input("Enter the doctor Working Time: \n"))
        qual = str(input("Enter the doctor Qualification: \n"))
        numb = str(input("Enter the doctor Room Number: \n"))
        self.id = id
        self.name = name
        self.specialization = spec
        self.working_time = time
        self.qualification = qual
        self.room_number = numb
        return self
    # Reads the doctors.txt file and populates the information into objects and attributes

    def read_doctor_file(self):
        with open('doctors.txt', 'r') as f:
            doc = f.read()
            doc = doc.replace("_", " ")
            doc = doc.split()
        if self == title:
            self.id = doc[0]
            self.name = doc[1]
            self.specialization = doc[2]
            self.working_time = doc[3]
            self.qualification = doc[4]
            self.room_number = 'Room Number'
            self.id = self.id.title()
            self.name = self.name.title()
            self.specialization = self.specialization.title()
            self.working_time = self.working_time.title()
            self.qualification = self.qualification.title()
        elif self == doc_1:
            self.id = str(doc[6])
            self.name = doc[7]
            self.specialization = doc[8]
            self.working_time = doc[9]
            self.qualification = doc[10]
            self.room_number = doc[11]
        elif self == doc_2:
            self.id = str(doc[12])
            self.name = doc[13]
            self.specialization = doc[14]
            self.working_time = doc[15]
            self.qualification = doc[16]
            self.room_number = doc[17]
        elif self == doc_3:
            self.id = str(doc[18])
            self.name = doc[19]
            self.specialization = doc[20]
            self.working_time = doc[21]
            self.qualification = doc[22]
            self.room_number = doc[23]
        elif self == doc_4:
            self.id = str(doc[24])
            self.name = doc[25]
            self.specialization = doc[26]
            self.working_time = doc[27]
            self.qualification = doc[28]
            self.room_number = doc[29]
        elif self == doc_5:
            self.id = str(doc[30])
            self.name = doc[31]
            self.specialization = doc[32]
            self.working_time = doc[33]
            self.qualification = doc[34]
            self.room_number = doc[35]
        elif self == doc_6:
            self.id = str(doc[36])
            self.name = doc[37]
            self.specialization = doc[38]
            self.working_time = doc[39]
            self.qualification = doc[40]
            self.room_number = doc[41]
        return self
    # Allows the user to search for a doctor by their ID.

    def search_doctor_by_id(self):
        search_id = str(input("Enter the doctor ID:\n"))
        if doc_1.id == search_id:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_1.id, doc_1.name, doc_1.specialization, doc_1.room_number, doc_1.qualification,
                  doc_1.working_time)
        elif doc_2.id == search_id:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_2.id, doc_2.name, doc_2.specialization, doc_2.room_number, doc_2.qualification,
                  doc_2.working_time)
        elif doc_3.id == search_id:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_3.id, doc_3.name, doc_3.specialization, doc_3.room_number, doc_3.qualification,
                  doc_3.working_time)
        elif doc_4.id == search_id:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_4.id, doc_4.name, doc_4.specialization, doc_4.room_number, doc_4.qualification,
                  doc_4.working_time)
        elif doc_5.id == search_id:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_5.id, doc_5.name, doc_5.specialization, doc_5.room_number, doc_5.qualification,
                  doc_5.working_time)
        elif doc_6.id == search_id:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_6.id, doc_6.name, doc_6.specialization, doc_6.room_number, doc_6.qualification,
                  doc_6.working_time)
        elif doc_7.id == search_id:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_7.id, doc_7.name, doc_7.specialization, doc_7.room_number, doc_7.qualification,
                  doc_7.working_time)
        else:
            print("Sorry no Doctor with that ID exists in the database. Please try again.")
        return self
    # Allows the user to search for a doctor by their name.

    def search_doctor_by_name(self):
        search_name = str(input("Enter the doctor name (Dr.Name):\n"))
        if doc_1.name == search_name:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_1.id, doc_1.name, doc_1.specialization, doc_1.room_number, doc_1.qualification,
                  doc_1.working_time)
        elif doc_2.name == search_name:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_2.id, doc_2.name, doc_2.specialization, doc_2.room_number, doc_2.qualification,
                  doc_2.working_time)
        elif doc_3.name == search_name:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_3.id, doc_3.name, doc_3.specialization, doc_3.room_number, doc_3.qualification,
                  doc_3.working_time)
        elif doc_4.name == search_name:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_4.id, doc_4.name, doc_4.specialization, doc_4.room_number, doc_4.qualification,
                  doc_4.working_time)
        elif doc_5.name == search_name:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_5.id, doc_5.name, doc_5.specialization, doc_5.room_number, doc_5.qualification,
                  doc_5.working_time)
        elif doc_6.name == search_name:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_6.id, doc_6.name, doc_6.specialization, doc_6.room_number, doc_6.qualification,
                  doc_6.working_time)
        elif doc_7.name == search_name:
            print(title.id, title.name, title.specialization, title.room_number, title.qualification,
                  title.working_time)
            print(doc_7.id, doc_7.name, doc_7.specialization, doc_7.room_number, doc_7.qualification,
                  doc_7.working_time)
        else:
            print("Sorry no Doctor with that name exists in the database. Please try again.")
        return self
    # Displays all the doctors information

    def display_doctor_info(self):
        if self == doc_1:
            print(doc_1.id, doc_1.name, doc_1.specialization, doc_1.room_number, doc_1.qualification,
                  doc_1.working_time)
        elif self == doc_2:
            print(doc_2.id, doc_2.name, doc_2.specialization, doc_2.room_number, doc_2.qualification,
                  doc_2.working_time)
        elif self == doc_3:
            print(doc_3.id, doc_3.name, doc_3.specialization, doc_3.room_number, doc_3.qualification,
                  doc_3.working_time)
        elif self == doc_4:
            print(doc_4.id, doc_4.name, doc_4.specialization, doc_4.room_number, doc_4.qualification,
                  doc_4.working_time)
        elif self == doc_5:
            print(doc_5.id, doc_5.name, doc_5.specialization, doc_5.room_number, doc_5.qualification,
                  doc_5.working_time)
        elif self == doc_6:
            print(doc_6.id, doc_6.name, doc_6.specialization, doc_6.room_number, doc_6.qualification,
                  doc_6.working_time)
        elif self == doc_7:
            print(doc_7.id, doc_7.name, doc_7.specialization, doc_7.room_number, doc_7.qualification,
                  doc_7.working_time)
        return self
    # Allows user to edit information for an existing doctor.

    def edit_doctor_info(self):
        search_id = str(input("Enter the id of the doctor that you want to edit their information: \n"))
        if doc_1.id == search_id:
            doc_1.enter_doctor_info()
        elif doc_2.id == search_id:
            doc_2.enter_doctor_info()
        elif doc_3.id == search_id:
            doc_3.enter_doctor_info()
        elif doc_4.id == search_id:
            doc_4.enter_doctor_info()
        elif doc_5.id == search_id:
            doc_5.enter_doctor_info()
        elif doc_6.id == search_id:
            doc_6.enter_doctor_info()
        elif doc_7.id == search_id:
            doc_7.enter_doctor_info()
        else:
            print("Sorry no Doctor with that ID exists in the database. Please try again.")
        return self
    # Displays all doctor attributes.

    def display_doctor_list(self):
        print(title.id, title.name, title.specialization, title.room_number, title.qualification, title.working_time)
        print(doc_1.id, doc_1.name, doc_1.specialization, doc_1.room_number, doc_1.qualification, doc_1.working_time)
        print(doc_2.id, doc_2.name, doc_2.specialization, doc_2.room_number, doc_2.qualification, doc_2.working_time)
        print(doc_3.id, doc_3.name, doc_3.specialization, doc_3.room_number, doc_3.qualification, doc_3.working_time)
        print(doc_4.id, doc_4.name, doc_4.specialization, doc_4.room_number, doc_4.qualification, doc_4.working_time)
        print(doc_5.id, doc_5.name, doc_5.specialization, doc_5.room_number, doc_5.qualification, doc_5.working_time)
        print(doc_6.id, doc_6.name, doc_6.specialization, doc_6.room_number, doc_6.qualification, doc_6.working_time)
        if doc_7.id != '2':
            print(doc_7.id, doc_7.name, doc_7.specialization, doc_7.room_number, doc_7.qualification, doc_7.working_time)
        return self
    # Saves all doctors in the database to the text file.

    def write_list_of_doctors_to_file(self):
        line1 = title.format_doctor_info()
        line2 = doc_1.format_doctor_info()
        line3 = doc_2.format_doctor_info()
        line4 = doc_3.format_doctor_info()
        line5 = doc_4.format_doctor_info()
        line6 = doc_5.format_doctor_info()
        line7 = doc_6.format_doctor_info()
        line8 = doc_7.format_doctor_info()
        with open('doctors.txt', 'r') as r:
            lines = r.readlines()
            lines[0] = line1 + "\n"
            lines[1] = line2 + "\n"
            lines[2] = line3 + "\n"
            lines[3] = line4 + "\n"
            lines[4] = line5 + "\n"
            lines[5] = line6 + "\n"
            lines[6] = line7 + "\n"
            lines[7] = line8
        with open('doctors.txt', 'w') as w:
            for line in lines:
                w.write(line)
        return self
    # Saves one doctor in the database to the text file.

    def add_doctor_to_file(self):
        if self == doc_1:
            line2 = doc_1.format_doctor_info()
        elif self == doc_2:
            line3 = doc_2.format_doctor_info()
        elif self == doc_3:
            line4 = doc_3.format_doctor_info()
        elif self == doc_4:
            line5 = doc_4.format_doctor_info()
        elif self == doc_5:
            line6 = doc_5.format_doctor_info()
        elif self == doc_6:
            line7 = doc_6.format_doctor_info()
        elif self == doc_7:
            line8 = doc_7.format_doctor_info()
        with open('doctors.txt', 'r') as r:
            lines = r.readlines()
            if self == doc_1:
                lines[1] = line2
            elif self == doc_2:
                lines[2] = line3
            elif self == doc_3:
                lines[3] = line4
            elif self == doc_4:
                lines[4] = line5
            elif self == doc_5:
                lines[5] = line6
            elif self == doc_6:
                lines[6] = line7
            elif self == doc_7:
                lines[7] = line8
        with open('doctors.txt', 'w') as w:
            for line in lines:
                w.write(line)
        return self


# Class for facility objects with attributes
class Facility:

    # This method adds and writes
    # the facility name to the file

    def addFacility(self):
        self.newFacility = input(str("Enter Facility name: \n"))
        return self.newFacility
    
    # This method  writes the facilities 
    # list to facilities.txt

    def writeListOfFacilitiesToFile(self):
        with open('facilities.txt', 'a') as newFaci:
            newFaci.write(self.newFacility + "\n")

    # This displays the list
    # of facilities

    def displayFacility(self):
        with open('facilities.txt') as facilities:
            for line in facilities:
               print (line)


# Class for laboratory objects with attributes
class Laboratory:

    # This asks the user to enter the lab name
    # and costs and forms a Laboratory object
    
    def enterLaboratoryInfo(self):
        self.newLabName = input(str("Enter Laboratory facility:\n"))
        self.newLabCost = input("Enter Laboratry cost:\n")

        return self.newLabName, self.newLabCost
    
    # This formats the laboratory object
    # similar to the laboratories.txt 
    # file

    def formatLabInfo(self):
        self.newLab = self.newLabName + '_' + self.newLabCost
        return self.newLab

    # This adds and writes the lab name to the
    # file in the format of the data that
    # is in the file

    def addLabToFile(self):
        self.addLab = self.formatLabInfo()
        return self.addLab

    # This writes the list of labs into
    # the file laboratories.txt
    
    def writeListOfLabsToFile(self):
        with open('laboratories.txt', 'a') as addLabF:
            addLabF.write(self.addLabToFile() + "\n")

    # This displays the list
    # of laboratories
    
    def displayLabsList(self):
        displayLab = self.readLaboratoriesfile()
        return displayLab

    # This reads the laboratories.txt file and fill its 
    # contents in a list of Laboratory objects

    def readLaboratoriesfile(self):
        with open('laboratories.txt', 'r') as LabList:
            lines = LabList.readlines()
            for F, C in enumerate(lines):
                Facility, Cost = C.strip('\n').split('_')
                print(f'{Facility:15}{Cost}')


# Class for patient objects with attributes
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


# Class for management object with no attributes, serves as the menu for all classes.
class Management:
    def display_menu(self):
        print("Welcome to the Alberta Hospital (AH) management system.")
        print("Select from the following options, or select 0 to stop:")
        print("1 - 	Doctors")
        print("2 - 	Facilities")
        print("3 - 	Laboratories")
        print("4 - 	Patients")
        selection = int(input())
        while selection != 0:
            if selection == 1:
                print("Doctors Menu:")
                print("1 - Display Doctors list")
                print("2 - Search for doctor by ID")
                print("3 - Search for doctor by name")
                print("4 - Add doctor")
                print("5 - Edit doctor info")
                print("6 - Back to the Main Menu")
                menu = int(input())
                while menu != 6:
                    if menu == 1:
                        doc_1.display_doctor_list()
                        print("Doctors Menu:")
                        print("1 - Display Doctors list")
                        print("2 - Search for doctor by ID")
                        print("3 - Search for doctor by name")
                        print("4 - Add doctor")
                        print("5 - Edit doctor info")
                        print("6 - Back to the Main Menu")
                        menu = int(input())
                    elif menu == 2:
                        doc_1.search_doctor_by_id()
                        print("Doctors Menu:")
                        print("1 - Display Doctors list")
                        print("2 - Search for doctor by ID")
                        print("3 - Search for doctor by name")
                        print("4 - Add doctor")
                        print("5 - Edit doctor info")
                        print("6 - Back to the Main Menu")
                        menu = int(input())
                    elif menu == 3:
                        doc_1.search_doctor_by_name()
                        print("Doctors Menu:")
                        print("1 - Display Doctors list")
                        print("2 - Search for doctor by ID")
                        print("3 - Search for doctor by name")
                        print("4 - Add doctor")
                        print("5 - Edit doctor info")
                        print("6 - Back to the Main Menu")
                        menu = int(input())
                    elif menu == 4:
                        doc_7.enter_doctor_info()
                        doc_1.write_list_of_doctors_to_file()
                        print("Doctors Menu:")
                        print("1 - Display Doctors list")
                        print("2 - Search for doctor by ID")
                        print("3 - Search for doctor by name")
                        print("4 - Add doctor")
                        print("5 - Edit doctor info")
                        print("6 - Back to the Main Menu")
                        menu = int(input())
                    elif menu == 5:
                        doc_1.edit_doctor_info()
                        doc_1.write_list_of_doctors_to_file()
                        print("Doctors Menu:")
                        print("1 - Display Doctors list")
                        print("2 - Search for doctor by ID")
                        print("3 - Search for doctor by name")
                        print("4 - Add doctor")
                        print("5 - Edit doctor info")
                        print("6 - Back to the Main Menu")
                        menu = int(input())
                selection = 0
                boss.display_menu()
            elif selection == 2:
                print("Facilities Menu:")
                print("1 - Display Facilities List")
                print("2 - Add Facility")
                print("3 - Back to the Main Menu")
                menu = int(input())
                while menu != 3:
                    if menu == 1:
                        facility.displayFacility()
                        print("Facilities Menu:")
                        print("1 - Display Facilities List")
                        print("2 - Add Facility")
                        print("3 - Back to the Main Menu")
                        menu = int(input())
                    elif menu == 2:
                        facility.addFacility()
                        facility.writeListOfFacilitiesToFile()
                        print("Facilities Menu:")
                        print("1 - Display Facilities List")
                        print("2 - Add Facility")
                        print("3 - Back to the Main Menu")
                        menu = int(input())
                selection = 0
                boss.display_menu()
            elif selection == 3:
                print("Laboratories Menu:")
                print("1 - Display Laboratories List")
                print("2 - Add Laboratory")
                print("3 - Back to the Main Menu")
                menu = int(input())
                while menu != 3:
                    if menu == 1:
                        lab.displayLabsList()
                        print("Laboratories Menu:")
                        print("1 - Display Laboratories List")
                        print("2 - Add Laboratory")
                        print("3 - Back to the Main Menu")
                        menu = int(input())
                    elif menu == 2:
                        lab.enterLaboratoryInfo()
                        lab.formatLabInfo()
                        lab.addLabToFile()
                        lab.writeListOfLabsToFile()
                        print("Laboratories Menu:")
                        print("1 - Display Laboratories List")
                        print("2 - Add Laboratory")
                        print("3 - Back to the Main Menu")
                        menu = int(input())
                selection = 0
                boss.display_menu()
            elif selection == 4:
                patient.displayPatientInfo()
                patient.searchPatientbyID()
                patient.addPatientToFile()
                patient.editPatientInfo()
                patient.displayPatientInfo()
                print("Patients Menu:\n"
                             "1 - Display patients list\n"
                             "2 - Search for patient by ID\n"
                             "3 - Add patient\n"
                             "4 - Edit patient info\n"
                             "5 - Back to the Main Menu\n")
                menu = int(input())


# Definitions of initial objects for each class
boss = Management()
title = Doctor('2', '3', '4', '5', '6', '7')
doc_1 = Doctor('2', '3', '4', '5', '6', '7')
doc_2 = Doctor('2', '3', '4', '5', '6', '7')
doc_3 = Doctor('2', '3', '4', '5', '6', '7')
doc_4 = Doctor('2', '3', '4', '5', '6', '7')
doc_5 = Doctor('2', '3', '4', '5', '6', '7')
doc_6 = Doctor('2', '3', '4', '5', '6', '7')
doc_7 = Doctor('2', '3', '4', '5', '6', '7')
facility = Facility()
lab = Laboratory()
patient = Patient()
title.read_doctor_file()
doc_1.read_doctor_file()
doc_2.read_doctor_file()
doc_3.read_doctor_file()
doc_4.read_doctor_file()
doc_5.read_doctor_file()
doc_6.read_doctor_file()

# Initializes program
boss.display_menu()