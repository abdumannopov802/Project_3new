from championship import Championship
championship1 = Championship()

championship1.defineGrandPrix("GP1")
championship1.createDriver("Driver-1")
championship1.createDriver("Driver-2")

print(championship1.getGrandPrix("GP1"))
print(championship1.getDriver("Driver-1"))
print(championship1.getDriver("Driver-2"))

championship1.set_time("GP1", "Driver-2", (1, 22, 55, 30))
championship1.set_time("GP1", "Driver-2", (2, 13, 45, 28))

print(championship1.get_GP_Ranking())
