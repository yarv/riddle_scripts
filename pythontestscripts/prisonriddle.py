import math
import random



def prisonerriddle():
    
    random.seed()

    prisoners = {i:"noflick" for i in range(100)}
    prisonersin={i:0 for i in range(100)}

    """(before game begins)"""

    lightswitch = "off"
    specialcount = 0
    day = 1

    """On first day:"""

    wardenchoice = random.randint(0,99)
    prisoners[wardenchoice] = "special"
    prisonersin[wardenchoice] = 1
    specialcount += 1
    day += 1

    dayfinished = 0
    """On every subsequent day"""
    
    while specialcount < 100:
        if sum(prisonersin.values()) == 100.0:
            dayfinished = day
            for i in range(100):
                prisonersin[i] = 2

        day +=1

        wardenchoice = random.randint(0,99)
        
        if prisonersin[wardenchoice] == 0:
            prisonersin[wardenchoice] = 1

        if prisoners[wardenchoice] == "special":
            if lightswitch == "on":
                specialcount += 1
                lightswitch = "off"

        elif prisoners[wardenchoice] == "noflick":
            if lightswitch == "off":
                lightswitch = "on"
                prisoners[wardenchoice] = "flicked"
        
    return (day, dayfinished)

if __name__ == "__main__":
    print prisonersriddle()
