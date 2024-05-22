import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

CITIES = ('chicago', 'new york city', 'washington')
MONTHS = ('january', 'february', 'march', 'april', 'may', 'june')
DAYS = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')


def get_city():
    """
    Ask user to specify a city to analyze.

    Returns:
        (str) city - name of the city to analyze
    """

    city = input('\nPlease provide the city name. The options are: '
                 '\n1 - Chicago,'
                 '\n2 - New York City,'
                 '\n3 - Washington.'
                 '\nJust write 1, 2 or 3 to select particular city: ')
    match city:
        case '1':
            print('Chicago')
            return CITIES[0]
        case '2':
            print('New York City')
            return CITIES[1]
        case '3':
            print('Washington')
            return CITIES[2]
        case _:
            print('\n!INVALID INPUT!\n\tPlease provide the city name again.\n')
            return get_city()


def get_month():
    """
    Ask user to specify a month to analyze.

    Returns:
        (str) month - name of the month to filter by
    """

    month = input('\nPlease provide the month name. The options are: '
                  '\n0 - All,'
                  '\n1 - January,'
                  '\n2 - February,'
                  '\n3 - March,'
                  '\n4 - April,'
                  '\n5 - May,'
                  '\n6 - June.'
                  '\nJust write 0, 1, 2, 3, 4, 5 or 6 to select particular month: ')
    match month:
        case '0':
            print('all')
            return 'all'
        case '1':
            print('January')
            return MONTHS[0]
        case '2':
            print('February')
            return MONTHS[1]
        case '3':
            print('March')
            return MONTHS[2]
        case '4':
            print('April')
            return MONTHS[3]
        case '5':
            print('May')
            return MONTHS[4]
        case '6':
            print('June')
            return MONTHS[5]
        case _:
            print('\n!INVALID INPUT!\n\tPlease provide the month name again.\n')
            return get_month()


def get_day():
    """
    Ask user to specify a day to analyze.

    Returns:
        (str) day - name of the day to filter by
    """

    day = input('\nPlease provide the day name. The options are: '
                '\n0 - All,'
                '\n1 - Monday,'
                '\n2 - Tuesday,'
                '\n3 - Wednesday,'
                '\n4 - Thursday,'
                '\n5 - Friday,'
                '\n6 - Saturday,'
                '\n7 - Sunday.'
                '\nJust write 0, 1, 2, 3, 4, 5, 6 or 7 to select particular day: ')
    match day:
        case '0':
            print('all')
            return 'all'
        case '1':
            print('Monday')
            return DAYS[0]
        case '2':
            print('Tuesday')
            return DAYS[1]
        case '3':
            print('Wednesday')
            return DAYS[2]
        case '4':
            print('Thursday')
            return DAYS[3]
        case '5':
            print('Friday')
            return DAYS[4]
        case '6':
            print('Saturday')
            return DAYS[5]
        case '7':
            print('Sunday')
            return DAYS[6]
        case _:
            print('\n!INVALID INPUT!\n\tPlease provide the day name again.\n')
            return get_day()


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_city()

    # get user input for month (all, january, february, ... , june)

    month = get_month()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_day()

    print('-' * 40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        df = df[df['month'] == month.title()]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('The most common month is: ', df['month'].mode()[0])
    print('Counts:', df['month'].value_counts().max())

    print('The most common day of week is: ', df['day_of_week'].mode()[0])
    print('Counts:', df['day_of_week'].value_counts().max())

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: ', df['hour'].mode()[0])
    print('Counts:', df['hour'].value_counts().max())

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common start station is: {}'.format(df['Start Station'].mode()[0]))
    print('Counts:', df['Start Station'].value_counts().max())

    # display most commonly used end station
    print('The most common end station is: {}'.format(df['End Station'].mode()[0]))
    print('Counts:', df['End Station'].value_counts().max())

    # display most frequent combination of start station and end station trip
    start_end_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most common start and end station is: {} {}'.format(start_end_station[0], start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time_hour = int(df['Trip Duration'].sum() / 60)
    print('Total tavel time is: {} h'.format(travel_time_hour))

    # display mean travel time
    mean_travel_time_hour = df['Trip Duration'].mean() / 60
    print('Mean travel time is: {} h'.format(round(mean_travel_time_hour)))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    for user_type, count in user_types_count.items():
        print('Counts of user type {}: {}'.format(user_type, count))

    print()
    # Display counts of gender
    gender_count = df['Gender'].value_counts()
    for gender, count in gender_count.items():
        print('Counts of gender {}: {}'.format(gender, count))

    print()
    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = int(df['Birth Year'].min())
    print('The earliest year of birth is: ', earliest_birth_year)

    most_recent_birth_year = int(df['Birth Year'].max())
    print('The most recent year of birth is: ', most_recent_birth_year)

    most_common_birth_year = int(df['Birth Year'].mode()[0])
    print('The most common year of birth is: ', most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)


def print_raw_lines(df):
    """Prints raw lines of data"""

    print('\nWould you like to see raw data? Enter yes or no: \n')
    show_raw_data = input().lower()
    if show_raw_data != 'yes':
        return
    else:
        try:
            limit = int(input('How many data would you like to see?. Enter a number (max {})'.format(len(df))))
        except ValueError:
            print('\n!INVALID INPUT!\n')
            return
    for line in df.head(limit).iterrows():
        print(line)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_raw_lines(df)

        restart = input('\nWould you like to restart program? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
