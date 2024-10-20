# BIManalyst group 14
for i in range(20):
    i = "Around the world, around the world"
    print(i)

#First we import necessary data:    
import ifcopenshell
from bonsai.bim.ifc import IfcStore

#Then we load both the MEP and ARC-file:
mep_file = ifcopenshell.open("/Users/bruger/Downloads/CES_BLD_24_06_MEP.ifc")
arc_file = ifcopenshell.open("/Users/bruger/Downloads/CES_BLD_24_10_ARC.ifc")

#Now we can extract the components for ventilation, technical installations, etc. and other MEP systems:
def extract_components(file):
    ventilation = file.by_type("IfcDistributionElement")  
    heating = file.by_type("IfcFlowTerminal")  
    cooling = file.by_type("IfcEnergyConversionDevice") 
    pipes = file.by_type("IfcFlowSegment")  
    electrical = file.by_type("IfcCableSegment")  
    fire_systems = file.by_type("IfcFireSuppressionTerminal")  
    ahu_units = file.by_type("IfcBuildingElementProxy") 
    technical_installations = file.by_type("IfcFlowController")
    
    #Since we defined the components, we can return the components for ARC file too:
    return ventilation, heating, cooling, pipes, electrical, fire_systems, ahu_units, technical_installations

#Subsequently, we extract the components from the MEP-file
ventilation, heating, cooling, pipes, electrical, fire_systems, ahu_units, technical_installations = extract_components(mep_file)

#And we do so for the components for the ARC-file as well:
ventilation_arc, heating_arc, cooling_arc, pipes_arc, electrical_arc, fire_systems_arc, ahu_units_arc, technical_installations_arc = extract_components(arc_file) 

#Finally, we can print the amount for each component for MEP:
print(f"Ventilation elements: {len(ventilation)}")
print(f"Heating elements: {len(heating)}")
print(f"Cooling elements: {len(cooling)}")
print(f"Pipes: {len(pipes)}")
print(f"Electrical cables: {len(electrical)}")
print(f"Fire protection systems: {len(fire_systems)}")
print(f"Air Handling Units (AHUs): {len(ahu_units)}")
print(f"Technical installations: {len(technical_installations)}")

print("\n---------------")


#And also for the ARC-file:
print(f"Ventilation elements: {len(ventilation_arc)}")
print(f"Heating elements: {len(heating_arc)}")
print(f"Cooling elements: {len(cooling_arc)}")
print(f"Pipes: {len(pipes_arc)}")
print(f"Electrical cables: {len(electrical_arc)}")
print(f"Fire protection systems: {len(fire_systems_arc)}")
print(f"Air Handling Units (AHUs): {len(ahu_units_arc)}")
print(f"Technical installations: {len(technical_installations_arc)}")

#Now we can check and compare the Claims from the report:
print("\n-----Reported claims from the report-----")
print(f"Reported number of Air Handling Units (AHUs): 11")
print(f"Reported ventilation rate for toilets: 10 L/s")
print(f"Reported ventilation rate for kitchens: 20 L/s")
print(f"Reported number of pipes and cables passing through the cores: 36")

#We can also look at an example, where we make calculation of ventilation requirements for specific rooms
def ventilation_need(n, q_p, A_R, q_b):
    """
    We use the given formula in the report to calculate the ventilation need for the specific room:
    q_tot = n * q_p + A_R * q_b
    where:
    n: amount of people in the room
    q_p: ventilation rate per person (in L/s)
    A_R: room area (in m²)
    q_b: ventilation rate per unit area (in L/s per m²)
    """
    q_tot = n * q_p + A_R * q_b
    return q_tot

#We can now test examples with ventilation calculation for toilets and kitchens:
n_toilet = 3
A_R_toilet = 15  
q_p_toilet = 10  
q_b_toilet = 0.1 

n_kitchen = 5
A_R_kitchen = 30  
q_p_kitchen = 20  
q_b_kitchen = 0.2 

#Now we calculate the examples:
q_tot_toilet = ventilation_need(n_toilet, q_p_toilet, A_R_toilet, q_b_toilet)
q_tot_kitchen = ventilation_need(n_kitchen, q_p_kitchen,A_R_kitchen, q_b_kitchen)

print(f"\nCalculated ventilation need for toilet: {q_tot_toilet} L/s")
print(f"Calculated ventilation need for kitchen: {q_tot_kitchen} L/s")
