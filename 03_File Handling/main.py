import csv_module as csv

table = csv.read_csv("data.csv", "row")
print("\nTable:")
csv.show_table(table)

table = csv.read_csv("data.csv", "col")
print("\nTable:")
csv.show_table(table)