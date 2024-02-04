import csv
def retrieve_data(user_name):
    commands = []

    # Open the CSV file for the specified user
    file_path = f"{user_name}.csv"

    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            # Skip the header row
            next(csvreader, None)
            # Read each row and append to the commands list
            for row in csvreader:
                commands.append(row)
    except FileNotFoundError:
        # Handle the case where the file is not found (user has no commands yet)
        pass

    return commands