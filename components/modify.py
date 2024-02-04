import csv
import ast

def modify_data_point(user_name, index, new_date, new_time):
    # Open the CSV file for the specified user
    fieldnames = ['primary_key', 'date', 'time', 'event', 'Along_with']
    file_path = f"{user_name}.csv"
    primary=0
    
        # Read all data from the CSV file into a list
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        data = list(csvreader)

    # Modify the data point at the specified index with new values
    if 0 <= index < len(data):
        # Update the date and time values
        # data[index][0] = new_date
        # data[index][1] = new_time
        primary= data[index][0] 
          
    else:
        print("Invalid index.")

    # Write the updated data back to the CSV file
#     with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerows(data)

    along=[]
    with open("schedule.csv", 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        for row in csvreader:
            if row['primary_key'] == primary:
                along=row["Along_with"]
    
    along = ast.literal_eval(along)
    for user in along:
    # Open the user CSV file
        
        with open(f"{user}.csv", 'r+', newline='', encoding='utf-8') as userfile:
            user_reader = csv.DictReader(userfile)
            user_data = list(user_reader)

            # Find and update the entry with the specified primary key
            for entry in user_data:
                if entry['primary_key'] == primary:
                    # Update the date and time columns with new values
                    entry['date'] = new_date
                    entry['time'] = new_time

            # Write the updated data back to the user CSV file
            userfile.seek(0)
            userfile.truncate()
            user_writer = csv.DictWriter(userfile, fieldnames=user_reader.fieldnames)
            user_writer.writeheader()
            user_writer.writerows(user_data)        