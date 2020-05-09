import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
         city = input("What city would you like to review?")
         if city in CITY_DATA:
                print("Selected city:", city)
                break
         else:
                print("invalid input! please enter either chicago, new york city or washington!")


    # TO DO: get user input for month (all, january, february, ... , june)
         months = ('january', 'february', 'march', 'april', 'may', 'june', 'all' )
    while True:
         month = input("enter month of interest:")
         if month in months:
                 print("Selected month:", month)
                 break
         else:
                  print("invalid input!")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ("monday", "tuesday", "wednesday", "thursday", "friday","saturday", "sunday", "all")
    while True:
         day = input('enter day of the week:')
         if day in days:
               print("Selected day:", day)
               break

         else:
            print("invalid input!")

    print('-'*40)
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

    df= pd.read_csv(CITY_DATA[city])

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'], format= '%Y-%m-%d %H:%M:%S')
    df['month'] = df['Start Time'].dt.month
    print('The most frequent month of traveling:', [df['month'].mode()[0]])
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    print('The most frequent day of traveling:', [df['day'].mode()[0]])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most frequent hour of traveling:', [df['hour'].mode()[0]])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print('popular start station:', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print("popular end stattion:", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station','End Station']).agg(lambda x:x.value_counts().index[0])
    print('popular station combination:', most_frequent_combination).mode()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total_travel_time:', total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('avg_travel_time:', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('number of users:', user_types)

    # TO DO: Display counts of gender
    genders = df["Gender"].value_count()
    print('gender count:', genders)


    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    print("earliest year of birth:", birth_year.min())
    print("most recent year of birth:", birth_year.max())
    print("popular year of birth:", birth_year.mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
