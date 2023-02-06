input_month = input()
input_day = int(input())


if (input_day < 1):
    season = "Invalid"    

elif ((input_month == "March") and (31 >= input_day >= 20)):
    season = "Spring"

elif ((input_month == "June") and (30 >= input_day <= 20)):
    season = "Spring"

elif ((input_month == "April" and input_day <= 30) or (input_month =="May" and input_day <= 31)):
    season = "Spring"

elif ((input_month == "June") and (30 >= input_day >= 21)):
    season = "Summer"

elif ((input_month == "September" and input_day <= 31) and ( 31 >= input_day <= 21)):
    season = "Summer"
   
elif ((input_month == "July" and input_day <= 31) or (input_month == "August" and input_day <= 31)):
    season = "Summer"

elif ((input_month == "September" and input_day <= 30) and (input_day >= 22)):
    season = "Autumn"

elif ((input_month == "December" and input_day <= 31) and (input_day <= 20)):
    season = "Autumn"
    
elif ((input_month == "October" and input_day <= 31) or (input_month == "November" and input_day <= 30)):
    season = "Autumn"

elif ((input_month == "December" and input_day <= 31) and (input_day >= 21)):
    season = "Winter"
    
elif ((input_month == "March" and input_day <= 31) and (input_day <= 19)):
    season = "Winter"

elif ((input_month == "January" and input_day <= 31) or (input_month =="February" and input_day <= 28)):
     season = "Winter"

else:
    
    season = "Invalid"

print(season)

