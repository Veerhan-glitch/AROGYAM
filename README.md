#inital setup
Clone the repository:

##
    git clone https://github.com/Veerhan-glitch/AROGYAM/
    
Navigate to the project folder:

##
    cd AROGYAM
    
Create and activate a virtual environment:

On Linux/macOS:

##
    python -m venv venv
    source venv/bin/activate

On Windows:
##
    python -m venv venv
    venv\Scripts\activate
    
Install dependencies:

##
    pip install -r requirements.txt


Apply database migrations:

##
    python manage.py migrate


Run the development server:

##
    python manage.py runserver




##

psql-> create database arogyam_db

python manage.py createsuperuser   -> admin -> admin@arogyam.com -> password


pip install djangorestframework psycopg2



python manage.py inspectdb users orders product orderitems prescription doctor booksappointment healthrecords payments labtests reports supporttickets feedback notifications offers useroffers > arogyam/backend/models.py


then manuky add

    def __str__(self):
        return str(self.userid) for all

        # The composite primary key (userid, offerid) found, that is not supported. The first column is selected.
                unique_together = (('userid', 'offerid'),)

                change: useroferid

                        managed = False removed, delet on cascde
                        feedback product id not done in .sql
                        all defalt id are 0