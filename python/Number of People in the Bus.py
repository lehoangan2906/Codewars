def number (bus_stops):
    result = 0

    for stop in bus_Stops:
        result += stop[0]
        result -= stop[1]

    if result < 0:
        return 0
    else:
        return result
