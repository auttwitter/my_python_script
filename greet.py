# greeting

# Import the datetime module to work with dates and times

import datetime

def get_time_of_day():
    """"Get the current time of day as as string."""
    # Get the current hour (0-23)
    current_hour = datetime.datetime.now().hour
    # Determine the time of the day based on the hour
    if current_hour < 12:
        return 'morning'
    # current hour is greater than or equal to 12 AND less than 18
    elif 12 <= current_hour < 18:
        return 'afternoon'
    else:
        return 'evening'
    
def get_current_time():
    """Get the current time in readable format."""
    return datetime.datetime.now().strftime('%I:%M %p')

def main():
    # Ask for the user's name
    name = input('What is your name? ')

    # Get the current time of the day and the current time
    time_of_day = get_time_of_day()
    current_time = get_current_time()

    # Personalize the greeting
    print(f'Good {time_of_day}, {name}!')
    print(f'The current time is: {current_time}')

    # Farewell message
    print(f'Goddbye, {name}! Have a wonderful {time_of_day}')

#Check if this script is being run directly (not imported)

if __name__ == '__main__':
    main()