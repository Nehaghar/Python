# Creating a dataframe from a dictionary
# Let's define a dataframe with a list of bank clients with IDs = 1, 2, 3, 4, 5 

raw_data = {'Bank Client ID': ['1', '2', '3', '4', '5'],
            'First Name': ['Nancy', 'Alex', 'Shep', 'Max', 'Allen'], 
            'Last Name': ['Rob', 'Ali', 'George', 'Mitch', 'Steve']}

Bank_df_1 = pd.DataFrame(raw_data, columns = ['Bank Client ID', 'First Name', 'Last Name'])
Bank_df_1


# Let's define another dataframe for a separate list of clients (IDs = 6, 7, 8, 9, 10)
raw_data = {
        'Bank Client ID': ['6', '7', '8', '9', '10'],
        'First Name': ['Bill', 'Dina', 'Sarah', 'Heather', 'Holly'], 
        'Last Name': ['Christian', 'Mo', 'Steve', 'Bob', 'Michelle']}
Bank_df_2 = pd.DataFrame(raw_data, columns = ['Bank Client ID', 'First Name', 'Last Name'])
Bank_df_2


# Let's assume we obtained additional information (Annual Salary) about our bank customers 
# Note that data obtained is for all clients with IDs 1 to 10 
raw_data = {
        'Bank Client ID': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        'Annual Salary [$/year]': [25000, 35000, 45000, 48000, 49000, 32000, 33000, 34000, 23000, 22000]}
bank_df_salary = pd.DataFrame(raw_data, columns = ['Bank Client ID','Annual Salary [$/year]'])
bank_df_salary


# Let's concatenate both dataframes #1 and #2
# Note that we now have client IDs from 1 to 10
bank_df_all = pd.concat([Bank_df_1, Bank_df_2])
bank_df_all


# Let's merge all data on 'Bank Client ID'
bank_df_all = pd.merge(bank_df_all, bank_df_salary, on = 'Bank Client ID')
bank_df_all
