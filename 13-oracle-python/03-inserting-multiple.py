import cx_Oracle

# Load data from a csv file into Oracle table using executemany
try:
	con = cx_Oracle.connect('tiger/scott@localhost:1521/xe')

except cx_Oracle.DatabaseError as er:
	print('There is an error in Oracle database:', er)

else:
	try:
		cur = con.cursor()
		data = [[10007, 'Vikram', 48000.0], [10008, 'Sunil', 65000.1], [10009, 'Sameer', 75000.0]]

		cur = con.cursor()
		# Inserting multiple records into employee table
		# (:1,:2,:3) are place holders. They pick data from a list supplied as argument
		cur.executemany('insert into employee values(:1,:2,:3)', data)

	except cx_Oracle.DatabaseError as er:
		print('There is an error in Oracle database:', er)

	except Exception as er:
		print(er)

	else:
		# To commit the transaction manually
		con.commit()
		print('Multiple records are inserted successfully')

finally:
	if cur:
		cur.close()
	if con:
		con.close()
