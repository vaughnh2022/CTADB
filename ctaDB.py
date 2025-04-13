from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
connection_url="your connection here"
client = MongoClient(connection_url)
db = client["comp_353"]


#define train class in python with save functions
class Train:
    def __init__(self,tID,tStopNum):
        self.tID = tID
        self.tStopNum = tStopNum
    
    def save(self):
        train_data = {
            "tID": self.tID,
            "tStopNum" : self.tStopNum
        }
        db.train.insert_one(train_data)

# tId, tStopNum
trains = [
    Train("R1",5),
    Train("R2",5),
    Train("B1",4),
    Train("B2",4),
    Train("Y1",3)
]

# saves train insertions
for train in trains:
    train.save()
        

#define station class in python with init and save functions
class Station:
    def __init__(self, sName, sAccessibility, sTransfer):
        self.sName = sName
        self.sAccessibility = sAccessibility
        self.sTransfer = sTransfer

    def save(self):
        station_data = {
            "sName": self.sName,
            "sAccessibility": self.sAccessibility,
            "sTransfer": self.sTransfer
        }
        db.station.insert_one(station_data)

# sName,SAccessability,sTransfer
stations = [
    Station("Howard", True, {"bus": False, "train": True}),
    Station("Loyola", True, {"bus": False, "train": False}),
    Station("Oakton-Skokie", False, {"bus": False, "train": False}),
    Station("Dempster-Skokie", True, {"bus": False, "train": False}),
    Station("O'Hare", False, {"bus": False, "train": False}),
    Station("Wilson", False, {"bus": False, "train": False}),
    Station("Lake", False, {"bus": False, "train": False}),
    Station("Belmont", False, {"bus": False, "train": False}),
    Station("Damen", False, {"bus": False, "train": False}),
    Station("Irving Park", False, {"bus": False, "train": False}),
]

# saves station insertions
for station in stations:
    station.save()


#define train_schedule class in python with init and save function
class train_schedule:
    def __init__(self, tDirection, tColor, tID, tRoute, tArrivalTime, tDepartureTime):
        self.tDirection = tDirection
        self.tColor = tColor
        self.tID = tID
        self.tRoute = tRoute
        self.tArrivalTime = tArrivalTime
        self.tDepartureTime = tDepartureTime

    def save(self):
        schedule_data = {
            "tDirection": self.tDirection,
            "tColor": self.tColor,
            "tID": self.tID,
            "tRoute": self.tRoute,
            "tArrivalTime": self.tArrivalTime,
            "tDepartureTime": self.tDepartureTime
        }
        db.train_schedule.insert_one(schedule_data)

# Define train schedule data
train_schedules = [
    train_schedule(
        "northwest", "yellow", "Y1",
        [{"sName": "Howard"}, {"sName": "Oakton-Skokie"}, {"sName": "Dempster-Skokie"}],
        [datetime(2025, 4, 14, 12, 10), datetime(2025, 4, 14, 12, 25), datetime(2025, 4, 14, 12, 40)],
        [datetime(2025, 4, 14, 12, 15), datetime(2025, 4, 14, 12, 30), datetime(2025, 4, 14, 12, 45)]
    ),
    train_schedule(
        "south", "red", "R1",
        [{"sName": "Howard"}, {"sName": "Loyola"}, {"sName": "Wilson"}, {"sName": "Belmont"}, {"sName": "Lake"}],
        [datetime(2025, 4, 14, 12, 10), datetime(2025, 4, 14, 12, 25), datetime(2025, 4, 14, 12, 40),
         datetime(2025, 4, 14, 12, 55), datetime(2025, 4, 14, 12, 10)],
        [datetime(2025, 4, 14, 12, 15), datetime(2025, 4, 14, 12, 30), datetime(2025, 4, 14, 12, 45),
         datetime(2025, 4, 14, 13, 0), datetime(2025, 4, 14, 13, 15)]
    ),
    train_schedule(
        "north", "red", "R2",
        [{"sName": "Lake"}, {"sName": "Belmont"}, {"sName": "Wilson"}, {"sName": "Loyola"}, {"sName": "Howard"}],
        [datetime(2025, 4, 14, 12, 5), datetime(2025, 4, 14, 12, 20), datetime(2025, 4, 14, 12, 35),
         datetime(2025, 4, 14, 12, 50), datetime(2025, 4, 14, 13, 5)],
        [datetime(2025, 4, 14, 12, 10), datetime(2025, 4, 14, 12, 25), datetime(2025, 4, 14, 12, 40),
         datetime(2025, 4, 14, 12, 55), datetime(2025, 4, 14, 13, 10)]
    ),
    train_schedule(
        "west", "blue", "B1",
        [{"sName": "Lake"}, {"sName": "Damen"}, {"sName": "Irving Park"}, {"sName": "O'Hare"}],
        [datetime(2025, 4, 14, 12, 30), datetime(2025, 4, 14, 12, 45), datetime(2025, 4, 14, 13, 0), datetime(2025, 4, 14, 13, 15)],
        [datetime(2025, 4, 14, 12, 35), datetime(2025, 4, 14, 12, 50), datetime(2025, 4, 14, 13, 5), datetime(2025, 4, 14, 13, 20)]
    ),
    train_schedule(
        "east", "blue", "B2",
        [{"sName": "O'Hare"}, {"sName": "Irving Park"}, {"sName": "Damen"}, {"sName": "Lake"}],
        [datetime(2025, 4, 14, 11, 50), datetime(2025, 4, 14, 12, 5), datetime(2025, 4, 14, 12, 20), datetime(2025, 4, 14, 12, 35)],
        [datetime(2025, 4, 14, 11, 55), datetime(2025, 4, 14, 12, 10), datetime(2025, 4, 14, 12, 25), datetime(2025, 4, 14, 12, 40)]
    ),
]

# Save train_schedule insertions
for schedule in train_schedules:
    schedule.save()

train_data = db.train_schedule.find_one({"tID": "R1"})
print(train_data)