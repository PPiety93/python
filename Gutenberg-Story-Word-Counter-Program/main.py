# 11/30/2021
# Paola Lopez - Piety
# PROG108 - Gutenberg Story Word Counter Program

import csv

#create a filenamefor our .csv file
filename = "search.csv"

#create a filenam efor our .txt file
pride_and_prejudice = "pride-and-prejudice.txt"
emma = "emma.txt"
persuasion = "persuasion.txt"

#create function that save the info in the cvs.file
def write_search(eachsearch):
  with open(filename, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(eachsearch)

#get the data
def read_search():
  searches = []
  
  with open(filename, newline="") as file:
    reader = csv.reader(file)
    for row in reader:
      searches.append(row)
  return searches
 

def list_search(searches):
  print("BOOK\t\t\t\t\tEARCH TERM\t\t\tRESULTS") #headings
  for i in range(0,len(searches)):
    eachsearch = searches[i] # i counter
    print(str(eachsearch[0]).center(20) + str(eachsearch[1]).center(20) + str(eachsearch[2]).center(20))


def display_menu():
  
  print("Please choose from one of the stories below:")
  print("A - Pride and Prejudice (1998)")
  print("B - Emma (1994)")
  print("C - Persuasion (1994)")
  print("E - Exit Program")
  print()  


#Book A

def choice_A():
  try:
    with open(pride_and_prejudice) as story1:
      story = story1.read() # save the entire story to a string
      # break the string into a list of words
      storyWords = story.split()
      return storyWords
  except FileNotFoundError:
    print("Sorry that story cannot be found")
  except OSError:
    print("Sorry that story cannot be found")


#Book B
def choice_B():
  try:
    with open(emma) as story2:
      story = story2.read() # save the entire story to a string
      # break the string into a list of words
      storyWords = story.split()
      return storyWords
  except FileNotFoundError:
    print("Sorry that story cannot be found")
  except OSError:
    print("Sorry that story cannot be found")

#Book C
def choice_C():
  try:
    with open(persuasion) as story3:
      story = story3.read() # save the entire story to a string
      # break the string into a list of words
      storyWords = story.split()
      return storyWords
  except FileNotFoundError:
    print("Sorry that story cannot be found")
  except OSError:
    print("Sorry that story cannot be found")


def main():
  print("Gutenberg Story Word Counter Program")
  print()  
  again = "n"
  while again.lower() == "n":
    print()   
    display_menu()
    print()
    searches = read_search()
    

    bookName = "";
    storyWords = "";
    storyLen = "";
    
    choice = "";

    while choice != "e":
      choice = input("Your choice: ").lower()
      if choice.lower() == "a":
        bookName = "Pride and Prejudice"
        storyWords = choice_A()
        storyLen = len(choice_A())
        break
      elif choice.lower() == "b":
        bookName = "Emma"
        storyWords = choice_B()
        storyLen = len(choice_B())
        break
      elif choice.lower() == "c":
        bookName = "Persuasion"
        storyWords = choice_C()
        storyLen = len(choice_C())
        break
      elif choice.lower() == "e":
        print("Good Bye!")
        exit()
      else:
        print("Not a valid command. Please try again.\n")
        choice = input("Your choice: ").lower()

    print()
    print(f"Great, we will work with {bookName}.")
    print()

    again = "y"
    while again.lower() == "y":
      searchTerm = input("Enter your search term: ")
      while len(searchTerm.strip()) == 0:
        searchTerm = input("Try Again. Enter your search term: ") 
      print()
      print(f"{bookName} has about {storyLen} words.")

      # search our list for a count of that search term
      termCount = storyWords.count(searchTerm)

      # print the count of the search term found 
      print(f"The search term {searchTerm} was found {termCount} times in {bookName}")
      print()

      #create another list for each record
      eachsearch =[]
      eachsearch.append(bookName)
      eachsearch.append(searchTerm)
      eachsearch.append(termCount)
      #append the entire row to my searches list
      searches.append(eachsearch)

      #open the file and save the data
      write_search(eachsearch)
      print("Your searches:")
      print()
      list_search(searches)
      print()

      again = input("Would you like to search again (y/n)?: ")
      while again.lower() != "y" and again.lower() != "n":
        again = input("Please try again (y/n)?: ")

  


if __name__ == "__main__":
    main()




