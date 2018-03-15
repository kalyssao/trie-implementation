import random
from Trie import *
from HashTable import *

#Setting the student directory and hash table as global variables
directory = Trie()
Hash = HashTable()

#A function which adds new students to the directory
#The function also gives the students a slot in the HashTable
#The slot holds the student name and the student ID

def addStudent(Name, yearGroup, directory, Hash):
    directory.addName(Name.lower())
    ID = Hash.generateID(yearGroup)
    Hash.put(Name.lower(), ID)

#A function to verify a password
# The function receives an input and checks it against a prestored value
def checkPassword(user_input):
    password = 'ashes1'
    if user_input == password:
        return True
    else:
        return False

#A function which searches the student directory for the student name
#The function then finds the student name and associated ID in a hash table
def searchDirectory(studentName, directory, Hash):
    searchNames = directory.getNodeOfLastLetter(studentName)
    mylist = []
    directory.findNames(searchNames,studentName, mylist)
    print()

    if mylist != None:
        for i in mylist:
            print('Name :', i, '\nID   :', Hash.get(i))
            print()

#This function requests inputs from the user. Based on the user's input, a student is either
#Added to the directory or a search of students is conducted on the directory.
#Password : ashes1

def accessFunction():
    user_input = input('1. Add new student (Admin Only) \n2. Search for student NB: Start with First Name \
     \n3. Any other number to exit(3-9)\n\n')
    yeargroups = [2021,2020,2019,2018]


    if int(user_input) == 1:
        password = input('\nHello Administrator, enter password:  ')

        if checkPassword(password) == True:
            name = input('\nEnter student name: ')
            yearGroup = input('Enter year group: ')
            if eval(yearGroup) not in yeargroups:
                yearGroup = input('Enter year group, one of the following [2021,2020,2019,2018]: ')
            addStudent(name, yearGroup, directory, Hash)
            print(name, 'has been added to the directory')
            print()
            accessFunction()
        else:
            print('Wrong Password')
            print()
            accessFunction()

    elif int(user_input) == 2:
        studentName = input('Kindly enter student name. NB, feel free to hit enter after typing in the first few letters of the name\n\n')
        print("Searching for ", studentName)
        print()
        searchDirectory(studentName.lower(), directory, Hash)
        accessFunction()
    return

def main():
    #An initial list of tuples made up of the student name and their year groups
    students = [('Edwin Adatsi', 2019), ('Esther Akati', 2020), ('Enam Nanemeh', 2018), ('Philip Asante', 2019),
                ('Kwame Osei Owusu', 2021),('Jojoe Ainoo', 2019),('Kingsley Laryeh',2018), ('Claude Tamakloe',2021),
                ('Samuel Bunyan', 2021), ('Mac Noble', 2019), ('Kusi Berma Asante', 2020)]

    #A text file with student names
    text = open("names.txt", 'r')
    names = text.read().split(',')
    possibleYears = [2021,2020,2019,2018]

    for name in names:
        i = random.randint(0,3)
        students.append((name, possibleYears[i]))


    print("Welcome to the Ashesi Student Directory")
    print("We have ", len(students), "students and we will add them to the student directory.")
    print("The students are: \n")
    count = 1
    for i in students:
        print(count, ' Name: ', i[0], ',   Year Group: ', i[1] )
        count += 1

    for stu in students:
        addStudent(stu[0], stu[1], directory, Hash)
    print('\nStudents have been successfully added to the student directory.')

    print()
    print('Student Directory: ')
    accessFunction()

if __name__ == '__main__':
    main()