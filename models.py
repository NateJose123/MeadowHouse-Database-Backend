from peewee import *

## 1. The name of your database here
db = 'SQLPracticeHubway'
un = 'MySQL_Username' # likely root still
pw = 'your_MySQL_password_here' # initially it was also root

mysql_db = MySQLDatabase(db, user=un, passwd=pw)

## This is the Base class that Peewee uses to interact with the MySQL DB.
## Don't change it!
## All your model classes should inherit from this BaseModel class
class BaseModel(Model):
        class Meta:
                database = mysql_db

## 2. PUT YOUR MODELS HERE (replace the Stations class with your own classes)
class Stations(BaseModel):
        ID = PrimaryKeyField()
        station = CharField()
        municipality = CharField()
        lat = CharField(max_length=20)
        lng = CharField(max_length=20)

        def __str__(self):
                return str(self.ID)


## CALL .connect() on your database whenever you want to execute a query,
## and then .close() when the query is finished
## Make sure you save your result table!
mysql_db.connect()
result = Stations.select()
for r in result:
	print(r)

mysql_db.close()
