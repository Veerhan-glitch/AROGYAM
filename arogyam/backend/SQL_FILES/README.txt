to run 1st make a database 'arogyam_db'

then run command

psql -U postgres -d arogyam_db -f arogyam/backend/SQL_FILES/create_tables.sql

to create tables

and

psql -U postgres -d arogyam_db -f arogyam/backend/SQL_FILES/insert_dummy_data.sql

to populate them


Then use following command to seee output of sql quarrys

make run-sql
