from datetime import datetime

# Sample attendance data
attendance_data = [
    {"employee_name": "Chetan Pawar", "attendance": {"2024-08-15": ("09:00", "17:00"), "2024-08-16": ("09:15", "17:10")}},
    {"employee_name": "Aditi Shah", "attendance": {"2024-08-15": ("09:00", "17:00"), "2024-08-16": ("09:00", "17:00"), "2024-08-17": ("09:00", "17:00")}},
    {"employee_name": "Ravi Kumar", "attendance": {"2024-08-15": ("09:30", "17:00")}},
    {"employee_name": "Sneha Patil", "attendance": {"2024-08-15": ("09:00", "17:00"), "2024-08-16": ("09:00", "17:00")}},
]

# Initialize variables to store insights
total_hours_worked = {}
perfect_attendance = []
most_absences = []
total_days = 3  # Assuming we are considering 3 days of attendance

# Process attendance data
for employee in attendance_data:
    employee_name = employee["employee_name"]
    attendance = employee["attendance"]
    
    # Calculate total hours worked
    total_hours = 0
    for date, times in attendance.items():
        clock_in = datetime.strptime(times[0], "%H:%M")
        clock_out = datetime.strptime(times[1], "%H:%M")
        hours_worked = (clock_out - clock_in).seconds / 3600
        total_hours += hours_worked

    total_hours_worked[employee_name] = total_hours
    
    # Check for perfect attendance
    if len(attendance) == total_days:
        perfect_attendance.append(employee_name)
    
    # Calculate absences
    absences = total_days - len(attendance)
    most_absences.append((employee_name, absences))

# Sort employees by most absences
most_absences.sort(key=lambda x: x[1], reverse=True)

# Display insights
print("Total Hours Worked:")
for employee, hours in total_hours_worked.items():
    print(f"  {employee}: {hours:.2f} hours")

print("\nEmployees with Perfect Attendance:")
if perfect_attendance:
    for employee in perfect_attendance:
        print(f"  {employee}")
else:
    print("  None")

print("\nEmployees with the Most Absences:")
for employee, absences in most_absences:
    print(f"  {employee}: {absences} absences")
