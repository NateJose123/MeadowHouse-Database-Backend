from peewee import *
database = MySQLDatabase('MeadowHouse_Plants', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'user': 'root', 'password': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class BloomingTime(BaseModel):
    bloom_key = IntegerField(column_name='Bloom_KEY', index=True)
    day_bloomed = DateField(column_name='Day_Bloomed', index=True)

    class Meta:
        table_name = 'Blooming_Time'
        primary_key = False

class Location(BaseModel):
    location_key = AutoField(column_name='Location_KEY')
    quadrant = CharField(column_name='Quadrant')

    class Meta:
        table_name = 'Location'

class Plant(BaseModel):
    color = TextField(column_name='Color')
    common_name = TextField(column_name='Common_Name')
    latin_name = TextField(column_name='Latin_Name', null=True)
    notes = TextField(column_name='Notes', null=True)
    plant_key = AutoField(column_name='Plant_Key')

    class Meta:
        table_name = 'Plant'

class Map(BaseModel):
    location_key = ForeignKeyField(column_name='Location_KEY', field='location_key', model=Location)
    plant_key = ForeignKeyField(column_name='Plant_Key', field='plant_key', model=Plant)
    map = IntegerField()

    class Meta:
        table_name = 'MAP'
        primary_key = False

class PlantBlooms(BaseModel):
    bloom_key = ForeignKeyField(column_name='Bloom_KEY', field='bloom_key', model=BloomingTime)
    plant_key = ForeignKeyField(column_name='Plant_KEY', field='plant_key', model=Plant)
    budding = IntegerField()

    class Meta:
        table_name = 'Plant_Blooms'
        primary_key = False

class Rarity(BaseModel):
    plant_key = ForeignKeyField(column_name='Plant_Key', field='plant_key', model=Plant)
    rarity = CharField(column_name='Rarity')
    rarity_key = AutoField(column_name='Rarity_KEY')

    class Meta:
        table_name = 'Rarity'


def insertdata(id, Commonname, Latinname, Color, Notes, Quadrant, Daybloomed, Rarety):
    database.connect()
    Plant.insert(common_name=Commonname, latin_name = Latinname, color = Color,  Plant_Key = id, notes = Notes).execute()
    Location.insert(quadrant = Quadrant, location_key = id).execute()
    BloomingTime.insert(day_bloomed = Daybloomed , bloom_key =id).execute()
    PlantBlooms.insert(budding = id, plant_key =id, bloom_key=id).execute()
    Map.insert(map = id, plant_key = id, location_key = id).execute()
    Rarity.insert(plant_key =id, rarity = Rarety, rarity_key = id).execute()
    database.close()




def deleet(key):
    database.connect()
    (Rarity.delete().where(Rarity.plant_key== key)).execute()
    (Map.delete().where(Map.plant_key == key)).execute()
    (PlantBlooms.delete().where(PlantBlooms.plant_key == key)).execute()
    (Plant.delete().where(Plant.plant_key == key)).execute()
    (Location.delete().where(Location.location_key == key)).execute()
    (BloomingTime.delete().where(BloomingTime.bloom_key == key)).execute()
    database.close()



def getAllPlantsByColor(Color):
   database.connect()
   for i in Plant:
       if(i.color==Color):
           print("Color: ", i.color, " Common Name: ",i.common_name," Latin Name: ",i.latin_name,  " Notes: ", i.notes)
           return ( i.color, i.common_name, i.latin_name, )
   database.close()

def getAllPlantsByCommonName(name):
   database.connect()
   for i in Plant:
       if (i.common_name == name):
           print("Common Name: ",i.common_name," Latin Name: ",i.latin_name, " Color: ", i.color, " Notes: ", i.notes)
           return (i.common_name, i.latin_name, i.color, )
   database.close()


def getAllPlantsByBloomTime(daybloomed):
  database.connect()
  for i,j in zip(Plant,BloomingTime):
      if (j.day_bloomed == daybloomed):
          print("Bloom date: ",j.day_bloomed, " Common Name: ",i.common_name," Latin Name: ",i.latin_name, " Color: ", i.color, " Notes: ", i.notes)
          return (j.day_bloomed,i.common_name, i.latin_name, i.color, )
  database.close()

def getAllPlantsByLocation(loc):
   database.connect()
   for j,i in zip(Location,Plant):
       if (j.quadrant == loc):
          print("Location - Quadrant:", j.quadrant, " Common Name: ",i.common_name," Latin Name: ",i.latin_name, " Color: ", i.color, " Notes: ", i.notes)
          return (j.quadrant,i.common_name, i.latin_name, i.color )
   database.close()

def getAllPlantsByRarity(rar):
   database.connect()
   for j,i in zip(Rarity,Plant):
       if (j.rarity == rar):
           print("Rarity: ", j.rarity, " Common Name: ",i.common_name," Latin Name: ",i.latin_name, " Color: ", i.color, " Notes: ", i.notes)
           return (j.rarity,i.common_name, i.latin_name, i.color, i.notes)
   database.close()	

def getPlant(key):
        database.connect()
        plant = Plant.get(key)
        return plant.common_name + " " + plant.latin_name + " "+ plant.notes
        database.close()


'''takes in column name, value to be changed, and key used to locate row to be changed'''
def update(column,value,key):
    database.connect()
    if column=='common_name':
        (Plant.update(common_name = value).where(Plant.plant_key == key)).execute()
    if column=='latin_name':
        (Plant.update(latin_name = value).where(Plant.plant_key == key)).execute()
    if column=='color':
        (Plant.update(color = value).where(Plant.plant_key == key)).execute()
    if column=='notes':
        (Plant.update(notes = value).where(Plant.plant_key == key)).execute()
    database.close()


