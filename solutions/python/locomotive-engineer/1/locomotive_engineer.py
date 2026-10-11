"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    *wagons_list, = args
    return wagons_list


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    a, b, c, *rest = each_wagons_id
    *fixed_list, = c, *missing_wagons, *rest, a, b
    return fixed_list


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    *missing_stops, = kwargs.values()
    route['stops'] = missing_stops
    return route




def extend_route_information(route:dict, more_route_information:dict):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    extended_route_information = {**route, **more_route_information}
    return extended_route_information


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    row1, row2, row3 = wagons_rows
    row1[1], row2[0] = row2[0], row1[1]
    row1[2], row3[0] = row3[0], row1[2]
    row2[2], row3[1] = row3[1], row2[2]
    *correct_wagons_grid, = row1, row2, row3
    return correct_wagons_grid 

