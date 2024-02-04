import dateparser
from datetime import datetime
from dateutil.relativedelta import relativedelta, MO

def get_date(relative_expression):
    # Define a reference date (e.g., today's date)
    reference_date = datetime.now()

    # Map weekday names to their corresponding integer values
    weekday_mapping = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    
    if relative_expression.isdigit()==False and relative_expression.lower() in weekday_mapping:
        # Find the next occurrence of the specified weekday
        next_weekday = reference_date + relativedelta(weekday=weekday_mapping[relative_expression.lower()])
        return next_weekday.date()
    else:
        # Use dateparser to parse the relative expression
        parsed_date = dateparser.parse(relative_expression, settings={'RELATIVE_BASE': reference_date})

        if parsed_date:
            return parsed_date.date()
        else:
            # If parsing fails, you might want to handle it accordingly
            raise ValueError("Failed to parse the relative expression")

# Example usage:
