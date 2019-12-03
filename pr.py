import os
from collections import defaultdict  #standard library
from prettytable import PrettyTable


FILE_NAME = "data.txt"


def display_data(data):

    header_list = ["Student ID", "First Name", "Last Name", "Major", "Phone", "GPA", "DOB"]
    t = PrettyTable(header_list) # pip install prettytable(init with header)
    for dt in data:
        t.add_row(dt)
    print(t)


def get_month_from_digit(month):
    if month == 1:
        return 'January'
    if month == 2:
        return 'Feb'
    if month == 3:
        return 'March'
    if month == 4:
        return 'April'
    if month == 5:
        return 'May'
    if month == 6:
        return 'June'
    if month == 7:
        return 'July'
    if month == 8:
        return 'August'
    if month == 9:
        return 'September'
    if month == 10:
        return 'October'
    if month == 11:
        return 'November'
    if month == 12:
        return 'December'



def write_line(the_list, file_name=FILE_NAME):
    mode = "w"
    if os.path.exists(file_name):
        mode = "a"
    fh = open(file_name, mode)
    line = "|".join(str(elm) for elm in the_list)
    fh.write(line + "\n")
    fh.close()


def get_suffix(day):
    suffix = ""
    if day.endswith("1") and (int(day) > 19 or int(day) < 10):
        suffix = "st"
    elif day.endswith("2") and (int(day) > 19 or int(day) < 10):
        suffix = "nd"
    elif day.endswith("3") and (int(day) > 19 or int(day) < 10):
        suffix = "rd"
    else:
        suffix = "th"
    return suffix


def main():
    print("                      Welcome To The Student Management System")
    print("                      ========================================")
    print("")

    while True:
        print("Choose an option from below choices to proceed further")
        print("______________________________________________________")
        print("1 - Enter 1 to Add a new student record")
        print("2 - Enter 2 to Display all student records")
        print("3 - Enter 3 to Sort student records")
        print("4 - Enter 4 to Search student records")
        print("5 - Enter 5 to Edit student records")
        print("6 - Enter 6 to Stop the application!")
        choice = int(input("Enter your choice : ").strip())
        if choice == 6:
            break
        if choice == 1:
            input_data()

        elif choice == 2:
            display_details()

        elif choice == 3:
            sort_data()

        elif choice == 4:
            search_data()


        elif choice == 5:
            edit_data()
        else:
            print("You have selected an option that does not exist, Please try again!")

def input_data():
    print("Enter the student details")
    print("--------------------------")
    fh = open("data.txt")
    lines = fh.readlines()
    fh.close()
    id = input("Enter the Student ID : ").strip()
    file_ids = []
    for line in lines:
        file_id = line.strip().split('|')[0]
        file_ids.append(file_id)
    while id in file_ids:
        id = input("Student id already exist,please enter a valid id: ")
    first_name = input("Enter the First Name : ").strip().capitalize()
    last_name = input("Enter the Last Name : ").strip().capitalize()
    major = input("Enter the Major : ").strip()
    phone = input("Enter the phone : ").strip()
    while len(phone) != 10 or not phone.isdigit():
        phone = input("Invalid phone number,Enter a valid number : ").strip()
    gpa = input("Enter the GPA : ").strip()
    print("Enter the Date Of Birth")
    day = input("Enter the day : ").strip()
    month = input("Enter the month : ").strip()
    while not (1 <= int(month) <= 12):
        month = input("Enter a valid month :").strip()
    month = get_month_from_digit(int(month))

    year = input("Enter the year : ").strip()

    suffix = get_suffix(day)

    dob = "{} {}{}, {}".format(month, day, suffix, year).capitalize()
    line_list = [id, first_name, last_name, major, phone, gpa, dob]
    write_line(line_list)

def display_details():
    fh = open(FILE_NAME)
    lines = fh.readlines()
    fh.close()

    out_list = []
    for line in lines:
        out_list.append(line.strip().split("|"))
    if not len(out_list) < 1:
        display_data(out_list)
    else:
        print("There is no records")
    input("Press Enter to continue ... ")

def sort_data():
    print("Select the field from menu to sort student records")
    print("1 - Enter 1 to sort records by First Name")
    print("2 - Enter 2 to sort records by Last Name")
    print("3 - Enter 3 to sorts records by Major")
    sort_choice = int(input("Enter your sorting choice : ").strip())

    sort_dict = defaultdict(list) # stadr list (initializing sortable dictionary using stard list)
    fh = open(FILE_NAME)
    lines = fh.readlines()
    fh.close()

    if sort_choice == 1:
        for line in lines:
            line_list = line.strip().split("|")
            sort_dict[line_list[1]].append(line_list)
    elif sort_choice == 2:
        for line in lines:
            line_list = line.strip().split("|")
            sort_dict[line_list[2]].append(line_list)
    elif sort_choice == 3:
        for line in lines:
            line_list = line.strip().split("|")
            sort_dict[line_list[3]].append(line_list)

    data_list = []

    for key in sorted(sort_dict):
        item = sort_dict[key]
        for it in item:
            data_list.append(it)
    display_data(data_list)
    input("Press Enter to continue ... ")

def search_data():
    print("Select the field from menu to search student records")
    print("1 - Enter 1 to search records by Student ID")
    print("2 - Enter 2 to search records by Last Name")
    print("3 - Enter 3 to sorts records by Major")
    search_choice = int(input("Enter your sorting choice : ").strip())
    fh = open(FILE_NAME)
    lines = fh.readlines()
    fh.close()

    search_records = []
    if search_choice == 1:
        student_id = input("Enter the Student Id to search student records : ")
        for line in lines:
            if line.strip().split("|")[0] == student_id.strip():
                search_records.append(line.strip().split("|"))
    elif search_choice == 2:
        last_name = input("Enter the Last Name to search student records : ")
        for line in lines:
            if line.strip().split("|")[2].strip() == last_name.strip().capitalize():
                search_records.append(line.strip().split("|"))
    elif search_choice == 3:
        major = input("Enter the Major to search student records : ")
        for line in lines:
            if line.strip().split("|")[3] == major.strip():
                search_records.append(line.strip().split("|"))
    display_data(search_records)
    input("Press Enter to continue ... ")

def edit_data():
    student_id = input("Enter the Student ID to modify the details : ")
    fh = open(FILE_NAME)
    lines = fh.readlines()
    fh.close()
    target_record = []
    target_line = None
    for line in lines:
        if line.strip().split("|")[0] == student_id.strip():
            target_record.append(line.strip().split("|"))
            target_line = line
            break
    print("Below is the record that you have chosen to modify")
    display_data(target_record)
    input("Press Enter to begin the modification ... ")
    student_id = input("Enter new student id, if you don't want to modify just press Enter : ")
    first_name = input("Enter new First Name, if you don't want to modify just press Enter : ")
    last_name = input("Enter new Last Name, if you don't want to modify just press Enter : ")
    major = input("Enter the new Major, if you don't want to modify just press Enter : ")
    gpa = input("Enter the new GPA value, if you don't want to modify just press Enter : ")
    phone = input("Enter the new Phone number, if you don't want to modify just press Enter : ")
    dob = ""
    dob_choice = input("Enter y/Y to modify DOB, if you don't want to modify just press Enter : ")
    if dob_choice.capitalize() == 'Y':
        day = input("Enter Day : ")
        month = input("Enter Month : ")
        year = input("Enter Year : ")
        dob = "{} {}{}, {}".format(month, day, get_suffix(day), year).capitalize()

    input_recod = [student_id.strip(), first_name.strip(), last_name.strip(), major.strip(), gpa.strip(), phone.strip(),
                   dob.strip()]
    target_record = target_record[0]

    for index in range(len(input_recod)):
        if (len(input_recod[index]) > 0) and (input_recod[index] != target_record[index]):
            target_record[index] = input_recod[index]

    fw = open(FILE_NAME, "w")
    for line in lines:
        if line != target_line:
            fw.write(line)
    fw.close()

    write_line(target_record)

main()
