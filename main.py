import ifcopenshell

from .rules import windowRule
from .rules import doorRule

model = ifcopenshell.open("/Users/bruger/Downloads/CES_BLD_24_06_MEP.ifc")

windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)
