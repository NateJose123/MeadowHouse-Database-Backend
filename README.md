# PM05- Creating your Database Application

This is the final project milestone of the abbreviated Sp2020 CSC330 course.
## Objective:
The goal of this milestone is to develop a skeleton database application to hand off to your client.
This milestone will walk you through the steps to prepare the necessary queries to retrieve data from database and translate your SQL tables into Python classes.

![Diagram of a Web Application (from https://reinvently.com/blog/fundamentals-web-application-architecture/)](diagram_reinvently.jpg "Diagram of server, database, and user interfaces")

## Preparation
- Your team should have sufficient sample data entered into your database to evaluate your queries.
- Your team should have an updated plan based on your contract renegotiation discussion with clients.
- If off campus, you should have setup VPN access to your virtual machine
- If you are unfamiliar with Linux terminal commands, particularly related to directories and understanding your current working directory, please review [this section](https://help.ubuntu.com/community/UsingTheTerminal#File_.26_Directory_Commands) on basic commands.

## Deliverables
By April 23, push to this repository:
1. SQL Queries
2. Screenshots of tables from your database structure (from myPhPAdmin)
3. A models.py file with your python classes and query methods
4. A link to your meeting document with notes from all team and client meetings since March

## Part 1 - Develop SQL Queries

Every piece of information displayed in your UI will likely come from your database, or be derived from data in your database.
Using your paper prototype as a guide, list out and write the SQL queries you will need to retrieve
the necessary data from your database to populate your webpage.

T04 and T05 were examples of how to start thinking about translating the information needed for your client into queries from the database.

_For example, if we were developing a dashboard for a Hubway client that showed the last known location of every bike,
the number of times a bike had been checked out, and how many bikes were at each station, then this dashboard would likely
require at least 3 SQL queries to supply this data to the dashboard page._

:exclamation: **TODO:** Copy and Paste your SQL queries here, with a comment containing a brief explanation of each query's purpose.
```
Create entry


/*This query inserts the common name, latin name, color, notes, and plant key of an entry, and is shown on the add entry page */
INSERT INTO `Plant`(`Common_Name`, `Latin_Name`, `Color`, `Plant_Key`, `Notes`) VALUES (name(), l_name(), color(), plant_key() , notes())
/*This query inserts the rarity, rarity key, and plant key of an entry, and is shown on the add entry page */
INSERT INTO `Rarity`(`Rarity`, `Rarity_KEY`, `Plant_Key`) VALUES ([value-1]),[value-2],[value-3])

/*This query inserts the quadrant, and location key of an entry, and is shown on the add entry page */
INSERT INTO `Location`(`Quadrant`, `Location_KEY`) VALUES ([value-1],[value-2])

/*This query inserts the day it bloomed, and the bloom key of an entry, and is shown on the add entry page */
INSERT INTO `Blooming_Time`(`Day_Bloomed`, `Bloom_KEY`) VALUES ([value-1],[value-2])

/*This query inserts the budding number, plant key, and bloom key of an entry, and is shown on the add entry page */

INSERT INTO `Plant_Blooms`(`budding`, `Plant_KEY`, `Bloom_KEY`) VALUES ([value-1],[value-2],[value-3])

/*This query inserts the map number, plant key, and location key of an entry, and is shown on the add entry page */
INSERT INTO `MAP`(`map`, `Plant_Key`, `Location_KEY`) VALUES ([value-1],[value-2],[value-3])


Delete entry
/*This query deletes all data associated with a certain plant key*/
Delete From ‘Plant’ where Plant_Key = {0}  



Modify entry
/*This query updates the details of the plant including the common name, latin name, color and notes.*/
UPDATE Plant 
SET Common_Name = “newvalue”, Latin_Name = “newvalue2”, Color = “newvalue3”, Plant_Key = “newvalue4”, Notes = “newvalue5” 
WHERE plant_key = “newvalue6”

/*This query updates the rarity of the plant.*/
UPDATE Rarity
SET Rarity = “newvalue”
 WHERE Rarity_KEY = “newvalue2”

/*This query updates the location of the plant.*/
UPDATE Location
SET Quadrant = “newvalue”
 WHERE Location_KEY = “newvalue2”

/*This query updates the blooming time of the plant.*/
UPDATE Blooming_Time
SET Day_Bloomed = “newvalue”
WHERE Bloom_KEY = “newvalue2”


Search Entries
/*This query searches the database for a specific common name.*/
SELECT  * FROM Plant  WHERE common_name = VARIABLE

/*This query searches the database for a specific latin name.*/
SELECT *  FROM Plant  WHERE latin_name = VARIABLE

/*This query searches the database for entries that are in a  specific quadrant.*/
SELECT  * FROM Location WHERE Quadrant = VARIABLE
/*This query searches the database for entries that have certain words in notes.*/
SELECT * FROM Plant WHERE notes LIKE " "

...
```

## Part 2 - Setup a basic Flask application
:exclamation: **TODO:** Follow each step to setup your Linux virtual environment.

### Step 1. Connect your Linux VM using the Terminal/Console
- Login to the VPN (You must be connected to Berea's VPN to access your virtual machine)
- Login to your virtual machine using Mac Terminal or [MobaXterm](https://mobaxterm.mobatek.net/download.html):

```
ssh USERNAME@IPADDRESS
```

- Clone the Github repository to your home directory:

``` git clone URL_TO_YOUR_REPO ```

- Go into your cloned repository directory:

```
ls -al
(this shows all files and folders in the current directory. Find your pm-05 directory)
cd YOUR_PM-05_DIRECTORY
 ```

### Step 2. Create a virtual environment and install dependencies
- Copy the setup.sh file into the ```www``` directory in your home directory (i.e., /home/USERNAME/www)

``` >>> cp setup.sh /home/USERNAME/www ```

- Run the setup file from the www directory. This will create a python virtual environment (/home/USERNAME/www/venv/) as well as install the dependencies that you need on your machine. This command will only work if your current working directory is the same as the setup.sh file (i.e., /home/USERNAME/www)

```
>>> cd /home/USERNAME/www
>>> source setup.sh
```

- Navigate to the venv directory and activate the virtual environment:

```
>>> cd /home/USERNAME/www/venv
>>> . bin/activate
```

(When the virtual environment is activated, you will see its name at the start of your command prompt, looking something like this.)

```
(venv) user@172.1.2.3:pm05 user$

```

## Part 3 - Create Python Classes for your Database Model

An object-relational model (ORM) turns your data model into a class model that you're familiar with from object-oriented programming. This way, you can treat your database entities like classes, and each entry into your database like an instance of the class. In this class, we use the Peewee Python library, which is compatible with several different databases, including MySQL.

The [sampleModels.py](sampleModels.py) file is an example of a python ORM of a database, as used by the Student Software Development Team.

:exclamation: **TODO:** Insert or link to screenshots of your database table structure from phpMyAdmin
```
Put screenshots of all your tables.
```
### Blooming Time


![image](https://github.com/2020-Spring-CSC-330/pm-05-creating-your-database-application-meadowhouse/blob/master/Tables%20Screenshots/Blooming_Time.png)

### Location


![image](https://github.com/2020-Spring-CSC-330/pm-05-creating-your-database-application-meadowhouse/blob/master/Tables%20Screenshots/Location.png)


### MAP


![image](https://github.com/2020-Spring-CSC-330/pm-05-creating-your-database-application-meadowhouse/blob/master/Tables%20Screenshots/MAP.png)

### Plant


![image](https://github.com/2020-Spring-CSC-330/pm-05-creating-your-database-application-meadowhouse/blob/master/Tables%20Screenshots/Plant.png)

### Plant Blooms


![image](https://github.com/2020-Spring-CSC-330/pm-05-creating-your-database-application-meadowhouse/blob/master/Tables%20Screenshots/Plant_Blooms.png)


### Rarity


![image](https://github.com/2020-Spring-CSC-330/pm-05-creating-your-database-application-meadowhouse/blob/master/Tables%20Screenshots/Rarity.png)


### Step 1. Create Models.py file
The [Peewee documentation](http://docs.peewee-orm.com/en/latest/peewee/models.html) includes detailed HOWTO's, examples, and explanations.

:exclamation: **TODO**:
We've provided a starter [models.py](models.py) that you can use. To complete the steps below, simply copy the file, or its contents, into your /home/USERNAME/www directory and modify as needed.

In the examples and [_models.py_](models.py):
 -  Notice how the class name is the same as the table name, and the class attributes are the same as the columns
 -  Peewee has equivalent datatypes for MySQL (See the documentation for full list)

#### There are two ways to create an ORM from your model:

_Semi-automated class creation:_

For pre-existing databases, Peewee provides a command line tool to automatically create an ORM that mirrors your database. This can save you a lot of typing! However, it will not be perfect, so you can use this to speed up your process, but not as your final product! Continue on to the manual step to check your columns, datatypes, fields, keys, and constraints.

:exclamation: **TODO:** In your FLASKDIR, replace the ALL CAPS fields and run this script on your command line. It will create or modify a models.py file:

```>>> python -m pwiz -e mysql -u root -H localhost -P DATABASENAME > models.py```

_Manual class creation:_

In your models.py file, create a class for each table in your database. See the model.py sample file for an example.
- Each class definition includes the table name, each column in the table, the field datatype, and primary and foreign keys
- Just like regular python classes, you can also include functions inside your class to perform object-specific functions (such as validity checks)

_Notes_: The below class function defines what information is returned when you call an instance of the object. If you leave this out, the default printout is the memory location, so it's worth it to put some useful identifying info here. That may be the ID (as below), or it could be other useful information (e.g., First Name and Last name).
```
def __str__(self):
                return str(self.ID)
```

### Step 2: Connect to your Database

Once your model is setup, you can connect to your database and start making queries!

Connecting to your database is 1 line of code ```database.connect()``` Every time you want to execute a set of queries, connect to the database, and disconnect when you are done, using ```database.close()```

You can test out your connection by making a few [test SELECT statements](http://docs.peewee-orm.com/en/latest/peewee/querying.html#selecting-multiple-records).

For example, in the example below, we open a connection, execute a simple SELECT query, print the first row from the result, and close the connection.

```
mainDB.connect()
query = Stations.select() #Replace "Stations" with the name of your class
print(query[0])
mainDB.close()
```

Another example is included in models.py which prints every row from the resulting SELECT query.

To see your query results, execute the python file.

``` >>> python models.py ```

If you have a lot of results, you might want to redirect them into another file. [View results in table format](https://www.tecmint.com/display-command-output-or-file-contents-in-column-format/)

```>>> python models.py > results.csv```

### Step 3: Write out your queries

Peewee provides a couple ways to write out your SQL queries.

__Option 1__:* The preferred method is generally to use [built-in methods to Create, Update, Retrieve (select), and Delete rows:](docs.peewee-orm.com/en/latest/peewee/querying.html)

For example, in Step 2, the ```.select()``` method represents the SELECT statement.

Peewee supports all the SQL clauses, such as [WHERE](http://docs.peewee-orm.com/en/latest/peewee/querying.html#filtering-records), [GROUP_BY](http://docs.peewee-orm.com/en/latest/peewee/querying.html#aggregating-records), and [JOINS](http://docs.peewee-orm.com/en/latest/peewee/relationships.html). It might even be easier to write your queries out this way!

__Option 2__: You can also [execute a SQL query directly](http://docs.peewee-orm.com/en/latest/peewee/database.html#executing-queries):

:exclamation: **TODO:** Write out your queries in Python. Place these queries in appropriately named functions at the bottom of your _models.py_ file. (i.e.:

```
def getNewDonors():
  return Donors.select(id, name).where(joinDate < '2020-01-01')
```

or more appropriately:

```
def getNewDonors(join_date):
  return Donors.select(id, name).where(joinDate < join_date)
```

Be sure to test all your queries!

---

## Submission Instructions
This is the final milestone of the course! All teamworks, milestones, and associated files should be submitted by April 23 @ 11:55PM.
1. Export and add your .sql file for your project to this repository.
2. Commit and push your README and Python files, and any supporting materials (i.e. images).
3. Merge any branches you created to the master branch.
