# Paola Lopez-Piety
# 12/13/2021
# PROG 108
# Final Project: Human Mission to Mars Account Setup system


import csv
import random
import string
from tabulate import tabulate

def display_menu():
    print("Human Mission to Mars Account Setup system")
    print()
    print("COMMAND MENU")
    print("add   - Add a new account")
    print("list  - List all accounts")
    print("find  - Find accounts by last name")
    print("pods  - List living pods")
    print("admin - Administrator report")
    print("del   - Delete account")
    print("exit  - Exit program")
    print()    


#create a filenamefor our .csv file
filename = "accounts.csv"

#create function that save the info in the cvs.file
def write_account(account):
  with open(filename, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(account)

#get the data
def read_accounts():
  accounts = []
  
  with open(filename, newline="") as file:
    reader = csv.reader(file)
    for row in reader:
      accounts.append(row)
  return accounts

# Create a function to add a new human account using inputs. (10 points)

def new_account(accounts, living_array):
  firstname = input("Enter first name: ").capitalize() 
  while len(firstname.strip()) == 0:
    firstname = input("Try Again. Enter first name: ").capitalize() 

  lastname = input("Enter last name: ").capitalize() 
  while len(lastname.strip()) == 0:
    lastname = input("Try Again. Enter last name: ").capitalize() 
  
  #id number - this should be a system-generated number between 1000 and 9999
  ID_number = random.randint(1000, 9999)
  email = (firstname + lastname + str(ID_number) + "@mars.com").lower()

  #password - create a randomly generated secure password consisting of at least 8 characters, a special character, a number, and a combination of lower and uppercase letters.
  
  random_pw = string.ascii_letters 
  # select 1 lowercase
  password = random.choice(string.ascii_lowercase)
  # select 1 uppercase
  password += random.choice(string.ascii_uppercase)
  # select 1 digit
  password += random.choice(string.digits)
  # select 1 special symbol
  password += random.choice(string.punctuation)

  # generate other characters
  for i in range(4):
    password += random.choice(random_pw)

  password_list = list(password)
  # shuffle all characters
  random.SystemRandom().shuffle(password_list)
  password = ''.join(password_list)
  

  age = input("Enter age: ")
  age_numeric = age.isnumeric()

  while age_numeric != True:
    print("Try again")
    age = input("Enter age: ")
    age_numeric = age.isnumeric()

  
  gender = input("Enter gender(F/M): ").upper()
  while gender.upper() != "F"  and gender.upper() != "M":
    gender = input("Please try again (F/M): ").upper()


  #living pod room number - system generated living pod room number assignment - this can be formatted however you want but I recommend that you come up with something like Building A - 8 slots 1, 2, 3, 4, 5, 6, 7 and 8 and so on. Assume a maximum of 20-30 humans living on this Mars mission.

  living_array = living_array

  if len(living_array) != 0: 
    if len(living_array[0]) == 0:
        living_array.pop(0)
    elif len(living_array[1]) == 0:
        living_array.pop(1)

    living_pod = ""
    exists = True
    while exists == True:
          
      # Randomly selects building
        
      b = random.randint(0, len(living_array)-1)
      building = living_array[b]
          
      #Randomly select room
      r = random.randint(0, len(building)-1)
      room = building[r]
      living_pod = str(room)

      building.pop(r)

      exists = living_pod in [item for sublist in accounts for item in sublist]


  return firstname, lastname, ID_number, email, password, age, gender, living_pod


# Create a function to list all human's names, their email addresses, age, gender, and their designated living pod room number. (5 points)

def read_list(accounts):

  all_humans = []
  
  i = 1
  for row in accounts: 

    fullName = row[0] + " "+row[1]
    human = [i, fullName, row[3], row[5], row[6], row[7]]
    i += 1
    all_humans.append(human)

  print(tabulate(all_humans, headers=["Index","Full Name", "Email", "Age", "Gender", "Living Pod"]))    
      



# Create a search function to search for a human by last name. Then list all of the matches of the last name, first name, and their designated living pod room number. (10 points)

def search_lastName(accounts):
  search_lastName =input("Enter the last name you are looking for: ").capitalize()
  print()

  #List for the matches
  searches = []
  #for loop for every match and it is going to the searches list 
  for i, x in enumerate(accounts):
    if search_lastName in x:
      searches.append(accounts[i]) 
  
  if len(searches) == 0:
    print("No results found!")
  else: 
    match = []

    for row in searches: 
      search= [row[0], row[1], row[7]]
      match.append(search)


    print(tabulate(match, headers=["First Name", "Last Name", "Living Pod"]))    
      
  print()   
   
    
# Create a living pod search that shows how many humans are assigned to each pod and how many spaces are still available. (10 points)

def search_living_pod(accounts):
  #Original slots 
  original_living_array = [
              ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10"], #"Building A, 10 Slots"
              ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10"]] #"Building B, 10 Slots"
  rows_accounts=len(accounts) #finding the max number of rows in accounts 
  columns_accounts=len(accounts[0]) #finding the max number of columns in accounts

  len_Building_A = len(original_living_array[0])
  len_Building_B = len(original_living_array[1])

  #define new array for slots taken
  slots_taken = []

  #count the number of slots taken on each building
  slots_ocuppied_building_A = 0
  slots_ocuppied_building_B = 0

  #search in accounts if the room is taken, if so add it to the occupied array
  for i in range(rows_accounts):
      for j in range(columns_accounts):
        exists = accounts[i][j] in [item for sublist in original_living_array for item in sublist]
        
        if exists == True:
          slots_taken.append(accounts[i][j])

  #search in the slots_taken array which belong to the building A or B

  for item in slots_taken:
    if item.startswith('A'):
      slots_ocuppied_building_A +=1
    elif item.startswith('B'):
      slots_ocuppied_building_B +=1


  #debugging purposes
  #print(slots_taken)
  #print(slots_ocuppied_building_A)
  #print(slots_ocuppied_building_B)
        
  #find how many spaces are avaliable in each building

  slots_available_building_A = 0
  slots_available_building_B = 0

  slots_available_building_A = len_Building_A - slots_ocuppied_building_A

  slots_available_building_B = len_Building_B - slots_ocuppied_building_B

  #debugging purposes
  #print("slots availables")
  #print(slots_available_building_A)
  #print(slots_available_building_B)

  #save the information in the search_living_pod array and output

  search_living_pod = [
    ["Building A", len_Building_A, slots_ocuppied_building_A, slots_available_building_A],
    ["Building B", len_Building_B, slots_ocuppied_building_B, slots_available_building_B]
  ]

  print(tabulate(search_living_pod, headers=["Building Name", "Total Slots", "# Humans assign", "Slots availables"]))  



# Create a function to display an administrator human population report that lists the account information for all human users - showing id number, first/last name, email and password. Require that an admin password is input before processing this request (let me know what it is!)  (10 points)

def human_report(accounts):
  admin_password_input = input("Password: ")
  admin_password = "Admin123*"

  while admin_password_input != admin_password:
    print("Password incorrect. Try again")
    admin_password_input = input("Password: ")

  print()
  all_accounts = []
 
  for row in accounts: 

    fullName = row[0] + " / "+row[1]
    adm_acc = [row[2], fullName , row[3], row[4]]
    all_accounts.append(adm_acc)

  print(tabulate(all_accounts, headers=["ID number", "First/Last Name", "Email", "Password"]))    

  print()
  


# Create a delete function that will allow the user to delete a human from the system. (5 points)

def delete_acc(accounts):
  
  delete_input = input("Which account you want to delete? Enter a number: ")
  delete_input_numeric = delete_input.isnumeric()

  while delete_input_numeric != True:

    print("Try again")
    delete_input = input("Enter a number: ")
    delete_input_numeric = delete_input.isnumeric()

  delete_input = int(delete_input)
    
  while delete_input < 1 or delete_input  > len(accounts):
    delete_input = int(input("Invalid number, please choose again:"))  
   
  name_del = accounts.pop(delete_input-1)
  print(name_del[0] + " " +name_del[1] + " was deleted.\n")


  #update file 
      
  with open(filename, newline="") as f:
    reader=csv.reader(f)
    for row in reader: #for every row in the file
      if row[0] == (delete_input-1): 
        accounts.remove(row) #remove row
      
      
  with open(filename,"w",newline="") as f:
    Writer=csv.writer(f)
    Writer.writerows(accounts)
    print("File has been updated")
 




def main():
  living_array = [
              ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10"], #"Building A, 10 Slots"
              ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10"]] #"Building B, 10 Slots"

  accounts = read_accounts()
  display_menu()

  while True:        
    command = input("Command: ").lower()
    print()
    if command == "add":
      try:
        new_human_account = new_account(accounts, living_array)

        #create another list for each record
        account =[]
        account.append(new_human_account[0]) #FirstName
        account.append(new_human_account[1]) #LastName
        account.append(new_human_account[2]) #ID
        account.append(new_human_account[3]) #Email
        account.append(new_human_account[4]) #Password
        account.append(new_human_account[5]) #Age
        account.append(new_human_account[6]) #Gender
        account.append(new_human_account[7]) #LivingPod

        #append the entire row to my accounts list
        accounts.append(account)

        #open the file and save the data
        write_account(account)
        print()
        print("The new account was added succesfully!")
        print()
      except ValueError:
        print()
        print("No slots avaliables, the information can not be save")
        print()
    elif command == "list":
      #open the lists with all humans information
      read_list(accounts)
      print()
    elif command == "find":
      #Search last Name in the list
      search_lastName(accounts)
      print()
    elif command == "pods":
      #Search pods
      search_living_pod(accounts)
      print()
    elif command == "admin":
      #human report
      human_report(accounts)
      print()
    elif command == "del":
      #delete human account
      delete_acc(accounts)
      print()
    elif command == "exit":
      print("Bye!")
      break
    else:
      print("Not a valid command. Please try again.\n")
    
  print()
  
  

if __name__ == "__main__":
  main()