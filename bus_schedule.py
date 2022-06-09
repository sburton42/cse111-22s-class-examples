from datetime import datetime

# Ask for information: Stop/Street, Bus #, How Full (and save it into variables)
street = input("What is the street for your stop? ")
bus_number = input("What is the bus number? ")
capacity = float(input("How full is the bus (percentage)? "))

# Clean up our variables
street = street.title().strip()
bus_number = bus_number.upper().strip()

# Convert decimal percents to whole numbers
if capacity > 0 and capacity < 1:
    capacity = capacity * 100
    #capacity *= 100

# Find the current day and time
today = datetime.now()

# Add to a text file
with open("bus_data.csv", "at") as bus_file:
    print(f"{today:%Y-%m-%d},{street},{bus_number},{capacity:.0f}%", file=bus_file)

# Display a message to the user saying it has been recorded
print(f"{street},{bus_number},{capacity:.0f}%")
