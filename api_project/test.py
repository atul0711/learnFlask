schema = ['id', 'name', 'salary', 'department', 'position', 'hireDate']
# "INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')
data = {'id': '4', 'name': 'Nano', 'salary': '200', 'department': 'HR', 'position': 'Manager', 'hireDate': '2017-01-03'}
insert_string = ''
for attr in schema:
    insert_string += '\''+data[attr]+'\''+' '
print(insert_string)
