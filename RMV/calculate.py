
def calculateUsedLiters(usedBars, cylinderVolume):
    multiplication = int(usedBars) * int(cylinderVolume)
    return multiplication

def calcLitersPerMinute(usedLiters, divingTime):
    dividing = int(usedLiters) / int(divingTime)
    return dividing

def calculateRMV(litersPerMinute, mediumPressure):
    dividing = int(litersPerMinute) / float(mediumPressure)
    return round(dividing, 2)

