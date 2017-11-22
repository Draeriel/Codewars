def zeroFuel(distance_to_pump, mpg, fuel_left):
    total = mpg*fuel_left
    if total >= distance_to_pump:
        return True
    else:
        return False