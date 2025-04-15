from pymongo import MongoClient
from datetime import datetime
import pymongo

# Connect to MongoDB
connection_url="your_url_here"
client = MongoClient(connection_url)
db = client["comp_353_5"]


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
for train_save in trains:
    train_save.save()
        

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
    Station("Howard", True, {"bus": True, "train": True}),
    Station("Loyola", True, {"bus": False, "train": False}),
    Station("Oakton-Skokie", False, {"bus": False, "train": False}),
    Station("Dempster-Skokie", True, {"bus": True, "train": False}),
    Station("O'Hare", False, {"bus": True, "train": False}),
    Station("Wilson", False, {"bus": False, "train": False}),
    Station("Lake", False, {"bus": False, "train": True}),
    Station("Belmont", False, {"bus": True, "train": False}),
    Station("Damen", False, {"bus": False, "train": False}),
    Station("Irving Park", False, {"bus": True, "train": False}),
]

# saves station insertions
for station_save in stations:
    station_save.save()


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
        train_schedule_data = {
            "tDirection": self.tDirection,
            "tColor": self.tColor,
            "tID": self.tID,
            "tRoute": self.tRoute,
            "tArrivalTime": self.tArrivalTime,
            "tDepartureTime": self.tDepartureTime
        }
        db.train_schedule.insert_one(train_schedule_data)

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
    )
]

# Save train_schedule insertions
for schedule_save in train_schedules:
    schedule_save.save()

#define train class in python with save functions
class bus:
    def __init__(self,bID,bStopNum):
        self.bID = bID
        self.bStopNum = bStopNum
    
    def save(self):
        bus_data = {
            "bID": self.bID,
            "bStopNum" : self.bStopNum
        }
        db.bus.insert_one(bus_data)

# tId, tStopNum
buses = [
    bus("001",3),
    bus("002",3),
    bus("003",2),
    bus("004",2)
]

# saves train insertions
for bus_save in buses:
    bus_save.save()



#define bus_schedule class in python with init and save function
class bus_schedule:
    def __init__(self, bDirection,  bID, bNum, bRoute, bArrivalTime, bDepartureTime):
        self.bDirection = bDirection
        self.bID = bID
        self.bNum = bNum
        self.bRoute = bRoute
        self.bArrivalTime = bArrivalTime
        self.bDepartureTime = bDepartureTime

    def save(self):
        bus_schedule_data = {
            "bDirection": self.bDirection,
            "bID": self.bID,
            "bNum": self.bNum,
            "bRoute": self.bRoute,
            "bArrivalTime": self.bArrivalTime,
            "bDepartureTime": self.bDepartureTime
        }
        db.bus_schedule.insert_one(bus_schedule_data)

# Define bus schedule data
bus_schedules = [
    bus_schedule(
        "west", "001","155",
        [{"sName": "Howard"}, {"sName": "Dempster-Skokie"}, {"sName": "O'Hare"}],
        [datetime(2025, 4, 14, 12, 10), datetime(2025, 4, 14, 12, 25), datetime(2025, 4, 14, 13, 10)],
        [datetime(2025, 4, 14, 12, 12), datetime(2025, 4, 14, 12, 27), datetime(2025, 4, 14, 13, 12)]
    ),
    bus_schedule(
        "east", "002","155",
        [{"sName": "O'Hare"}, {"sName": "Dempster-Skokie"}, {"sName": "Howard"}],
        [datetime(2025, 4, 14, 10, 15), datetime(2025, 4, 14, 10, 55), datetime(2025, 4, 14, 11, 10)],
        [datetime(2025, 4, 14, 10, 18), datetime(2025, 4, 14, 10, 57), datetime(2025, 4, 14, 11, 12)]
    ),
    bus_schedule(
        "west", "003","274",
        [{"sName": "Belmont"}, {"sName": "Irving Park"}],
        [datetime(2025, 4, 14, 13, 15), datetime(2025, 4, 14, 13, 37)],
        [datetime(2025, 4, 14, 13, 18), datetime(2025, 4, 14, 10, 39)]
    ),
    bus_schedule(
        "east", "004","274",
        [{"sName": "Irving Park"}, {"sName": "Belmont"}],
        [datetime(2025, 4, 14, 12, 5), datetime(2025, 4, 14, 10, 33)],
        [datetime(2025, 4, 14, 12, 8), datetime(2025, 4, 14, 10, 35)]
    )
]

# Save bus_schedule insertions
for schedule_save in bus_schedules:
    schedule_save.save()


#define passenger class in python with save functions
class Passenger:
    def __init__(self, pName,pBalance, pCurrentStation, pPreviousStation):
        self.pBalance = pBalance
        self.pName = pName
        self.pCurrentStation = pCurrentStation
        self.pPreviousStation = pPreviousStation

    def save(self):
        passenger_data = {
            "pBalance": self.pBalance,
            "pName": self.pName,
            "pCurrentStation": self.pCurrentStation,
            "pPreviousStation": self.pPreviousStation
        }
        db.passenger.insert_one(passenger_data)


# Define passenger data
passengers = [
    Passenger("Arthur Morgan", 50, [
            {"sName": "Howard"},datetime(2025, 4, 14, 21, 55)
        ], [
            {"sName": "Loyola"},datetime(2025, 4, 13, 21, 55)
        ]
    ),
    Passenger("Mark Zuckerberg", 10, [
            {"sName": "Lake"},datetime(2025, 4, 14, 21, 55)
        ], [

        ]
    ),
    Passenger("Charlie Brown", 76,
            None,
        [
            [{"sName": "O'Hare"},datetime(2025, 4, 13, 21, 55)],
            [{"sName": "Damen"}, datetime(2025, 4, 12, 21, 55)]
        ]
    ),
    Passenger("Jane Doe", 22, [
            {"sName": "Belmont"},datetime(2025, 4, 14, 21, 55)
        ], [
            [{"sName": "Loyola"}, datetime(2025, 4, 13, 21, 55)],
            [{"sName": "Lake"}, datetime(2025, 4, 12, 21, 55)]
        ]
    ),
    Passenger("John Smith", 13, [
            {"sName": "O'Hare"},datetime(2025, 4, 14, 21, 55)
        ], [
            [{"sName": "Damen"}, datetime(2025, 4, 13, 21, 55)]
        ]
    ),
    Passenger("Emma Watson", 31, [
            {"sName": "Irving Park"},datetime(2025, 4, 14, 21, 55)
        ], [
            [{"sName": "O'Hare"}, datetime(2025, 4, 13, 21, 55)]
        ]
    ),
    Passenger("Bruce Wayne", 10, [
            {"sName": "Howard"},datetime(2025, 4, 14, 21, 55)
        ], [
            [{"sName": "Loyola"}, datetime(2025, 4, 13, 21, 55)],
            [{"sName": "Lake"}, datetime(2025, 4, 12, 21, 55)]
        ]
    ),
    Passenger("Clark Kent", 6, [
            {"sName": "Oakton-Skokie"},datetime(2025, 4, 14, 21, 55)
        ], [
            [{"sName": "Dempster-Skokie"}, datetime(2025, 4, 13, 21, 55)],
            [{"sName": "Howard"}, datetime(2025, 4, 12, 21, 55)],
            [{"sName": "Lake"}, datetime(2025, 4, 11, 21, 55)]
        ]
    )
]

# Save passenger insertions
for passenger_save in passengers:
    passenger_save.save()

def passengers_currently_in_a_station():
    pipeline = [
        {"$match": {"pCurrentStation": {"$ne": None}}},
        {"$project": {"pName": 1,"pBalance": 1,"stationName": {"$arrayElemAt": ["$pCurrentStation.sName", 0]}}},
        {"$lookup": {"from": "station","localField": "stationName","foreignField": "sName","as": "station_info"}},
        {"$project": {"_id": 0,"name": "$pName","balance": "$pBalance","current_station": "$stationName", "station_info.sTransfer": 1,
        "can_transfer_to_bus": "$stationInfo.sTransfer.bus","can_transfer_to_train": "$stationInfo.sTransfer.train"}},
        {"$sort": {"current_station": 1,"name": 1}}
    ]

    results = list(db.passenger.aggregate(pipeline))
    # Print the results
    print("Passengers that are currently in a station and their possibility for a transfer\n")
    for p in results:
        print("Name is ",p['name'])
        print("",p["name"],"'s current station is",p['current_station'])
        sTransfer=p['station_info'][0]['sTransfer']
        bus_transfer = "Available" if sTransfer['bus'] else "Not Available"
        train_transfer = "Available" if sTransfer['train'] else "Not Available"
        print("Bus transfer is ", bus_transfer," and train transfer is ",train_transfer)
        print("-----------------------------------------------------------")

def getTrainsAndBussesBetweenTime(start, end):
    print("\n##### These are the Trains and busses that are scheduled between the times #####\n--",start, "--\nand\n--", end,"--")
    # Query train schedules in this window
    train_schedules = db.train_schedule.find({
        "tDepartureTime": {
            "$elemMatch": {
                "$gte": start_time,
                "$lte": end_time
            }
        }
    })
    # Query bus schedules in this window
    bus_schedules = db.bus_schedule.find({
        "bDepartureTime": {
            "$elemMatch": {
                "$gte": start_time,
                "$lte": end_time
            }
        }
    })
    # Prints results
    print("Train schedules between 12:00 PM and 1:00 PM:")
    for schedule in train_schedules:
        print(f"Train {schedule['tID']} ({schedule['tColor']} line) going {schedule['tDirection']}")
    print("\nBus schedules between 12:00 PM and 1:00 PM:")
    for schedule in bus_schedules:
        print(f"Bus {schedule['bID']} (Route {schedule['bRoute']}) going {schedule['bDirection']}")
    print()


start_time = datetime(2025, 4, 14, 12, 0)  # 12:00 PM
end_time = datetime(2025, 4, 14, 13, 0)    # 1:00 PM

getTrainsAndBussesBetweenTime(start_time,end_time)
passengers_currently_in_a_station()

    
        


