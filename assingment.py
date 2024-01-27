import pandas as pd
from datetime import timedelta
def read_csv_and_process(file_path):
    # Read CSV file into a DataFrame
    df = pd.read_csv( file_path , parse_dates=['Time', 'Time Out', 'Pay Cycle Start Date', 'Pay Cycle End Date'])


     # Convert time columns to datetime format
    df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
    df['Time Out'] = pd.to_datetime(df['Time Out'], errors='coerce')

    # a) Who has worked for 7 consecutive days
    consecutive_days_df = df.groupby('Employee Name')['Time'].diff().dt.days.eq(1).groupby(df['Employee Name']).cumsum()
    consecutive_days_df = consecutive_days_df[consecutive_days_df == 6].index
    print("Employees who have worked for 7 consecutive days:")
    print(df[df['Employee Name'].isin(consecutive_days_df)][['Employee Name', 'Time']])

    # b) Who have less than 10 hours of time between shifts but greater than 1 hour
    time_between_shifts = df['Time'] - df['Time Out'].shift(1)
    condition_b_df = df[(time_between_shifts > timedelta(hours=1)) & (time_between_shifts < timedelta(hours=10))]
    print("\nEmployees with less than 10 hours but greater than 1 hour between shifts:")
    print(condition_b_df[['Employee Name', 'Time', 'Time Out']])

    # c) Who has worked for more than 14 hours in a single shift
    condition_c_df = df[df['Time Out'] - df['Time'] > timedelta(hours=14)]
    print("\nEmployees who have worked for more than 14 hours in a single shift:")
    print(condition_c_df[['Employee Name', 'Time', 'Time Out']])

    # You can also perform various operations on the DataFrame based on your requirements

    # Save the processed DataFrame to a new CSV file if needed
    # df.to_csv("output_file.csv", index=False)

if __name__ == "__main__":
    # Specify the path to your CSV file
    csv_file_path = "C:\python\sheet1.csv"

    # Call the function to read and process the CSV file
    read_csv_and_process(csv_file_path)


