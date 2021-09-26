# pylint: disable=missing-docstring

RATES = {"USDEUR": 0.85, "GBPEUR": 1.13, "CHFEUR": 0.86, "EURGBP": 0.885}

# `amount` is a `tuple` like (100, EUR). `currency` is a `string`
def convert(amount, currency):
    """Rate conversion function"""
    conversion = amount[1] + currency
    if conversion in RATES:
        factor = RATES[conversion]
        converted = amount[0] * factor
        return round(converted)
    return None
        