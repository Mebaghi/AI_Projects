# Constant Values
deltaEntropy = 1.0
useEntropy = True # Entropy or Gini

# Project 1 Attributes
all_attributes = ['Alt', 'Bar', 'Fri', 'Hun', 'Pat', 'Price', 'Rain', 'Res', 'Type', 'Est']

# Project 2 Attributes
import csv
airplane_train = {}
airplane_test = {}
dictCounter = 0
columns_to_keep = ['Gender', 'Customer Type', 'Age', 'Type of Travel', 'Class', 'Flight Distance',
                   'Inflight wifi service', 'Departure/Arrival time convenient', 'Ease of Online booking',
                   'Gate location', 'Food and drink', 'Online boarding', 'Seat comfort', 'Inflight entertainment',
                   'On-board service', 'Leg room service', 'Baggage handling', 'Checkin service', 'Inflight service',
                   'Cleanliness', 'Departure Delay in Minutes', 'Arrival Delay in Minutes', 'satisfaction']
with open('Airplane.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        try:
            modified_row = {key: value for key, value in row.items() if key in columns_to_keep}

            if int(modified_row['Age']) < 18:
                modified_row['Age'] = 1
            elif 18 <= int(modified_row['Age']) < 30:
                modified_row['Age'] = 2
            elif 30 <= int(modified_row['Age']) < 45:
                modified_row['Age'] = 3
            elif 45 <= int(modified_row['Age']) < 60:
                modified_row['Age'] = 4
            elif int(modified_row['Age']) >= 60:
                modified_row['Age'] = 5


            if int(modified_row['Flight Distance']) < 600:
                modified_row['Flight Distance'] = 1
            elif 600 <= int(modified_row['Flight Distance']) < 1200:
                modified_row['Flight Distance'] = 2
            elif 1200 <= int(modified_row['Flight Distance']) < 1800:
                modified_row['Flight Distance'] = 3
            elif 1800 <= int(modified_row['Flight Distance']) < 2400:
                modified_row['Flight Distance'] = 4
            elif int(modified_row['Flight Distance']) >= 2400:
                modified_row['Flight Distance'] = 5


            if int(modified_row['Departure Delay in Minutes']) == 0:
                modified_row['Departure Delay in Minutes'] = 1
            elif 0 < int(modified_row['Departure Delay in Minutes']) < 30:
                modified_row['Departure Delay in Minutes'] = 2
            elif 30 <= int(modified_row['Departure Delay in Minutes']) < 60:
                modified_row['Departure Delay in Minutes'] = 3
            elif 60 <= int(modified_row['Departure Delay in Minutes']) < 150:
                modified_row['Departure Delay in Minutes'] = 4
            elif int(modified_row['Departure Delay in Minutes']) >= 150:
                modified_row['Departure Delay in Minutes'] = 5

            if int(modified_row['Arrival Delay in Minutes']) == 0:
                modified_row['Arrival Delay in Minutes'] = 1
            elif 0 < int(modified_row['Arrival Delay in Minutes']) < 30:
                modified_row['Arrival Delay in Minutes'] = 2
            elif 30 <= int(modified_row['Arrival Delay in Minutes']) < 60:
                modified_row['Arrival Delay in Minutes'] = 3
            elif 60 <= int(modified_row['Arrival Delay in Minutes']) < 90:
                modified_row['Arrival Delay in Minutes'] = 4
            elif int(modified_row['Arrival Delay in Minutes']) >= 90:
                modified_row['Arrival Delay in Minutes'] = 5

            if dictCounter < 80000:
                airplane_train.update({f'x{dictCounter}' : modified_row})
            elif dictCounter < 100000:
                airplane_test.update({f'x{dictCounter}': modified_row})
            elif dictCounter == 100000:
                break

            dictCounter += 1

        except:
            continue


airplane_attributes = airplane_train['x0']
del airplane_train['x0']
airplane_attributes = list(airplane_attributes)
