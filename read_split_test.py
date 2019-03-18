import mysql.connector
import math
import numpy as np
from numpy import linalg
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D

PI = math.pi

def f_lookup(r, c):
	table = [[161.4476,
	199.5000,
	215.7073,
	224.5832,
	230.1619,
	233.9860,
	236.7684,
	238.8827,
	240.5433,
	241.8817,
	243.9060,
	245.9499,
	248.0131,
	249.0518,
	250.0951,
	251.1432,
	252.1957,
	253.2529,
	254.3144],
	[18.5128,
	19.0000,
	19.1643,
	19.2468,
	19.2964,
	19.3295,
	19.3532,
	19.3710,
	19.3848,
	19.3959,
	19.4125,
	19.4291,
	19.4458,
	19.4541,
	19.4624,
	19.4707,
	19.4791,
	19.4874,
	19.4957],
	[10.1280,
	9.5521,
	9.2766,
	9.1172,
	9.0135,
	8.9406,
	8.8867,
	8.8452,
	8.8123,
	8.7855,
	8.7446,
	8.7029,
	8.6602,
	8.6385,
	8.6166,
	8.5944,
	8.5720,
	8.5494,
	8.5264],
	[7.7086,
	6.9443,
	6.5914,
	6.3882,
	6.2561,
	6.1631,
	6.0942,
	6.0410,
	5.9988,
	5.9644,
	5.9117,
	5.8578,
	5.8025,
	5.7744,
	5.7459,
	5.7170,
	5.6877,
	5.6581,
	5.6281],
	[6.6079,
	5.7861,
	5.4095,
	5.1922,
	5.0503,
	4.9503,
	4.8759,
	4.8183,
	4.7725,
	4.7351,
	4.6777,
	4.6188,
	4.5581,
	4.5272,
	4.4957,
	4.4638,
	4.4314,
	4.3985,
	4.3650],
	[5.9874,
	5.1433,
	4.7571,
	4.5337,
	4.3874,
	4.2839,
	4.2067,
	4.1468,
	4.0990,
	4.0600,
	3.9999,
	3.9381,
	3.8742,
	3.8415,
	3.8082,
	3.7743,
	3.7398,
	3.7047,
	3.6689],
	[5.5914,
	4.7374,
	4.3468,
	4.1203,
	3.9715,
	3.8660,
	3.7870,
	3.7257,
	3.6767,
	3.6365,
	3.5747,
	3.5107,
	3.4445,
	3.4105,
	3.3758,
	3.3404,
	3.3043,
	3.2674,
	3.2298],
	[5.3177,
	4.4590,
	4.0662,
	3.8379,
	3.6875,
	3.5806,
	3.5005,
	3.4381,
	3.3881,
	3.3472,
	3.2839,
	3.2184,
	3.1503,
	3.1152,
	3.0794,
	3.0428,
	3.0053,
	2.9669,
	2.9276],
	[5.1174,
	4.2565,
	3.8625,
	3.6331,
	3.4817,
	3.3738,
	3.2927,
	3.2296,
	3.1789,
	3.1373,
	3.0729,
	3.0061,
	2.9365,
	2.9005,
	2.8637,
	2.8259,
	2.7872,
	2.7475,
	2.7067],
	[4.9646,
	4.1028,
	3.7083,
	3.4780,
	3.3258,
	3.2172,
	3.1355,
	3.0717,
	3.0204,
	2.9782,
	2.9130,
	2.8450,
	2.7740,
	2.7372,
	2.6996,
	2.6609,
	2.6211,
	2.5801,
	2.5379],
	[4.8443,
	3.9823,
	3.5874,
	3.3567,
	3.2039,
	3.0946,
	3.0123,
	2.9480,
	2.8962,
	2.8536,
	2.7876,
	2.7186,
	2.6464,
	2.6090,
	2.5705,
	2.5309,
	2.4901,
	2.4480,
	2.4045],
	[4.7472,
	3.8853,
	3.4903,
	3.2592,
	3.1059,
	2.9961,
	2.9134,
	2.8486,
	2.7964,
	2.7534,
	2.6866,
	2.6169,
	2.5436,
	2.5055,
	2.4663,
	2.4259,
	2.3842,
	2.3410,
	2.2962],
	[4.6672,
	3.8056,
	3.4105,
	3.1791,
	3.0254,
	2.9153,
	2.8321,
	2.7669,
	2.7144,
	2.6710,
	2.6037,
	2.5331,
	2.4589,
	2.4202,
	2.3803,
	2.3392,
	2.2966,
	2.2524,
	2.2064],
	[4.6001,
	3.7389,
	3.3439,
	3.1122,
	2.9582,
	2.8477,
	2.7642,
	2.6987,
	2.6458,
	2.6022,
	2.5342,
	2.4630,
	2.3879,
	2.3487,
	2.3082,
	2.2664,
	2.2229,
	2.1778,
	2.1307],
	[4.5431,
	3.6823,
	3.2874,
	3.0556,
	2.9013,
	2.7905,
	2.7066,
	2.6408,
	2.5876,
	2.5437,
	2.4753,
	2.4034,
	2.3275,
	2.2878,
	2.2468,
	2.2043,
	2.1601,
	2.1141,
	2.0658],
	[4.4940,
	3.6337,
	3.2389,
	3.0069,
	2.8524,
	2.7413,
	2.6572,
	2.5911,
	2.5377,
	2.4935,
	2.4247,
	2.3522,
	2.2756,
	2.2354,
	2.1938,
	2.1507,
	2.1058,
	2.0589,
	2.0096],
	[4.4513,
	3.5915,
	3.1968,
	2.9647,
	2.8100,
	2.6987,
	2.6143,
	2.5480,
	2.4943,
	2.4499,
	2.3807,
	2.3077,
	2.2304,
	2.1898,
	2.1477,
	2.1040,
	2.0584,
	2.0107,
	1.9604],
	[4.4139,
	3.5546,
	3.1599,
	2.9277,
	2.7729,
	2.6613,
	2.5767,
	2.5102,
	2.4563,
	2.4117,
	2.3421,
	2.2686,
	2.1906,
	2.1497,
	2.1071,
	2.0629,
	2.0166,
	1.9681,
	1.9168],
	[4.3807,
	3.5219,
	3.1274,
	2.8951,
	2.7401,
	2.6283,
	2.5435,
	2.4768,
	2.4227,
	2.3779,
	2.3080,
	2.2341,
	2.1555,
	2.1141,
	2.0712,
	2.0264,
	1.9795,
	1.9302,
	1.8780],
	[4.3512,
	3.4928,
	3.0984,
	2.8661,
	2.7109,
	2.5990,
	2.5140,
	2.4471,
	2.3928,
	2.3479,
	2.2776,
	2.2033,
	2.1242,
	2.0825,
	2.0391,
	1.9938,
	1.9464,
	1.8963,
	1.8432],
	[4.3248,
	3.4668,
	3.0725,
	2.8401,
	2.6848,
	2.5727,
	2.4876,
	2.4205,
	2.3660,
	2.3210,
	2.2504,
	2.1757,
	2.0960,
	2.0540,
	2.0102,
	1.9645,
	1.9165,
	1.8657,
	1.8117],
	[4.3009,
	3.4434,
	3.0491,
	2.8167,
	2.6613,
	2.5491,
	2.4638,
	2.3965,
	2.3419,
	2.2967,
	2.2258,
	2.1508,
	2.0707,
	2.0283,
	1.9842,
	1.9380,
	1.8894,
	1.8380,
	1.7831],
	[4.2793,
	3.4221,
	3.0280,
	2.7955,
	2.6400,
	2.5277,
	2.4422,
	2.3748,
	2.3201,
	2.2747,
	2.2036,
	2.1282,
	2.0476,
	2.0050,
	1.9605,
	1.9139,
	1.8648,
	1.8128,
	1.7570],
	[4.2597,
	3.4028,
	3.0088,
	2.7763,
	2.6207,
	2.5082,
	2.4226,
	2.3551,
	2.3002,
	2.2547,
	2.1834,
	2.1077,
	2.0267,
	1.9838,
	1.9390,
	1.8920,
	1.8424,
	1.7896,
	1.7330],
	[4.2417,
	3.3852,
	2.9912,
	2.7587,
	2.6030,
	2.4904,
	2.4047,
	2.3371,
	2.2821,
	2.2365,
	2.1649,
	2.0889,
	2.0075,
	1.9643,
	1.9192,
	1.8718,
	1.8217,
	1.7684,
	1.7110],
	[4.2252,
	3.3690,
	2.9752,
	2.7426,
	2.5868,
	2.4741,
	2.3883,
	2.3205,
	2.2655,
	2.2197,
	2.1479,
	2.0716,
	1.9898,
	1.9464,
	1.9010,
	1.8533,
	1.8027,
	1.7488,
	1.6906],
	[4.2100,
	3.3541,
	2.9604,
	2.7278,
	2.5719,
	2.4591,
	2.3732,
	2.3053,
	2.2501,
	2.2043,
	2.1323,
	2.0558,
	1.9736,
	1.9299,
	1.8842,
	1.8361,
	1.7851,
	1.7306,
	1.6717],
	[4.1960,
	3.3404,
	2.9467,
	2.7141,
	2.5581,
	2.4453,
	2.3593,
	2.2913,
	2.2360,
	2.1900,
	2.1179,
	2.0411,
	1.9586,
	1.9147,
	1.8687,
	1.8203,
	1.7689,
	1.7138,
	1.6541],
	[4.1830,
	3.3277,
	2.9340,
	2.7014,
	2.5454,
	2.4324,
	2.3463,
	2.2783,
	2.2229,
	2.1768,
	2.1045,
	2.0275,
	1.9446,
	1.9005,
	1.8543,
	1.8055,
	1.7537,
	1.6981,
	1.6376],
	[4.1709,
	3.3158,
	2.9223,
	2.6896,
	2.5336,
	2.4205,
	2.3343,
	2.2662,
	2.2107,
	2.1646,
	2.0921,
	2.0148,
	1.9317,
	1.8874,
	1.8409,
	1.7918,
	1.7396,
	1.6835,
	1.6223],
	[4.0847,
	3.2317,
	2.8387,
	2.6060,
	2.4495,
	2.3359,
	2.2490,
	2.1802,
	2.1240,
	2.0772,
	2.0035,
	1.9245,
	1.8389,
	1.7929,
	1.7444,
	1.6928,
	1.6373,
	1.5766,
	1.5089],
	[4.0012,
	3.1504,
	2.7581,
	2.5252,
	2.3683,
	2.2541,
	2.1665,
	2.0970,
	2.0401,
	1.9926,
	1.9174,
	1.8364,
	1.7480,
	1.7001,
	1.6491,
	1.5943,
	1.5343,
	1.4673,
	1.3893],
	[3.9201,
	3.0718,
	2.6802,
	2.4472,
	2.2899,
	2.1750,
	2.0868,
	2.0164,
	1.9588,
	1.9105,
	1.8337,
	1.7505,
	1.6587,
	1.6084,
	1.5543,
	1.4952,
	1.4290,
	1.3519,
	1.2539],
	[3.8415,
	2.9957,
	2.6049,
	2.3719,
	2.2141,
	2.0986,
	2.0096,
	1.9384,
	1.8799,
	1.8307,
	1.7522,
	1.6664,
	1.5705,
	1.5173,
	1.4591,
	1.3940,
	1.3180,
	1.2214,
	1.0000]]

	if(r <= 30):
		if((c <= 11)):
			return table[r-1][c-1]
		if(c < 15):
			return table[r-1][10]
		if(c <= 20):
			return table[r-1][11]
		if(c <= 24):
			return table[r-1][12]
		if(c < 30):
			return table[r-1][13]
		if (c < 40):
			return table[r-1][14]
		if (c < 60):
			return table[r-1][15]
		if (c < 120):
			return table[r-1][16]
		return table[r-1][17]
	elif(r < 40):
		if ((c <= 11)):
			return table[29][c - 1]
		if (c < 15):
			return table[29][10]
		if (c <= 20):
			return table[29][11]
		if (c <= 24):
			return table[29][12]
		if (c < 30):
			return table[29][13]
		if (c < 40):
			return table[29][14]
		if (c < 60):
			return table[29][15]
		if (c < 120):
			return table[29][16]
		return table[29][17]
	elif (r < 60):
		if ((c <= 11)):
			return table[30][c - 1]
		if (c < 15):
			return table[30][10]
		if (c <= 20):
			return table[30][11]
		if (c <= 24):
			return table[30][12]
		if (c < 30):
			return table[30][13]
		if (c < 40):
			return table[30][14]
		if (c < 60):
			return table[30][15]
		if (c < 120):
			return table[30][16]
		return table[30][17]
	elif (r < 120):
		if ((c <= 11)):
			return table[31][c - 1]
		if (c < 15):
			return table[31][10]
		if (c <= 20):
			return table[31][11]
		if (c <= 24):
			return table[31][12]
		if (c < 30):
			return table[31][13]
		if (c < 40):
			return table[31][14]
		if (c < 60):
			return table[31][15]
		if (c < 120):
			return table[31][16]
		return table[31][17]
	else:
		if ((c <= 11)):
			return table[32][c - 1]
		if (c < 15):
			return table[32][10]
		if (c <= 20):
			return table[32][11]
		if (c <= 24):
			return table[32][12]
		if (c < 30):
			return table[32][13]
		if (c < 40):
			return table[32][14]
		if (c < 60):
			return table[32][15]
		if (c < 120):
			return table[32][16]
		return table[32][17]


mydb = mysql.connector.connect(
	host="satellitesidecaruserhistory.c701a5j4aycw.us-east-1.rds.amazonaws.com",
	user="admin",
	passwd="design2019",
	database="ssHistory"
)

mycursor = mydb.cursor()

def mvn_confidence(pop, means, covarMat, newMeans):
	meanDiffMat = [[means[0][0] - newMeans[0][0]], [means[1][0] - newMeans[1][0]]]
	#print("Heck: ", meanDiffMat)
	matMultOne = np.matmul(np.transpose(meanDiffMat), np.linalg.inv(covarMat))
	matMultTwo = np.matmul(matMultOne, meanDiffMat)
	firstCompare = pop*matMultTwo

	fVal = f_lookup(pop-2, 2)
	#print("FVal: ", fVal)
	secondCompare = ((pop-1)*2)/(pop-2)*fVal

	#print(firstCompare)
	#print(secondCompare)

	conf = 1/(firstCompare / (secondCompare / 100.0))

	if(firstCompare > secondCompare):
		return [0, conf] #print("Greater")
	else:
		return [1, conf] #print("Lesser")

def select_from_window(stringWindowStart, stringWindowEnd):
	sql = "SELECT * FROM sensorData WHERE dataID IN (SELECT dataID FROM sensorData WHERE TIME(pullTime) > %s AND TIME(pullTime) < %s)"
	vals = (stringWindowStart, stringWindowEnd)
	mycursor.execute(sql, vals)
	result = mycursor.fetchall()

	lons = []
	lats = []
	for row in result:
		lons.append(row[3])
		lats.append(row[4])
	lons = np.array(lons)
	lats = np.array(lats)

	meanLon = np.mean(lons)
	meanLat = np.mean(lats)
	covarMat = np.cov(lons.astype(float), lats.astype(float))

	return [covarMat, meanLon, meanLat]

sql = "SELECT * FROM sensorData WHERE pullTime = (SELECT MAX(pullTime) FROM sensorData WHERE user = 'testUser')"
mycursor.execute(sql)
result = mycursor.fetchone()
mydb.commit()

windowStart = result[7] - timedelta(minutes=30)
windowEnd = result[7] + timedelta(minutes=30)
stringWindowStart = windowStart.strftime("%H:%M:%S:%f")
stringWindowEnd = windowEnd.strftime("%H:%M:%S:%f")

firstSelect = select_from_window(stringWindowStart, stringWindowEnd)
secondSelect = select_from_window('19:25:46:0000', '20:25:46:0000')

firstMeans = [[float(firstSelect[1])], [float(firstSelect[2])]]
ftestMeanLon = firstMeans[0][0]-.0000114
ftestMeanLat = firstMeans[1][0]-.0000167
ftestMeans = [[ftestMeanLon], [ftestMeanLat]]
firstConfidence = mvn_confidence(60, firstMeans, firstSelect[0], ftestMeans)

secondMeans = [[float(secondSelect[1])], [float(secondSelect[2])]]
stestMeanLon = secondMeans[0][0]-.0000114
stestMeanLat = secondMeans[1][0]-.0000167
stestMeans = [[stestMeanLon], [stestMeanLat]]
secondConfidence = mvn_confidence(60, secondMeans, secondSelect[0], stestMeans)

firstNonConfident = mvn_confidence(60, secondMeans, secondSelect[0], ftestMeans)
secondNonConfident = mvn_confidence(60, firstMeans, firstSelect[0], stestMeans)

#Create grid and multivariate normal
x = np.linspace(40.463,40.467,50)
y = np.linspace(-79.937,-79.933,50)
X, Y = np.meshgrid(x,y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X; pos[:, :, 1] = Y
rv1 = multivariate_normal([firstSelect[1], firstSelect[2]], firstSelect[0])
rv2 = multivariate_normal([secondSelect[1], secondSelect[2]], secondSelect[0])


stringOne = "First Point: Confidence in D1 = " + str(firstConfidence[1])
stringTwo = "Second Confidence in D2 = " + str(secondConfidence[1])
#Make a 3D plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, rv1.pdf(pos),cmap='viridis',linewidth=0)
ax.plot_surface(X, Y, rv2.pdf(pos),cmap='viridis',linewidth=0)
ax.text(ftestMeanLon, ftestMeanLat, 150000, stringOne, color='black')
ax.text(stestMeanLon, stestMeanLat, 685000, stringTwo, color='black')
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Distribution')
plt.show()