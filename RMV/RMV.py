# python RMV.py 200 12 60 1.9

from sys import argv
from datetime import date
import sqlite3

conn = sqlite3.connect('rmv.db')
c = conn.cursor()

# c.execute('''CREATE TABLE rmvResults(data TEXT, rmv REAL)''')

def calculateUsedLiters(usedBars, cylinderVolume):
    multiplication = int(usedBars) * int(cylinderVolume)
    return multiplication

def calcLitersPerMinute(usedLiters, divingTime):
    dividing = int(usedLiters) / int(divingTime)
    return dividing

def calculateRMV(litersPerMinute, mediumPressure):
    dividing = int(litersPerMinute) / float(mediumPressure)
    return dividing

def saveResult():
    c.execute("""INSERT INTO rmvResults VALUES('date.today()', 'Rmv')""")
    conn.commit()

def showProgress():
    for row in c.execute('SELECT * FROM rmvResults'):
        print (row)

usedLiters = calculateUsedLiters(argv[1], argv[2])
print('Used liters: ', usedLiters)

litersPerMinute = calcLitersPerMinute(usedLiters, argv[3])
print('Used liters per minute: ', litersPerMinute)

Rmv = round(calculateRMV(litersPerMinute, argv[4]), 2)
print('Your RMV: ', Rmv)

saveResult()
showProgress()
conn.close()

#with open('results.txt', 'a') as save_result:
    #save_result.write('In ' + str(date.today()) + ' was ' + str(Rmv) + ' liters per minute\n')