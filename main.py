import ifcopenshell

from rules import AHURule
# Vi importerer filen via ifcopenshell
model = ifcopenshell.open("/Users/bruger/Downloads/CES_BLD_24_06_MEP.ifc")

# Vi definerer AHU:
AHUResult = AHURule.checkRule(model)

# Vi tjekker hvor mange AHU der er via:
print("AHU result:",AHUResult)


