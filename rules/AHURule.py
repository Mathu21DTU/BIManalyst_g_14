import ifcopenshell

def checkRule(model):
    AHU = model.by_type('fcBuildingElementProx')

    result = f"There are: {len(AHU)} air handling units."

    return result