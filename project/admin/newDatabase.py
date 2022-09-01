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
        cursor.execute("SELECT * from admin WHERE username=%s and password = %s",data)
        return cursor.fetchone()
    except:
        return False
    

def cityAdd(data):
    try:
        cursor.execute("INSERT INTO city (name, state) VALUES (%s, %s)", data)
        con.commit()
        return True
    except:
        return False

def manageCity():
    try:
        cursor.execute('SELECT * FROM city')
        return cursor.fetchall()
    except:
        return False

def deleteCity(id):
    try:
        cursor.execute('DELETE FROM city WHERE id = %s', id)
        con.commit()
        return True
    except:
        return False

def getSingleCity(id):
    try:
        cursor.execute('SELECT * FROM city WHERE id =%s', id)
        return cursor.fetchone()
    except:
        return False

def editCity(data):
    try:
        cursor.execute('UPDATE city SET name = %s, state = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False


def allCityForArea():
    try:
        cursor.execute('SELECT id, name FROM city')
        return cursor.fetchall()
    except:
        return False

def addArea(data):
    try:
        cursor.execute('INSERT INTO areas (cityId, name) VALUES (%s, %s)', data)
        con.commit()
        return True
    except:
        return False

def allAreas():
    try:
        cursor.execute('SELECT areas.id, city.name, areas.name FROM areas left join city on city.id = areas.cityId')
        return cursor.fetchall()
    except:
        return False

def deleteAreas(data):
    try:
        cursor.execute('DELETE FROM areas WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False

def singleArea(data):
    try:
        cursor.execute('SELECT city.id, city.name, areas.name FROM areas left join city on city.id = areas.cityId WHERE areas.id = %s', data)
        return cursor.fetchone()
    except:
        return False

def editArea(data):
    
    try:
        cursor.execute('UPDATE areas SET cityId = %s, name = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False


def addVolunteer(data):

    try:
        cursor.execute('INSERT INTO volunteer (name, age, contact, address, username, password) VALUES (%s, %s, %s, %s, %s, %s)', data)
        con.commit()
        return True
    except:
        return False


def allVolunteer():
    try:
        cursor.execute('SELECT * FROM volunteer')
        return cursor.fetchall()
    except:
        return False

def deleteVolunteer(id):
    try:
        cursor.execute('DELETE FROM volunteer WHERE id = %s', id)
        con.commit()
        return True
    except:
        return False

def singleVolunteer(id):
    try:
        cursor.execute('SELECT * FROM volunteer WHERE id =%s', id)
        return cursor.fetchone()
    except:
        return False

def editVolunteers(data):
    try:
        cursor.execute('UPDATE volunteer SET name = %s, age = %s, contact = %s, address = %s, username = %s, password = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False


def assignCity():
    try:
        cursor.execute('SELECT id, name FROM city')
        return cursor.fetchall()
    except:
        return False

def getAreass(id):
    print(id)
    # cursor.execute('SELECT id, name FROM areas WHERE id = %s', (id,))
    try:
        cursor.execute('SELECT id, name FROM areas WHERE cityId = %s', (id,))
        return cursor.fetchall()
    except:
        return False

def getVolunteers():
    try:
        cursor.execute('SELECT id, name FROM volunteer')
        return cursor.fetchall()
    except:
        return False


def assignVolunteer(data):
    try:
        cursor.execute('INSERT INTO assignarea (volunteerId, areaId, expectedHouses, cityId) VALUES (%s, %s, %s, %s)', data)
        con.commit()
        return True
    except:
        return False

def allAssignArea():
    try:
        cursor.execute('SELECT assignarea.id, volunteer.name, areas.name, assignarea.expectedHouses, city.name FROM assignarea LEFT JOIN volunteer ON volunteer.id = assignarea.volunteerId LEFT JOIN areas ON areas.id = assignarea.areaId LEFT JOIN city ON city.id = assignarea.cityId')
        return cursor.fetchall()
    except:
        return False

def deleteAssignArea(id):
    try:
        cursor.execute('DELETE FROM assignarea WHERE id = %s', id)
        con.commit()
        return True
    except:
        return False

def getExpectedHouses(areaId):
    try:
        cursor.execute('SELECT expectedHouses FROM assignarea WHERE areaId = %s', (areaId,))
        return cursor.fetchall()
    except:
        return False

def getCoveredHouses(areaId):
    try:
        cursor.execute('SELECT * FROM houses WHERE areaId = %s', (areaId, ))
        return cursor.fetchall()
    except:
        return False