WORKOUT_TYPE_INDEX = 0
DISTANCE_INDEX = 1
TIME_INDEX = 2

def get_entries():
    entries = {
    "2022-06-30": ["run", 3.1, 27.5],
    "2022-06-29": ["run", 5.2, 48.1],
    "2022-06-26": ["bike", 28.5, 123.2],
    "2022-06-19": ["run", 4.7, 44.7],
    "2022-06-17": ["bike", 34.9, 140.5],
    "2022-06-15": ["bike", 18, 62.1],
    "2022-06-13": ["run", 3.5, 34.2],
    }
    return entries

def print_fastest_workout(entries, user_workout_type="run"):
    """
    Finds and displays the fastest workout of the provided type.
    Params:
        entries: The dictionary of entries
        workout_type (Optional): The type of the workout to find (e.g., "run" or "bike").
    Returns:
        None
    """
    # Declare our fastest variable
    fastest = 0

    # Loop through each workout in the entries list
    for workout in entries.values():
        # pull out the variables for the type, distance, and time
        workout_type = workout[WORKOUT_TYPE_INDEX]
        distance = workout[DISTANCE_INDEX]
        time = workout[TIME_INDEX]

        # check if it matches our type
        if workout_type == user_workout_type:
            # calculate the speed as the distance / time
            speed = distance / (time / 60)
 
            # Compare speed to the fastest one, and save if it's the best
            if speed > fastest:
                fastest = speed

    # print the fastest
    print(f"The fastest {user_workout_type} is {fastest} mph")

def print_workouts(entries):
    for workout in entries.values():
        workout_type = workout[WORKOUT_TYPE_INDEX]
        distance = workout[DISTANCE_INDEX]

        print(f"{workout_type} ({distance} miles)")

def main():
    entries = get_entries()
    
    print_workouts(entries)
    print_fastest_workout(entries, "bike")

if __name__ == "__main__":
    main()

