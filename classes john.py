# Assignment: Classes
# Date Submitted: 09-December-2022
# Authors: John Chernoff
# Program Description:
# This program serves as a management system application for Alberta Hospital (AH).
# Allows user to enter data and generate reports.
# Uses the following classes throughout the application:
#  #1 - 	Doctor
#  #2 - 	Facility
#  #3 - 	Laboratory
#  #4 - 	Patient
#  #5 - 	Management
# This individual component contains classes 1 and 5.


# Class #1: Doctor
class Doctor:
    def __init__(self, id, name, specialization, working_time, qualification, room_number):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def format_doctor_info(self):
        if self == title:
            self.room_number = 'roomNb'
        doc = self.id + "_" + self.name + "_" + self.specialization + "_" + self.working_time + "_" + self.qualification + "_" + self.room_number
        doc = str(doc)
        return doc

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
                print("Facility class goes here.")
            elif selection == 3:
                print("Laboratory class goes here.")
            elif selection == 4:
                print("Patient class goes here.")


boss = Management()
title = Doctor('2', '3', '4', '5', '6', '7')
doc_1 = Doctor('2', '3', '4', '5', '6', '7')
doc_2 = Doctor('2', '3', '4', '5', '6', '7')
doc_3 = Doctor('2', '3', '4', '5', '6', '7')
doc_4 = Doctor('2', '3', '4', '5', '6', '7')
doc_5 = Doctor('2', '3', '4', '5', '6', '7')
doc_6 = Doctor('2', '3', '4', '5', '6', '7')
doc_7 = Doctor('2', '3', '4', '5', '6', '7')
title.read_doctor_file()
doc_1.read_doctor_file()
doc_2.read_doctor_file()
doc_3.read_doctor_file()
doc_4.read_doctor_file()
doc_5.read_doctor_file()
doc_6.read_doctor_file()
boss.display_menu()
