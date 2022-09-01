from traceback import print_tb
import mysql.connector
from mysql.connector import IntegrityError

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="poliomanagement"
)
cursor = con.cursor()

def login(data):
    try:
        cursor.execute('SELECT id FROM volunteer WHERE username = %s and password = %s', data)
        return cursor.fetchall()
    except:
        return False

def viewAssignedArea(id):
    print(id)
    try:
        cursor.execute('SELECT areas.id, city.name, areas.name, assignarea.expectedHouses FROM assignarea LEFT JOIN city ON city.id = assignarea.cityId LEFT JOIN areas ON areas.id = assignarea.areaId WHERE assignarea.volunteerId = %s', id)
        return cursor.fetchall()
    except:
        return False

def getArea(id):
    try:
        cursor.execute('SELECT name FROM areas WHERE id = %s', id)
        return cursor.fetchone()
    except:
        return False

def addHouses(data):
    try:
        cursor.execute('INSERT INTO houses (areaId, address, numChildren, dosesGiven, coveredBy) VALUES (%s,%s,%s,%s,%s)', data)
        con.commit()
        return True
    except:
        return False

def viewHouses(volId, areaId):
    print((volId, areaId))
    try:
        cursor.execute('SELECT houses.id, houses.address, houses.numChildren, houses.dosesGiven, volunteer.name FROM houses LEFT JOIN volunteer ON houses.coveredBy = volunteer.id WHERE houses.areaId = %s', (areaId[0],))
        return cursor.fetchall()
    except:
        return False