from prettytable import PrettyTable

results = [[1, "ram", 80], [2, "sham", 90], [3, "ajita", 80]]

print "id", "name", "marks"
for i in results:
    print i


headers = ["id", "name", "marks"]

table = PrettyTable(headers)

for row in results:
    table.add_row(row)

print table