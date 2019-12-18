
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_CONVERTION = { 'january': 1,
                     'february': 2,
                     'march': 3,
                     'april': 4,
                     'may': 5,
                     'june': 6,
                     'july': 7,
                     'august': 8,
                     'september': 9,
                     'october': 10,
                     'november': 11,
                     'december': 12 }

DAY_CONVERTION = { 'monday': 0,
                   'tuesday': 1,
                   'wednesday': 2,
                   'thursday': 3,
                   'friday': 4,
                   'saturday': 5,
                   'sunday': 6 }

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
        try:
            city = input('Would you like to see data for Chicago, New York or Washington? \n ').lower()
            if city not in ['chicago', 'new york city', 'new york', 'washington']:
                print('Enter some of the this: chicago, new york city or washington')
            else:
                break
        except:
            print('Incorrect value; Please, enter one of: chicago, new york city or washington')

        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Would you like to filter data by month? \n Enter the month (or type "all" in case you want look across all months) \n ').lower()
            if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                print('Incorrect value; Please, enter the month () or all')
            else:
                break
        except:
            print('Incorrect value; Please, enter the month or all')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Would you like to filter data by day of week? Enter the week day or "all" in case you want look across all days \n ').lower()
            if day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
                print('Please, enter the name of the day or all')
            else:
                break
        except:
            print('Incorrect value; Please, enter the name of the day or all')


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
    try:
        df = pd.read_csv(CITY_DATA[city])
    except:
        return None
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    if month != 'all':
        df = df[df['Start Time'].dt.month == MONTH_CONVERTION[month]]

    if day != 'all':
        df = df[df['Start Time'].dt.dayofweek == DAY_CONVERTION[day]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    the_most_common_month = df['Start Time'].dt.month.mode()[0]
    print('the most common month is {}'.format(the_most_common_month))

    # TO DO: display the most common day of week
    the_most_common_dow = df['Start Time'].dt.dayofweek.mode()[0]
    print('the most common day of week is {}'.format(the_most_common_dow))

    # TO DO: display the most common start hour
    the_most_common_hour = df['Start Time'].dt.hour.mode()[0]
    print('the most common hour is {}'.format(the_most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('the most popular start station is {}'.format(most_commonly_used_start_station))

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('the most popular end station is {}'.format(most_commonly_used_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station'] + ' > ' + df['End Station']
    most_frequent_route = df['route'].mode()[0]
    print('the most frequent route is {}'.format(most_frequent_route))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time is {} seconds'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time is {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print('counts of user types: \n {}'.format(counts_user_types))

    # TO DO: Display counts of gender
    try:
        counts_user_gender = df['Gender'].value_counts()
    except:
        print('There is no information about users\' gender')
    else:
        print('counts of users gender: \n {}'.format(counts_user_gender))


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
    except:
        print('There is no information about users\' birth year')
    else:
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Birth years:\n earliest: {} \n most recent: {} \n most common: {}'.format(earliest_birth_year, most_recent_birth_year, most_common_birth_year))
    

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
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
