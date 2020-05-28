
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



