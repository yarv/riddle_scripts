import prisonriddle

daytotal = 0
realdaytotal = 0

data_file = open("riddledata.txt",'w')

for i in range(1000):
    run = prisonriddle.prisonerriddle()
    daytotal += run[0]
    realdaytotal += run[1]
    
    data_file.write(str(run[0])+" "+str(run[1])+"\n")
    print("run " + str(i) + " completed.")
data_file.close()

dayaverage = daytotal/1000.0
yearaverage = dayaverage/365.25

realyearaverage = realdaytotal/(1000.0*365.25)

print("after 1000 experiments, we have averages of " +
      str(yearaverage) + " and " + str(realyearaverage) + " years")
