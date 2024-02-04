from dateutil import parser

def get_time(input_time):
    try:
        parsed_time = parser.parse(input_time)
        return parsed_time.strftime("%H:%M:%S")
    except ValueError:
        return "Invalid input time format"

# # Example usage:
# time1 = "8pm"
# time2 = "2.45am"
# time3 = "12 PM"
# time4 = "12:45"

# result1 = parse_natural_language_time(time1)
# result2 = parse_natural_language_time(time2)
# result3 = parse_natural_language_time(time3)
# result4 = parse_natural_language_time(time4)

# print(f"{time1} converted to standard time: {result1}")
# print(f"{time2} converted to standard time: {result2}")
# print(f"{time3} converted to standard time: {result3}")
# print(f"{time4} converted to standard time: {result4}")
