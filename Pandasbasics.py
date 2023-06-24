#simple Function
def m2toft2(area_meter2):
    """
    This function takes in as input the area in meters squared
    and returns as an output the area in square feet

    input: area_meter2, the area in square meters
    output: area_feet2, the area in square feet
    """
    area_feet2 = 10.76391 * area_meter2
    return area_feet2


#Iteration in definition

def convert_area(area_meters2):
    """
    This function takes in a list of area in square meters and
    returns area in square feet

    input: area_meters2, area in square meters
    output: area_feet, area in square feet
    """
    area_feet2 = [item * 10.76391 for item in area_meters2]
    return area_feet2
