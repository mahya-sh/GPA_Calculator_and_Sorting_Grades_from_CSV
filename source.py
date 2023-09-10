import csv
from collections import OrderedDict
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        ## This ensures that no additional newlines are inserted between rows. 
        with open(output_file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in reader:
                name = row[0]
                grades = []
                for grade in row[1:]:
                    grades.append(float(grade))
                writer.writerow((name, float(mean(grades))))


def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        ## This ensures that no additional newlines are inserted between rows. 
        with open(output_file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            students = []
            for order, row in  enumerate(reader):
                name = row[0]
                grades = [ float(grade) for grade in row[1:] if grade.strip() != '']
                students.append((name, mean(grades), order))
            sorted_students = sorted(students, key=lambda x: (x[1], x[0]))
            for student in sorted_students:
                writer.writerow(student[:2])


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        ## This ensures that no additional newlines are inserted between rows. 
        with open(output_file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            students = []
            for order, row in  enumerate(reader):
                name = row[0]
                grades = [ float(grade) for grade in row[1:] if grade.strip() != '']
                students.append((name, mean(grades), order))
            sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
            counter = 0
            for student in sorted_students:
                writer.writerow(student[:2])
                counter += 1
                if counter == 3:
                    break



def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        ## This ensures that no additional newlines are inserted between rows. 
        with open(output_file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            students = []
            for order, row in  enumerate(reader):
                name = row[0]
                grades = [ float(grade) for grade in row[1:] if grade.strip() != '']
                students.append((name, mean(grades), order))
            sorted_students = sorted(students, key=lambda x: (x[1], x[0]))
            counter = 0
            for student in sorted_students:
                writer.writerow([student[1]])
                counter += 1
                if counter == 3:
                    break


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        ## This ensures that no additional newlines are inserted between rows. 
        with open(output_file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            averages = []
            sum_of_all = average_of_all = counter = 0
            for row in  reader:
                ##name = row[0]
                grades = [ float(grade) for grade in row[1:] if grade.strip() != '']
                averages.append(mean(grades)) 
            average_of_all = mean(averages)
            formatted_average = '{:.15f}'.format(average_of_all)
            writer.writerow([formatted_average])