noOfDays = int(input("How many day's temperature? :"))
weatherList = list()
i = 1
while i <= noOfDays:
    temp = int(input(f"Please Enter Day {i}'s Temperature ? :"))
    weatherList.append(temp)
    i+=1

averageTemperature = sum(weatherList)/noOfDays

counter = 0
for _var in weatherList:
    if _var >= averageTemperature:
        counter += 1

print(f"Average Temperature = : {averageTemperature}")
print(f"{counter} day(s) above average")