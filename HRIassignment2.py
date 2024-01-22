import csv

# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path = 'Q1 - Eye_data.csv'

# Create a dictionary to store the values
data_dict = {}

# Read the CSV file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Check if the row has at least 1 element
        if len(row) >= 1:
            # Extract the 6 numbers separated by commas
            numbers = list(map(int, row[0].split(',')))
            
            # Check if there are at least 6 numbers
            if len(numbers) >= 6:
                # Extract the first two numbers as indexes
                index1, index2 = numbers[:2]
                
                # Store the values in the dictionary
                data_dict[(index1, index2)] = numbers[2:6]

# Example: Access the values for indexes (1, 2)
data12 = data_dict[(1, 2)]
print("data12",data12)
