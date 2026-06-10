import json
import os
import csv
from json import JSONDecodeError


def inputfromuser(foods,date,month):

    if date is None and month is None:
        while True:
            try:
                date = int(input("Please enter the date of the day: (example :11) "))
                month = int(input("Please enter the month in number: (for january: 1)"))
                break
            except ValueError:
                print("Please enter a valid date")

    user_today_food = input("Please enter the food").lower()
    while True:
        try:

            if user_today_food not in foods:
                food_calories = float(input("Please enter the calories"))
                food_protein = float(input("Please enter the protein"))
            else:
                food_calories = None
                food_protein = None


            value = True
            while value:
                food_amount = float(input("Please enter the amount of food"))
                if food_amount == 0:
                    print("Food amount cannot be zero")
                    pass
                else:
                    value = False

            break

        except ValueError:
            print("Please enter a number")

    return date, month, user_today_food, food_calories, food_protein, food_amount


def csv_saver(dict_uwanna_save,csv_file_path,headers):

    if os.path.exists(csv_file_path):
        with open(csv_file_path, "a", newline="") as csvfilea:
            writer = csv.DictWriter(csvfilea, fieldnames=headers)
            writer.writerow(dict_uwanna_save)

    else:
        with open(csv_file_path, "w", newline="") as csvfilew:
            writer = csv.DictWriter(csvfilew, fieldnames=headers)
            writer.writeheader()
            writer.writerow(dict_uwanna_save)



def whole_info_opener(user_history_file):
    while True:
        read_again_decision = input("Do you want to read the whole info? (y/n)")
        if read_again_decision == "y":
            with open(user_history_file, "r", newline="") as csvfiler:
                csvreader = csv.DictReader(csvfiler)
                for rows in csvreader:
                    print(rows)
                break
        elif read_again_decision == "n":
            break

        else:
            print("Please enter y or n")


def daily_food_calculator(user_today_food,user_today_calories,food_amount,foods):
    if user_today_food not in user_today_calories:

        user_today_calories[user_today_food] = {
            "calories": food_amount * foods[user_today_food]["calories"],
            "protein": food_amount * foods[user_today_food]["protein"],
            "food_amount": food_amount
        }

    else:
        user_today_calories[user_today_food] = {
            "calories": user_today_calories[user_today_food]["calories"] + food_amount * foods[user_today_food][
                "calories"],
            "protein": user_today_calories[user_today_food]["protein"] + food_amount * foods[user_today_food][
                "protein"],
            "food_amount": user_today_calories[user_today_food]["food_amount"] + food_amount
        }

    total_calories = 0
    total_protein = 0

    for i in user_today_calories.keys():
        total_calories += (user_today_calories[i]['calories'])
        total_protein += (user_today_calories[i]['protein'])

    return total_calories, total_protein



def json_saver(file_path,foods):
    with open(file_path, "w", newline="") as jsonfile:
        json.dump(foods, jsonfile)

def json_opener_as_dict(file_path):
    if not os.path.exists(file_path):
        return {}
    else:
        try:
            with open(file_path, "r", newline="") as jsonfile:
                foods = json.load(jsonfile)
                return foods
        except JSONDecodeError:
            return {}




