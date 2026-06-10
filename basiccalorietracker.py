
import functions

user_history_file = "../PyCharmMiscProject/user_history.csv"
food_json_file_path = "../PyCharmMiscProject/foods.json"

foods = functions.json_opener_as_dict(food_json_file_path)

date = None
month = None

user_today_calories = {}

value = True

while value :

    #user input section
    date, month, user_today_food, food_calories, food_protein, food_amount = functions.inputfromuser(foods,date,month)



    if user_today_food not in foods:
        foods[user_today_food] = {"calories": food_calories / food_amount,
                                  "protein": food_protein / food_amount}

    total_calories, total_protein  = functions.daily_food_calculator(user_today_food,user_today_calories,food_amount,foods)


    print(user_today_calories)

    print(f"Your total calories: {total_calories} and protein: {total_protein}")



    #New food enter sction

    while True :
        user_recal_decision = input("Do you want to include another food? (y/n)")

        if user_recal_decision == "y":
            break
        elif user_recal_decision == "n":
            value = False
            break
        else:
            print("Please enter y or n")

today_info = { "day": f"{date}/{month}",
               "calories": total_calories,
               "protein": total_protein
               }


#csv saver section
functions.csv_saver(today_info, user_history_file,["day", "calories", "protein"])
functions.json_saver(food_json_file_path,foods)


# whole inf0 opening section
functions.whole_info_opener(user_history_file)


#ending section
print("Thank you for using this program")