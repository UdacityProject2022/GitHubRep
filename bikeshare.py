import time 
import pandas as pd 
import numpy as np 


CITY_DATA = { 'chicago': 'chicago.csv', 
             'new york city': 'new_york_city.csv',
             'washington':'washington.csv'}


Valid_Months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
Valid_Cities = ['chicago', 'new york city', 'washington','all']
Valid_Days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    print('Hello, Let\'s explore some US bikeshare data!')
    while True: 
        city = input ("Which city are you traveling in? Choose between Chicago, New York City or Washington:").lower()
        month = input("Enter the month you wish to travel, if you are unsure write all:").lower()
        day = input("Enter the day of the week you wish to travel,if you are unsure write all:").lower()
        if month in Valid_Months:
            if day in Valid_Days:
                if city in Valid_Cities:
                    print("That's great.")
                    break
                else: 
                    print("Please check your spelling for your city")  
            else:
                print("Please check your spelling for your day")
        else:
            print("Please check your spelling for your month")
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
       
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all': 
        month = Valid_Months.index(month)+1
        df = df[df['month']==month]
    
    if day != 'all':
        day = Valid_Days.index(day)
        df = df[df['day_of_week']==day]
        
  #popular_hour =df['hour'].mode()[0]
    popular_hour =df['hour'].mode()[0]
    popular_month = df['month'].mode()[0]
    popular_day = df['day_of_week'].mode()[0]

    print('\nCalculating the most frequent times of travel for the city you chose...\n')
    
    print("If you were unsure of the month you wish to travel (month selected was 'all', the most popular month for the city chosen is:")
    print("If you selected a month in which to travel, the most popular month will be the month you selected (There is no wrong choice)")
    Written_Month = Valid_Months[popular_month-1]
    print(Written_Month)
    
    print("The most popular hour for that city is:")
    print(popular_hour)
    
    print("The most popular day for that city is:")
    print("If you selected a day in which to travel, the most popular month will be the month you selected (There is no wrong choice)")
    Written_Day = Valid_Days[popular_day]
    print(Written_Day)       
        
#def load_data2(city, month, day):   
    #df2 = pd.read_csv(CITY_DATA[city])
    
    
    # df['Start Time'] = pd.to_datetime(df['Start Time'])
       
    
    # df['month'] = df['Start Time'].dt.month
    # df['day_of_week'] = df['Start Time'].dt.weekday
    # df['hour'] = df['Start Time'].dt.hour
    
    # if month != 'all': 
    #     month = Valid_Months.index(month)+1
    #     df = df[df['month']==month]
    
    # if day != 'all':
    #     day = Valid_Days.index(day)
    #     df = df[df['day_of_week']==day]
    
    
    
    
    
    popular_start = df['Start Station'].mode()[0]
    popular_end =df['End Station'].mode()[0]
    
    print('\nCalculating the most popular stations and trip..\n')
    print("the most commonly used start station is:")
    print(popular_start)
    
    print("the most commonly used end station is:")
    print(popular_end)
    
    df['Combined'] = df['Start Station'].map(str) + " " + df['End Station'] 

#print(df2)
    popular_comb = df['Combined'].mode()[0]
    print("The most frequent combination of start station and end station trip is:")
    print(popular_comb)
       
    

#def load_data3(city, month, day):
    #df3 = pd.read_csv(CITY_DATA[city])
    
    
    # df['Start Time'] = pd.to_datetime(df['Start Time'])
       
    
    # df['month'] = df['Start Time'].dt.month
    # df['day_of_week'] = df['Start Time'].dt.weekday
    # df['hour'] = df['Start Time'].dt.hour
    
    # if month != 'all': 
    #     month = Valid_Months.index(month)+1
    #     df = df[df['month']==month]
    
    # if day != 'all':
    #     day = Valid_Days.index(day)
    #     df = df[df['day_of_week']==day]

    while True: 
        if city == "washington":
            print("Sorry, there is no User or Gender data for Washington.")
            
        else: 
        
    
    #df3['Counts'] = df3['User Type'] + " " + df3['User Type'].value_counts()
    #Counts = df3['Counts']
            print('Calculating User Stats, displaying counts for all types of users')
            print(df['User Type'].value_counts())
    
            print('Calculating User Stats, displaying counts for all types of genders')
            print(df['Gender'].value_counts())

            print('Calculating User Stats, displaying minimum Birth Year')
            print(df['Birth Year'].min())

            print('Calculating User Stats, displaying most recent Birth Year')
            print(df['Birth Year'].max())
    
            print('Calculating User Stats, displaying average Birth Year')
            print(df['Birth Year'].mode()[0])
        break
    return city, month, day



#def load_data4(city, month, day):
    #df4 = pd.read_csv(CITY_DATA[city])
    
    
    # df['Start Time'] = pd.to_datetime(df['Start Time'])
       
    
    # df4['month'] = df4['Start Time'].dt.month
    # df4['day_of_week'] = df4['Start Time'].dt.weekday
    # df4['hour'] = df4['Start Time'].dt.hour
    
    # if month != 'all': 
    #     month = Valid_Months.index(month)+1
    #     df4 = df4[df4['month']==month]
    
    # if day != 'all':
    #     day = Valid_Days.index(day)
    #     df4 = df4[df4['day_of_week']==day]
        
    Sum = sum(df['Trip Duration'])
    print('Calculating Trip Duration, the total travel time is:')
    print(Sum)
    #print(df['Trip Duration'].sum())
    
    print('Calculating Trip Duration, the mean travel time is:')
    print(df['Trip Duration'].mode()[0])

def time_stats(df):
    start_time = time.time() 

    print('\nCalculating the data for user stats took %s seconds.' % (time.time() - start_time))
    print("-"*40)



def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Type yes or no")
    start_loc = 0 
    while True: 
        if view_data == "yes":
           print(df.iloc[0:5])
           start_loc +=5 
           view_data = input("Do you wish to continue?: ").lower()
           break
        else:
    
def main():
    while True: 
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # df2 = load_data2(city, month, day)
        # df3 = load_data3(city, month, day)
        # df4 = load_data4(city, month, day)
        
        time_stats(df)
        
        restart = input('\nWould you like to retstart? Enter yes or no. \n')
        if restart.lower() != 'yes': 
            break 
if __name__ == "__main__":
    main()    