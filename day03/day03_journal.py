import datetime
import os

#get todays date
today = datetime.date.today()
date_str = today.strftime("%y-%m-%d") #format:2025-08-26

#create file name with todays date
file_name = f"journal_{date_str}.txt"

#check if file already exists
if not os.path.exists(file_name):
    with open(file_name,"w") as file:
        file.write(f"Date: {date_str}\n")
        file.write("Day's Notes:\n")
        file.write("- "*10+"\n")
    print(f"Created new journal:{file_name}")
else:
    print(f"Today's journal already exists:{file_name}")
                          
