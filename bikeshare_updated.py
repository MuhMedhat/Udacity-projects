import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    city=input('Would you like to see data for Chicago, New York or Washington ?')
    city=city.lower() 
    """ To get city name  case insensitive"""
    while (city != 'chicago') and (city !='new york') and (city !='washington'):
        city=input('You enterered an invalid city \n Would you like to see data for Chigaco, New York or Washington ?')
        city=city.lower() 
      
    #print(city_name) 
    """For testing"""    
    filter_check =input('Would you like to filter by month, day or both. Enter"none" if you don\'t need filter  ')
    filter_check = filter_check.lower()
    while (filter_check != 'month') and (filter_check !='day') and (filter_check !='both') and (filter_check !='none'):
        filter_check=input('You enterered an invalid option \n Would you like to filter by month, day or both. Enter"none" if you don\'t need filter  ')
        filter_check=filter_check.lower() 
    
    # TO DO: get user input for month (all, january, february, ... , june)
    if (filter_check=='month' or filter_check=='both'):
       month=input('Which month ? January, February, March, April, May, June  ')
       month=month.lower()
       while (month != 'january') and (month != 'february') and (month != 'march') and (month != 'april') and (month != 'may') and (month != 'june'):
              month =input('You enterered an invalid month \n Which month ? January, February, March, April, May, June  ')
              month=month.lower()
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if (filter_check=='day' or filter_check=='both'):
       day=input('Which day ? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday  ')
       day=day.lower()
       while (day != 'monday') and (day != 'tuesday') and (day != 'wednesday') and (day != 'thursday') and (day != 'friday') and (day != 'saturday') and (day != 'sunday'):
              month =input('You enterered an invalid day \n Which day ? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday  ')
              month=month.lower()
                

    if filter_check=='none':
        month='all' 
        day = 'all'
    elif filter_check=='month':
        day = 'all'
    elif filter_check=='day':
        month = 'all'

    #print(day) 
    #print(month)
    """For testing"""
    
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
   #print(df)
    """testing"""
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Start Station:', commonly_start_station)

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    print('Most Commonly End Station:', commonly_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combined_start_end_station'] = df['Start Station'] +" and End  " +df['End Station']
    commonly_combined_station = df['combined_start_end_station'].mode()[0]
    print('Most Commonly Comination of Start and End Stations:', commonly_combined_station)    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time )   

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time:', average_travel_time ) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    if (city !='washington'):
        gender = df['Gender'].value_counts()
        print(gender)    

    # TO DO: Display earliest, most recent, and most common year of birth
    if (city !='washington'):
        min_birth = int( df['Birth Year'].min())
        print('Earlist year of birth',min_birth)   
        max_birth = int( df['Birth Year'].max())
        print('Most recent year of birth',max_birth)  
        common_birth = int( df['Birth Year'].mode()[0])
        print('Most common year of birth',common_birth)  
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
        view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no?')
        start_loc = 0
        view_display = 'yes' 
        # setting view display by default to yes to enter first while loop
        while (view_data=='yes' and  view_display =='yes'):
            print(df.iloc[start_loc:(start_loc+5)])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        """while checking washington data, an error exists as no gender there
        I tried to use city in the function but and error raised
        So I have to add new Arg here to give the function the city name to exclude washington from gender counting"""
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
