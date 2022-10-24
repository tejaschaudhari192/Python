import prettytable

table = prettytable.PrettyTable()

table.add_column("Subject", ['Graphics', 'cp', 'maths'])
table.add_column("Marks", ['64', '47', '40'])

print(table)  # default alignment is 'c'
table.align = 'l'
print(table)
