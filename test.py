from datetime import datetime
# Get the current date and time
current_datetime = datetime.now()

# Extract the current hour
current_hour = current_datetime.hour

print(f"The current hour is: {current_hour}")
print(current_hour==14)