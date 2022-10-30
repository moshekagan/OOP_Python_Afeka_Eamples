# import csv module
import csv
# ------------------------
# Read from CSV file
# ------------------------

# open the file 'example_csv_file.csv' (this is the file path) and save it in the variable: csv_file
with open("example_csv_file.csv") as csv_file:
    # read the file as a CSV file
    read = csv.reader(csv_file)

    # skip the first line in the CSV file (because it's the title)
    next(read)

    # Run over the row in the CSV file
    # Each row return in the loop a list of strings
    for row in read:
        # getting the name (first item in the row)
        name = row[0]
        # getting the grade (second item in the row)
        grade = row[1]

        # printing the name and his grade
        print(f"Name is {name} and the grade is {grade}")


# ------------------------
# Write into CSV file
# ------------------------

# open the file 'example_csv_file.csv' in mode "a" (Append) - will append to the end of the file
# Also possible to open in "w" (Write) mode - will overwrite any existing content
with open("example_csv_file.csv", mode='a') as csvfile:
    # create CSV writer from the file
    writer = csv.writer(csvfile)

    # read input from the user to insert as a new line to the file
    name = input("insert a student name: ")
    grade = int(input("insert a student name: "))

    # creating a list as a row of values
    row = [name, grade]
    # writing to the end of the file the new row
    writer.writerow(row)

    # Don't forget to close the file after writing!!!
    csvfile.close()
