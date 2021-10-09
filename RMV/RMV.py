# python RMV.py 200 12 60 1.9

from sys import argv
from datetime import date
import calculate
import DbConnect

#########################################################
DbConnect.createOrDrop("insert") # <------- WARNING!!  ##
# "insert" to create table or check if created         ##
# "drop" to drop table                                 ##
# "" continue saving records in current database table ##
#########################################################

usedLiters = calculate.calculateUsedLiters(argv[1], argv[2])
print('Used liters: ', usedLiters)

litersPerMinute = calculate.calcLitersPerMinute(usedLiters, argv[3])

Rmv = calculate.calculateRMV(litersPerMinute, argv[4])
print('Your RMV: ', Rmv, ' liters per minute')

DbConnect.insertTo(Rmv)
DbConnect.showDatabase()
DbConnect.closeDb()

with open('results.txt', 'a') as save_result:
    save_result.write('In ' + str(date.today()) + ' was ' + str(Rmv) + ' liters per minute\n')