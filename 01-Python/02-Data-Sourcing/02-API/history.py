# pylint: disable=missing-docstring

import sys
import datetime

from weather import search_city

def daily_forecast(woeid, year, month, day):
    pass

def monthly_forecast(woeid, year, month):
    pass # TODO: return a `list` of forecast for the whole month

def write_csv(woeid, year, month, city, forecasts):
    pass # TODO: dump all the forecasts to a CSV file in the `data` folder

def main():
    if len(sys.argv) > 2:
        city = search_city(sys.argv[1])
        if city:
            woeid = city['woeid']
            year = int(sys.argv[2])
            month = int(sys.argv[3])
            forecasts = monthly_forecast(woeid, year, month)
            write_csv(woeid, year, month, city['title'], forecasts)
    else:
        print("Usage: python history.py CITY YEAR MONTH")
        sys.exit(1)

if __name__ == '__main__':
    main()
