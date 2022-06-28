"# sql_app" 

use the commands in the mysql-db-create.sh file to create and populate the database.
alternatively run 'chmod +x mysql-db-create.sh' from bash.
then run python3 -m uvicorn sql_app.main:app --reload
and visit http://127.0.0.1:8000/docs#/ from your browser to inspect the server
