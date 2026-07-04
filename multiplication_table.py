# Prints multiplication table of given number.

table_of = int(input("Print the table of: "))

for i in range(11):
    print(f"{table_of} x {i} = {table_of * i}")