import random
import datetime
import csv
import pandas as pd
import os
from time import sleep

def setup():
  pd.set_option('display.max_columns', None)
  pd.set_option('display.max_rows', None)

def gender():
  gender_num = random.random()
  if gender_num <= 0.475:
    sex = 'Male'
    return sex
  else:
    sex = 'Female'
    return sex

def create_name(sex):
  if sex == 'Male':
    num = random.randint(0,275)
    file = open('male_names_2.txt', 'r')
    names = file.readlines()
    name = names[num]
    name = name.strip()
    file.close
  else:
    num = random.randint(0,145)
    file = open('female_names_2.txt', 'r')
    names = file.readlines()
    name = names[num]
    name = name.strip()
    file.close
  f = open('last_names.txt','r')
  name_num = random.randint(0,98)
  last_names = f.readlines()
  last_name = last_names[name_num]
  last_name = last_name.strip()
  f.close
  return name, last_name

def eye_colour():
  eyes = ['Brown','Blue','Hazel','Amber','Grey','Green','Violet']
  eye_num = random.random()
  if eye_num <= 0.75:
    eye = eyes[0]
    return eye
  elif eye_num <= 0.84:
    eye = eyes[1]
    return eye
  elif eye_num <= 0.89:
    eye = eyes[2]
    return eye
  elif eye_num <= 0.94:
    eye = eyes[3]
    return eye
  elif eye_num <= 0.97:
    eye = eyes[4]
    return eye
  elif eye_num <= 0.99:
    eye = eyes[5]
    return eye
  else:
    eye = eyes[6]
    return eye

def hair_colour():
  hairs = ['Black', 'Brunette', 'Blonde', 'Red']
  hair_num = random.random()
  if hair_num <= 0.84:
    hair = hairs[0]
    return hair
  elif hair_num <= 0.95:
    hair = hairs[1]
    return hair
  elif hair_num <= 0.98:
    hair = hairs[2]
    return hair
  else:
    hair = hairs[3]
    return hair

def heights(sex):
  if sex == 'Male':
    male_height = random.gauss(165.6, 30)
    height = round(male_height, 1)
    return height
  else:
    female_height = random.gauss(154.9, 30)
    height = round(female_height, 1)
    return height

def rand_distributed():
  month = {1:849,2:767,3:849,4:822,5:849,6:822,7:849,8:849,9:822,10:849,11:822,12:849}
  
  #find out how many births in total
  total_count=0
  for count in month.values():
    total_count +=  count

  #select one
  rand_selection = random.randint(0,total_count)

  #find out where that would fall in the range
  selection = 0
  total_count = 0
  for keyval_pair in month.items():
      if (total_count + keyval_pair[1] < rand_selection):
          total_count +=  keyval_pair[1]
      else:
        selection = keyval_pair[0]
        return selection

def birthday():
  now = datetime.datetime.now().year
  birth_month = rand_distributed()
  if birth_month == 1 or birth_month == 3 or birth_month == 5 or birth_month == 7 or birth_month == 8 or birth_month == 10 or birth_month == 12:
    birthday = random.randint(1, 31)
  elif birth_month == 2:
    leap_day = random.randint(1, 1461)
    if leap_day == 420:
      print("Leap Day")
      birthday = 29
    else:
      birthday = random.randint(1, 28)
  else:
    birthday =  random.randint(1, 30)
  
  if birth_month == 1:
    month = 'January'
  elif birth_month == 2:
    month = 'February'
  elif birth_month == 3:
    month = 'March'
  elif birth_month == 4:
    month = 'April'
  elif birth_month == 5:
    month = 'May'
  elif birth_month == 6:
    month = 'June'
  elif birth_month == 7:
    month = 'July'
  elif birth_month == 8:
    month = 'August'
  elif birth_month == 9:
    month = 'September'
  elif birth_month == 10:
    month = 'October'
  elif birth_month == 11:
    month = 'November'
  else:
    month = 'December'
  age = random.gauss(43.7, 15)
  age = round(age)
  year = now - age
  return birthday, month, year, age

def get_name():
  name = input("What is the person's first name?\n")
  name = name[0].upper() + name[1:len(name)].lower()
  sleep(0.5)
  last_name = input(f"What is {name}'s last name?\n")
  last_name = last_name[0].upper() + last_name[1:len(last_name)].lower()
  return name, last_name

def get_gender(name):
  while True:
    options = ['Male','Female','Non-binary','Other','Prefer not to say']
    option = options[0] + ', ' + options[1] + ', ' + options[2] + ', ' + options[3] + ', ' + options[4]
    sex = input(f"What is {name}'s gender?\nThe options are:\n{option}\nTo randomise between male and female, type 'Random'\n")
    sex = sex[0].upper() + sex[1:len(sex)].lower()
    if sex == 'Random':
      sex =  gender()
      print(f"The randomised choice is: {sex}")
      sleep(0.5)
      return sex
    elif sex not in options:
      print('That is not a valid option, please try again')
      sleep(0.5)
    else:
      return sex

def get_eye_colour(name):
  while True:
    options = ['Brown','Blue','Hazel','Amber','Grey','Green','Violet']
    option = options[0] + ', ' + options[1] + ', ' + options[2] + ', ' + options[3] + ', ' + options[4]
    eye = input(f"What colour is {name}'s eyes?\nThe options are:\n{option}\nTo randomise the option, type 'Random'\n")
    eye = eye[0].upper() + eye[1:len(eye)].lower()
    if eye == 'Random':
      eye = eye_colour()
      print(f"The randomised eye colour is: {eye}")
      sleep(0.5)
      return eye
    elif eye not in options:
      print("That is not a natural eye colour, please try again.")
      sleep(0.5)
    else:
      return eye


def get_hair_colour(name):
  while True:
    options = ['Black', 'Brunette', 'Blonde', 'Red']
    option = options[0] + ', ' + options[1] + ', ' + options[2] + ', ' + options[3]
    hair = input(f"What colour is {name}'s hair?\nThe options are:\n{option}\nType 'Random' to randomise this option\n")
    hair = hair[0].upper() + hair[1:len(hair)].lower()
    if hair == 'Random':
      hair = hair_colour()
      print(f"The randomised hair colour is: {hair}")
      return hair
    elif hair not in options:
      print("That is not a natural hair colour, please try again.")
      sleep(0.5)
    else:
      return hair

def foot_inch_convert(foot, inches):
 total_inches = inches + (foot*12)
 centimeters_to_inches = total_inches*2.54
 return centimeters_to_inches

def get_height(name,sex):
  while True:
    inch_or_cm = int(input(f"What is {name}'s height measured in?\n1.Feet and Inches\n2.Centimeters\n3.Randomise this option\n"))
    if inch_or_cm == 1:
      foot = float(input(f"How many feet tall is {name}?\n"))
      sleep(0.5)
      inches = float(input(f"How many inches?\n"))
      height = foot_inch_convert(foot, inches)
      height = round(height, 1)
      return height
    elif inch_or_cm == 2:
      height = float(input(f"What is {name}'s height in centimeters?\n"))
      height = round(height, 1)
      return height
    elif inch_or_cm == 3:
      height = heights(sex)
      print(f"The randomised height is: {height}cm")
      sleep(0.5)
      return height
    else:
      print("Invalid option, try again.")

def get_birthday(name):
  now = datetime.datetime.now().year
  while True:
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    month_vari = months[0] + ', ' + months[1] + ', ' + months[2] + ', ' + months[4] + ', ' + months[5] + ', ' + months[6] + ', ' + months[7] + ', ' + months[8] + ', ' + months[9] + ', ' + months[10] + ', ' + months[11]
    month = input(f"Which month was {name} born in?\nMonths:\n{month_vari}\nTo randomise {name}'s whole birthday, type 'Random'\n")
    month =  month[0].upper() + month[1:len(month)].lower()
    if month == 'Random':
      day, month, year, age = birthday()
      print(f"{name}'s randomised birthday is: {day} {month}, {year}")
      print(f"Age: {age}")
      sleep(0.5)
      return day, month, year, age
    if month not in months:
      print("That is not a correct month, try again.")
      sleep(0.5)
    else:
      break
  while True:
    if month == months[0] or month == months[2] or month == months[4] or month == months[6] or month == months[7] or month == months[9] or month == months[11]:
      days = 31
      break
    elif month == months[1]:
      while True:
        leap_year = int(input("1.Standard year\n2.Leap year\n"))
        if leap_year == 1:
          days = 28
          break
        elif leap_year == 2:
          days = 29
          break
        else:
          print("Invalid input, try again.")
          sleep(0.5)
    else:
      days = 30
  while True:
    day =  int(input(f"On which day in {month} was {name} born on?\n"))
    if day > days:
      print(f"There is not {day} days in {month}, try again.")
      sleep(0.5)
    elif day <= 0:
      print(f"There is not {day} days in {month}, try again.")
      sleep(0.5)
    else:
      break
  while True:
    year = int(input(f"What year was {name} born in?\n"))
    if year < 1900:
      print("Sorry, the age slider does not go brrr.")
      sleep(0.5)
    elif year > now:
      print("Sorry, a person cannot be born in the future.")
      sleep(0.5)
    else:
      break
  age = now - year
  print(f"Age: {age}")
  return day, month, year, age

def create_person():
  name, last_name = get_name()
  sleep(0.5)
  full_name = name + ' ' + last_name
  sex = get_gender(name)
  sleep(0.5)
  eye = get_eye_colour(name)
  sleep(0.5)
  hair = get_hair_colour(name)
  sleep(0.5)
  height = get_height(name,sex)
  sleep(0.5)
  day, month, year, age = get_birthday(name)
  sleep(0.5)
  birth_date = str(month) + ' ' + str(day) + ' ' + str(year)
  data = []
  data.append(full_name)
  data.append(sex)
  data.append(eye)
  data.append(hair)
  data.append(height)
  data.append(age)
  data.append(birth_date)
  print(data)
  file = open('Korean_people.csv', 'a')
  write = csv.writer(file)
  write.writerow(data)
  file.close
  print(f"{name} Created.")
  sleep(0.5)

  
def create_data():
  number = int(input("How many people will be created?\n"))
  for i in range(number):
    sex = gender()
    name, last_name = create_name(sex)
    full_name = name + ' ' + last_name
    eye = eye_colour()
    hair = hair_colour()
    height = heights(sex)
    day, month, year, age = birthday()
    birth_date = month + ' ' + str(day) + ' ' + str(year)
    data = []
    data.append(full_name)
    data.append(sex)
    data.append(eye)
    data.append(hair)
    data.append(height)
    data.append(age)
    data.append(birth_date)
    file = open('Korean_people.csv', 'a')
    write = csv.writer(file)
    write.writerow(data)
  file.close
  print("Data generated.")
  sleep(0.5)

def reset_data():
  header = ['Name', 'Gender/Sex', 'Eye Colour', 'Hair Colour', 'Height (cm)', 'Age', 'Birthday']
  os.remove('Korean_people.csv')
  file = open('Korean_people.csv','w')
  write = csv.writer(file)
  write.writerow(header)
  file.close
  sleep(0.5)
  print("Data Reset.")
  sleep(0.5)

def read_data():
  while True:
    data = pd.read_csv('Korean_people.csv')
    df =  pd.DataFrame(data)
    num_of_rows = len(df.index)
    if df.empty:
      print('There is no data in the database, you must generate some first.')
      sleep(0.5)
      break
    else:
      loop = True
      while loop == True:
        search = int(input("1.Search by number\n2.Search by name\n3.Back to menu\n"))
        if search == 1:
          line_num = int(input(f'Which number will be search?\n1 to {num_of_rows}\n'))
          if line_num > num_of_rows:
            print("Invalid, try again")
            sleep(0.5)
          else:
            print(df.iloc[(line_num-1),:])
            sleep(0.5)
        elif search == 2:
          term = input("What is the first name of the person you are searching for?\n")
          term = term[0].upper() + term[1:len(term)].lower()
          term_extra = input(f"What is the last name of {term}?\n")
          term_extra = term_extra[0].upper() + term_extra[1:len(term_extra)].lower()
          search_term = term + ' ' + term_extra
          with open("Korean_people.csv") as f_obj:
            reader = csv.reader(f_obj, delimiter=',')
            found = False
            for item in reader:
              if search_term in item[0]:
                print(f"Name\t\t\t{item[0]}")
                print(f"Gender/Sex\t\t{item[1]}")
                print(f"Eye Colour\t\t{item[2]}")
                print(f"Hair Colour\t\t{item[3]}")
                print(f"Height (cm)\t\t{item[4]}")
                print(f"Age\t\t\t\t{item[5]}")
                print(f"Birthday\t\t{item[6]}")
                print()
                sleep(0.5)
                found = True
            if found == False:
              print("Name not found")
              sleep(0.5)
              break
        elif search == 3:
          break
        else:
          print("Invalid option, try again")
    sleep(0.5)
    break

def menu():
  setup()
  while True:
    ans = int(input("1. Randomly generate some data\n2. Reset the database\n3. Search the database\n4. Create your own data entry\n5. Exit\n"))
    if ans == 1:
      create_data()
    elif ans == 2:
      reset_data()
    elif ans == 3:
      read_data()
    elif ans == 4:
      create_person()
    elif ans == 5:
      break
    else:
      print("Incorrect input. try again")

menu()
