
import ifcopenshell
from bonsai.bim.ifc import IfcStore

# Vi importerer filen via ifcopenshell
file = ifcopenshell.open("/Users/bruger/Downloads/CES_BLD_24_06_MEP.ifc")

# Vi definerer AHU:
things = file.by_type("IfcBuildingElementProxy")

# Vi tjekker hvor mange AHU der er via:
print(len(things))
