import csv
import ast

def remove_entry(user_name, index):
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
            updated_user_data = [entry for entry in user_data if entry['primary_key'] != primary]

    # Clear the file content
            userfile.seek(0)
            userfile.truncate()

    # Write the updated list back to the CSV file
            user_writer = csv.DictWriter(userfile, fieldnames=user_reader.fieldnames)
            user_writer.writeheader()
            user_writer.writerows(updated_user_data)

#     csv_file_path = f"{username}.csv"

#     # Read the CSV file and store the rows in a list
#     with open(csv_file_path, 'r', newline='') as file:
#         csv_reader = csv.reader(file)
#         rows = list(csv_reader)

#     # Check if the index is within the range of rows
#     if 0 <= index < len(rows):
#         # Remove the entry at the specified index
#         removed_entry = rows.pop(index)

#         # Write the modified list of rows back to the CSV file
#         with open(csv_file_path, 'w', newline='') as file:
#             csv_writer = csv.writer(file)
#             csv_writer.writerows(rows)
#     else:
#         print("Invalid index.")


# Example usage:
