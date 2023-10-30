import csv
from random import randint

count_task1 = 0

with open('books-en.csv', mode='r') as file:
    books = csv.DictReader(file, delimiter=';')
    for row in books:
        if len(row["Book-Title"]) > 30:
            count_task1 += 1
print(f"Тumber of books whose titles are longer than 30 characters is {count_task1}")

print("####### task2 ########")
author = input("please write the name of author: ")
with open('books-en.csv', mode='r') as file:
    books = csv.DictReader(file, delimiter=';')
    for row in books:
        if row["Book-Author"] == author and int(row["Year-Of-Publication"]) < 2016: #for example author -  Amy Tan
            print(row['Book-Title'])

############ task3 ############

with open('books-en.csv', mode='r') as file:
    text = open("bibliography.txt", "w")
    books = list(csv.DictReader(file, delimiter=';'))
    for i in range(1, 21):
        number = randint(1, 9400)
        text.write(f"{i} {books[number]['Book-Author']} - {books[number]['Book-Title']} \n")
