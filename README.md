# Meal Time Checker Program
This Python program helps determine whether it's time for breakfast, lunch, or dinner based on the input time. The user can input a time in either 24-hour format (e.g., "14:00") or 12-hour format with "AM" or "PM" (e.g., "2:00 PM"). The program checks the time and prints the corresponding meal time.

Requirements:
Python 3.x

How to Use:
Run the script.
When prompted, enter a time either in 24-hour format (e.g., 14:00) or 12-hour format with "AM" or "PM" (e.g., 2:00 PM).
The program will determine whether it’s:
Breakfast time (between 7:00 AM and 8:00 AM)
Lunch time (between 12:00 PM and 1:00 PM)
Dinner time (between 6:00 PM and 7:00 PM)
If the time is outside these ranges, no output is printed.

Example:
Input:
Enter time: 7:30 AM
Output:
breakfast time

Input:
Enter time: 14:30
Output:
lunch time

Input:
Enter time: 18:45

Output:
dinner time

Input:
Enter time: 22:00

Output:
(No output, as the time is outside the specified meal time ranges)

How It Works:
The program asks the user to enter a time, which is then stripped of extra spaces and converted to lowercase for consistency.
If the time is in 12-hour format (AM/PM), it is converted to 24-hour format using the convert_to_24hr_format function.
The time is then validated and converted into a float (e.g., "7:30" becomes 7.5 hours).
Based on the time, the program prints the corresponding meal time (breakfast, lunch, or dinner).

Valid Time Formats:
24-hour format (e.g., 14:00)
12-hour format with AM/PM (e.g., 2:00 PM, 7:30 AM)
