import mysql.connector
from datetime import datetime
from datetime import timedelta
import random

def loadHome():
	coordX = 40.463479
	coordY = -79.935727
	accel = 0.0
	orient = 2
	
def loadCMU1():
	coordX = 40.443776
	coordY = -79.946309
	accel = 0.0
	orient = 1
	
def loadCMU2():
	coordX = 40.440762
	coordY = -79.942983
	accel = 0.0
	orient = 1
	
def dbWrite(dataID, user, clusterID, coordX, coordY, accel, orient, day):
	sql = "INSERT INTO sensorData VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	pullTime = datetime.now() + timedelta(minutes=(1*dataID))
	val = (dataID, user, clusterID,  coordX, coordY, accel, orient, pullTime, day)
	mycursor.execute(sql, val)
	mydb.commit()
	
def loadMonday():
	coordX = 40.463479
	coordY = -79.935727
	accel = 0.0
	orient = 2

	for dataID in range(0, 526):
		xRand = random.uniform(-0.00001, 0.00001)
		yRand = random.uniform(-0.00001, 0.00001)
		coordX = coordX+xRand
		coordY = coordY+yRand

		print("before")
		dbWrite(dataID, "testUser", -1, coordX, coordY, 0.0, orient, "Wednesday")
		print("after")
		
	randAcc = random.uniform(-1,1)
	dbWrite(527, "testUser", -1, 40.462666, -79.934674, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(528, "testUser", -1, 40.461931, -79.931629, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(529, "testUser", -1, 40.458568, -79.933681, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(530, "testUser", -1, 40.456049, -79.933352, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(531, "testUser", -1, 40.452743, -79.936702, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(532, "testUser", -1, 40.450882, -79.943028, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(533, "testUser", -1, 40.447453, -79.942476, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(534, "testUser", -1, 40.444649, -79.943049, randAcc, orient, "Wednesday")

	coordX = 40.440762
	coordY = -79.942983
	orient = 1
	for dataID in range(535, 735):
		xRand = random.uniform(-0.00001, 0.00001)
		yRand = random.uniform(-0.00001, 0.00001)
		coordX += xRand
		coordY += yRand
			
		dbWrite(dataID, "testUser", -1, coordX, coordY, 0.0, orient, "Wednesday")
		
	randAcc = random.uniform(-1,1)
	dbWrite(736, "testUser", -1, 40.443537, -79.944951, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(737, "testUser", -1, 40.442932, -79.945362, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(738, "testUser", -1, 40.442069, -79.947187, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(739, "testUser", -1, 40.441048, -79.945002, randAcc, orient, "Wednesday")

	coordX = 40.440762
	coordY = -79.942983
	accel = 0.0
	orient = 1

	for dataID in range(740, 1022):
		xRand = random.uniform(-0.00001, 0.00001)
		yRand = random.uniform(-0.00001, 0.00001)
		coordX += xRand
		coordY += yRand
			
		dbWrite(dataID, "testUser", -1, coordX, coordY, 0.0, orient, "Wednesday")
		
	randAcc = random.uniform(-1,1)
	dbWrite(1023, "testUser", -1, 40.441404, -79.944100, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(1024, "testUser", -1, 40.444507, -79.942532, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(1025, "testUser", -1, 40.446035, -79.942241, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(1026, "testUser", -1, 40.447433, -79.942454, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(1027, "testUser", -1, 40.450898, -79.942994, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(1028, "testUser", -1, 40.451890, -79.939232, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(1029, "testUser", -1, 40.453109, -79.936039, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(1030, "testUser", -1, 40.454776, -79.932564, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(1031, "testUser", -1, 40.456723, -79.933753, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(1032, "testUser", -1, 40.459430, -79.933184, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(1033, "testUser", -1, 40.461986, -79.931695, randAcc, orient, "Wednesday")
	randAcc = random.uniform(-1,1)
	dbWrite(1034, "testUser", -1, 40.462533, -79.934148, randAcc, orient, "Wednesday")

	coordX = 40.463479
	coordY = -79.935727
	accel = 0.0
	orient = 2

	for dataID in range(1035, 1439):
		xRand = random.uniform(-0.00001, 0.00001)
		yRand = random.uniform(-0.00001, 0.00001)
		coordX = coordX+xRand
		coordY = coordY+yRand
			
		dbWrite(dataID, "testUser", -1, coordX, coordY, 0.0, orient, "Wednesday")

mydb = mysql.connector.connect(
	host="satellitesidecaruserhistory.c701a5j4aycw.us-east-1.rds.amazonaws.com",
	user="admin",
	passwd="design2019",
	database="ssHistory"
)

mycursor = mydb.cursor()

loadMonday()