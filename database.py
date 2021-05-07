from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, FloatProperty, UniqueIdProperty, RelationshipTo)
config.DATABASE_URL = 'bolt://neo4j:neo@localhost:7687'  # default
config.AUTO_INSTALL_LABELS = True

class Grape_Varietal(StructuredNode):
    name = StringProperty(unique_index=True)

class Color(StructuredNode):
    name = StringProperty(unique_index=True)
    mainType = StringProperty()

class Mouthfeel(StructuredNode):
    name = StringProperty(unique_index=True)

class Descriptor(StructuredNode):
    name = StringProperty(unique_index=True)

class Wine_Type(StructuredNode):
    name = StringProperty(unique_index=True)

class Country(StructuredNode):
    name = StringProperty(unique_index=True)

class Region(StructuredNode):
    name = StringProperty(unique_index=True)
    climate = StringProperty()
    isFromCountry = RelationshipTo(Country, 'FROM_COUNTRY')

class Wine(StructuredNode):
    name = StringProperty(unique_index=True)
    year = StringProperty()
    abv = FloatProperty()
    hasAroma = RelationshipTo(Descriptor, 'HAS_AROMA')
    hasFlavor = RelationshipTo(Descriptor, 'HAS_FLAVOR')
    hasColor = RelationshipTo(Color, 'HAS_COLOR')
    hasMouthfeel = RelationshipTo(Mouthfeel, 'HAS_MOUTHFEEL')
    isWineType = RelationshipTo(Wine_Type, 'IS_TYPE')
    hasGrapeVarietal = RelationshipTo(Grape_Varietal, 'HAS_GRAPE_VARIETAL')

class Producer(StructuredNode):
    name = StringProperty(unique_index=True)
    acreage = IntegerProperty()
    isFromRegion = RelationshipTo(Region, 'FROM_REGION')
    produced = RelationshipTo(Wine, "PRODUCED")

# Seed some data
blackcurrant = Descriptor(name="BLACKCURRANT").save()
cherry= Descriptor(name="CHERRY").save()
blackberry= Descriptor(name="BLACKBERRY").save()
leather= Descriptor(name="LEATHER").save()
vanilla= Descriptor(name="VANILLA").save()
tobacco= Descriptor(name="TOBACCO").save()
newGrapeVarietal = Grape_Varietal(name="PINOT NOIR").save()
newColor = Color(name="DARK RUBY", mainType="RED").save()
newMouthfeel = Mouthfeel(name="FULL").save()
newWineType = Wine_Type(name="PINOT_NOIR").save()
newCountry = Country(name="UNITED STATES").save()
newRegion = Region(name="TEXAS HILL COUNTRY", climate="ARID").save()
newRegion.isFromCountry.connect(newCountry)
newProducer = Producer(name="Westwick Winery", acreage=100).save()
newProducer.isFromRegion.connect(newRegion)
newWine = Wine(
    name="First Vintage",
    year="2016",
    abv=12.6
).save()
newWine.hasAroma.connect(cherry)
newWine.hasAroma.connect(leather)
newWine.hasAroma.connect(blackcurrant)
newWine.hasFlavor.connect(cherry)
newWine.hasFlavor.connect(blackberry)
newWine.hasFlavor.connect(vanilla)
newWine.hasFlavor.connect(tobacco)
newWine.hasColor.connect(newColor)
newWine.hasMouthfeel.connect(newMouthfeel)
newWine.isWineType.connect(newWineType)
newWine.hasGrapeVarietal.connect(newGrapeVarietal)
newProducer.produced.connect(newWine)

allWines = Wine.nodes.all()
print(allWines)