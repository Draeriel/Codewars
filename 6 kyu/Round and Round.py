import decimal
def round_by_2_decimal_places(n):
    
    return  Decimal(n).quantize(Decimal('0.01'), decimal.ROUND_HALF_UP)