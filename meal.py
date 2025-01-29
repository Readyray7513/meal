def main():
    # Prompt user for input time in 24-hour format (expect input like "14:00")
    time_input = input("Enter time: ").strip().lower()

    # Convert 12-hour to 24-hour time if necessary
    if "am" in time_input or "pm" in time_input:
        time_input = convert_to_24hr_format(time_input)
    
    try:
        time_in_hours = convert(time_input)
    except ValueError:
        return  # Exit if the input is invalid (will not print anything)

    # Check if it's breakfast, lunch, or dinner time
    if 7 <= time_in_hours <= 8:
        print("breakfast time")
    elif 12 <= time_in_hours <= 13:
        print("lunch time")
    elif 18 <= time_in_hours <= 19:
        print("dinner time")


def convert_to_24hr_format(time):
    # Convert 12-hour time format with AM/PM to 24-hour format
    if "am" in time:
        time = time.replace("am", "").strip()
        if time.startswith("12"):
            time = "00" + time[2:]  # Handle 12 AM case (midnight)
    elif "pm" in time:
        time = time.replace("pm", "").strip()
        if time.startswith("12"):
            time = "12" + time[2:]  # Handle 12 PM case (noon)
        else:
            hour, minute = time.split(":")
            hour = str(int(hour) + 12)  # Convert to 24-hour format
            time = f"{hour}:{minute}"
    return time


def convert(time):
    # Split the time into hours and minutes
    if ':' not in time:
        raise ValueError("Invalid time format")
    hours, minutes = time.split(":")
    
    # Ensure hours and minutes are valid integers
    if not hours.isdigit() or not minutes.isdigit():
        raise ValueError("Invalid time format")
    
    hours, minutes = int(hours), int(minutes)
    
    # Validate the range of hours and minutes
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        raise ValueError("Invalid time format")
    
    # Convert the time to float (e.g., "7:30" -> 7.5)
    return hours + minutes / 60.0


if __name__ == "__main__":
    main()






