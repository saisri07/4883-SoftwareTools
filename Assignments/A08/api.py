
from collections import defaultdict
import datetime
import sys

from fastapi import FastAPI, Response, status
from fastapi.responses import RedirectResponse
import uvicorn
import csv



description = """🚀
## Covid Stats API
### Get all covid related statistics
An api to show covid related data for each country and by each WHO region.
"""


app = FastAPI(

    description=description,

)

db = []

# Open the CSV file
# populates the `db` list with all the csv data
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    i = 0
    # Read each row in the CSV file
    for row in reader:
        if i == 0:
            i += 1
            continue
        db.append(row)


def getUniqueCountries():
    
    countries = set()

    for row in db:
        countries.add(row[2])

    return countries

def getUniqueWhos():
    
    whos = set()

    for row in db:
        whos.add(row[3])
   
    return whos

@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")

@app.get("/countries")
async def countries():

    """
    this method will return a list of all the countries for which data is available
    - ** Params: **
        None
    - ** Returns: **
        - (set) - set containing all the unique country names

    #### Example:
        [http://127.0.0.1:8000/api/v1/countries]

    #### Response:
        {
            "status": "success",
            "countries": [
                "Côte d’Ivoire",
                "Romania",
                "Türkiye",
                .
                .
                .
                "New Zealand"
            ]
        }

    """

    # returns
    return {"status": "success", "countries": getUniqueCountries()}


@app.get("/regions")
async def whos():

    """
    this method will return a list of all the WHO regions for which data is available
    - ** Params: **
        None
    - ** Returns: **
        - (set) - set containing all the unique WHO region names

    #### Example:
        [http://127.0.0.1:8000/api/v1/regions]
    
    #### Response:
        {
            "status": "success",
            "whos": [
                "EURO",
                "AFRO",
                "AMRO",
                "WPRO",
                "Other",
                "SEARO",
                "EMRO"
            ]
        }
    
    """

    # returns
    return {"status": "success", "whos": getUniqueWhos()}

@app.get("/deaths")
async def deathStats(response: Response, country: str = None, region: str = None, year: int = None):

    """
    This method will return the death count.
    The death count can be filtered by country and/or year
    and also by who region and/or year
    - ** Params: **
        - country (str): country name
        - region (str): who region name
        - year (int): 4 digit year
    - ** Returns: **
        - (int): the total or specific death count based on filters

    #### Example 1:
        [http://127.0.0.1:8000/api/v1/deaths]
    
    #### Response 1:
        {
            "status": "success",
            "deaths": {
                "All countries": 5158501455
            },
            "params": {
                "country": null,
                "region": null,
                "year": null
            }
        }
    
    #### Example 2:
        [http://127.0.0.1:8000/api/v1/deaths?country=India&year=2020]
    
    #### Response 2:
        {
            "status": "success",
            "deaths": {
                "India": 17022321
            },
            "params": {
                "country": "India",
                "region": null,
                "year": 2020
            }
        }
    
    #### Example 3:
        [http://127.0.0.1:8000/api/v1/deaths?region=EMROO&year=2020]
    
    #### Response 3:
        {
            "status": "error",
            "message": "given region is invalid"
        }

    """

    # creating a dict to store deaths by country
    deaths = defaultdict(int)

    # getting all the unique countries and who regions
    countries = getUniqueCountries()
    whos = getUniqueWhos()

    # checking if the given country is valid
    if country != None and country not in countries:

        # changing status code to 400 to show invalid country
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": "error", "message": "given country is invalid"}
    
    # checking if the given region is valid
    if region != None and region not in whos:

        # changing status code to 400 to show invalid region
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": "error", "message": "given region is invalid"}
    
    # if year parameter is null
    if year == None:

        # if no arguments given count all deaths
        if country == None and region == None:
            for row in db:
                deaths["All countries"] += int(row[7])
        
        # if country argument is given get deaths for that country
        elif region == None:
            for row in db:
                if row[2] == country:
                    deaths[country] += int(row[7])
        
        # if region argument is given get deaths for that region
        elif country == None:
            for row in db:
                if row[3] == region:
                    deaths[region] += int(row[7])

    # 2020 because covid started at the end of 2019
    # and guessing there wouldn't be any useful data for that short period
    # if given year is greater than current year
    # the below condition are not completely right!
    elif year < 2020 or year > datetime.datetime.now().year:

        # invalid year given so setting status code to 400
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": "error", "message": "enter a valid year"}
    
    # when valid year is given
    else:

        # if no arguments for country, region given
        if region == None and country == None:

            # change status code
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"status": "error", "message": "enter either country or region when using year query"}

        # if country argumemt is given
        elif region == None:

            for row in db:
                if row[2] == country and int(row[0][:4]) == year:
                    deaths[country] += int(row[7])
        
        # if region argumnet is given
        elif country == None:

            for row in db:
                if row[3] == region and int(row[0][:4]) == year:
                    deaths[region] += int(row[7])
        
        # when both country and region are given
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"status": "error", "message": "enter either country or region when using year query"}
    
    # response
    return {"status": "success", "deaths": deaths, "params": 
            {"country": country,
             "region": region,
             "year": year}}



@app.get("/cases")
async def caseStats(response: Response, country: str = None, region: str = None, year: int = None):
    """
    This method will return the case count.
    The case count can be filtered by country and/or year
    and also by who region and/or year
    - ** Params: **
        - country (str): country name
        - region (str): who region name
        - year (int): 4 digit year
    - ** Returns: **
        - (int): the total or specific case count based on filters

    #### Example 1:
        [http://127.0.0.1:8000/api/v1/cases]
    
    #### Response 1:
        {
            "status": "success",
            "cases": {
                "All countries": 401318665923
            },
            "params": {
                "country": null,
                "region": null,
                "year": null
            }
        }
    
    #### Example 2:
        [http://127.0.0.1:8000/api/v1/cases?country=India&year=2020]
    
    #### Response 2:
        {
            "status": "success",
            "cases": {
                "India": 1074019421
            },
            "params": {
                "country": "India",
                "region": null,
                "year": 2020
            }
        }
    
    #### Example 3:
        [http://127.0.0.1:8000/api/v1/cases?region=EMROO&year=2020]
    
    #### Response 3:
        {
            "status": "error",
            "message": "given region is invalid"
        }

    """

    # create a dictionary as a container for our results
    # that will hold unique regions. Why, because there 
    # cannot be duplicate keys in a dictionary.
    cases = defaultdict(int)

    # getting all unique countries and regions
    countries = getUniqueCountries()
    whos = getUniqueWhos()

    # if country given is invalid or region given is invalid
    # set status code to 400
    if country != None and country not in countries:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": "error", "message": "given country is invalid"}
    if region != None and region not in whos:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": "error", "message": "given region is invalid"}
    
    # if year parameter is null
    if year == None:

        # if no arguments given count all deaths
        if country == None and region == None:
            for row in db:
                cases["All countries"] += int(row[5])
        
        # if country argument is given get deaths for that country
        elif region == None:
            for row in db:
                if row[2] == country:
                    cases[country] += int(row[5])
        
        # if region argument is given get deaths for that region
        elif country == None:
            for row in db:
                if row[3] == region:
                    cases[region] += int(row[5])

    # 2020 because covid started at the end of 2019
    # and guessing there wouldn't be any useful data for that short period
    # if given year is greater than current year
    # the below condition are not completely right!
    elif year < 2020 or year > datetime.datetime.now().year:

        # invalid year given so setting status code to 400
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": "error", "message": "enter a valid year"}
    
    # when valid year is given
    else:

        # if no arguments for country, region given
        if region == None and country == None:

            # change status code
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"status": "error", "message": "enter either country or region when using year query"}

        # if country argumemt is given
        elif region == None:

            for row in db:
                if row[2] == country and int(row[0][:4]) == year:
                    cases[country] += int(row[5])
        
        # if region argumnet is given
        elif country == None:

            for row in db:
                if row[3] == region and int(row[0][:4]) == year:
                    cases[region] += int(row[5])
        
        # when both country and region are given
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"status": "error", "message": "enter either country or region when using year query"}
    
    # response
    return {"status": "success", "cases": cases, "params": 
            {"country": country,
             "region": region,
             "year": year}}

@app.get("/max_deaths")
async def maxDeaths(response: Response, min_date: str = None, max_date: str = None):

    """
    This method will return the country with maximum deaths out of all countries
    we can filter by dates as lower and upper bounds
    - ** Params: **
        - min_date (str): the minimum date for filtering
        - max_date (str): the maximum date for filtering
    - ** Returns: **
        - (int) - max deaths in a country out of all countries filtered by given range

    #### Example 1:
        [http://127.0.0.1:8000/api/v1/max-deaths]
    
    #### Response 1:

        {
            "status": "success",
            "United States of America": 827394185,
            "params": [
                null
            ]
        }
    
    #### Example 2:
        [http://127.0.0.1:5000/api/v1/max-deaths?min_date=2021-01-01&max_date=2021-12-31]
    
    #### Response 2:
        {
            "status": "success",
            "United States of America": 223942585,
            "params": [
                "2021-01-01",
                "2021-12-31"
            ]
        }
    
    #### Example 3:
        [http://127.0.0.1:8000/api/v1/max-deaths?min_date=2021-01-01&max_date=2020-12-31]
    
    #### Response 3:
        {
            "status": "error",
            "message": "min_date must be smaller than max_date"
        }
        
    """

    # dict to store the deaths by country
    deaths = defaultdict(int)

    # to store the country name
    maxDeathsCountry = ''

    # to store the max deaths
    maxDeaths = -sys.maxsize

    # if no arguments are given
    if min_date == None and max_date == None:

        # get death count for all countries
        for row in db:
            deaths[row[2]] += int(row[7])

    # if only one of the required arguments given
    elif min_date == None or max_date == None:

        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": "error", "message": "enter either both or none dates"}
    
    # when both arguments are given
    else:

        # converting the given dates to datetimeobjects
        start_date = list(map(int, min_date.split('-')))
        end_date = list(map(int, max_date.split('-')))
        start_date = datetime.datetime(start_date[0], start_date[1], start_date[2])
        end_date = datetime.datetime(end_date[0], end_date[1], end_date[2])

        # if given dates are invalid
        if(end_date < start_date):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"status": "error", "message": "min_date must be smaller than max_date"}

        # loop through the db to get all valid covid case stats based on filter
        for row in db:

            # getting present row date and converting it to datetime object
            current_date = list(map(int, row[0].split('-')))
            current_date = datetime.datetime(current_date[0], current_date[1], current_date[2])

            # filter condition
            if(current_date >= start_date and current_date <= end_date):
                deaths[row[2]] += int(row[7])
    
    # loop through all valid entries for each country to get the country with max deaths
    for country in deaths:
        if maxDeaths < deaths[country]:
            maxDeaths = deaths[country]
            maxDeathsCountry = country

    # response
    return {"status": "success", maxDeathsCountry: maxDeaths, "params": {min_date, max_date}}

@app.get("/min_deaths")
async def minDeaths(response: Response, min_date: str = None, max_date: str = None):

    """
    This method will return the country with minimum deaths out of all countries
    we can filter by dates as lower and upper bounds
    - ** Params: **
        - min_date (str): the minimum date for filtering
        - max_date (str): the maximum date for filtering
    - ** Returns: **
        - (int) - min deaths in a country out of all countries filtered by given range

    #### Example 1:
        [http://127.0.0.1:8000/api/v1/min-deaths]
    
    #### Response 1:
        {
            "status": "success",
            "Democratic People's Republic of Korea": 0,
            "params": [
                null
            ]
        }

    #### Example 2:
        [http://127.0.0.1:8000/api/v1/min-deaths?min_date=2021-01-01&max_date=2021-12-31]

    #### Response 2:
        {
            "status": "success",
            "American Samoa": 0,
            "params": [
                "2021-01-01",
                "2021-12-31"
            ]
        }
    
    #### Example 3:
        [http://127.0.0.1:8000/api/v1/min-deaths?min_date=2021-01-01&max_date=2020-12-31]
    
    #### Response 3:
        {
            "status": "error",
            "message": "min_date must be smaller than max_date"
        }
        
    """

    # dict to store the deaths by country
    deaths = defaultdict(int)

    # to store the country name
    minDeathsCountry = ''

    # to store the min deaths
    minDeaths = sys.maxsize

    # if no arguments are given
    if min_date == None and max_date == None:

        # get death count for all countries
        for row in db:
            deaths[row[2]] += int(row[7])

    # if only one of the required arguments given
    elif min_date == None or max_date == None:

        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": "error", "message": "enter either both or none dates"}
    
    # when both arguments are given
    else:

        # converting the given dates to datetimeobjects
        start_date = list(map(int, min_date.split('-')))
        end_date = list(map(int, max_date.split('-')))
        start_date = datetime.datetime(start_date[0], start_date[1], start_date[2])
        end_date = datetime.datetime(end_date[0], end_date[1], end_date[2])

        # if given dates are invalid
        if(end_date < start_date):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"status": "error", "message": "min_date must be smaller than max_date"}

        # loop through the db to get all valid covid case stats based on filter
        for row in db:

            # getting present row date and converting it to datetime object
            current_date = list(map(int, row[0].split('-')))
            current_date = datetime.datetime(current_date[0], current_date[1], current_date[2])

            # filter condition
            if(current_date >= start_date and current_date <= end_date):
                deaths[row[2]] += int(row[7])
    
    # loop through all valid entries for each country to get the country with min deaths
    for country in deaths:
        if minDeaths > deaths[country]:
            minDeaths = deaths[country]
            minDeathsCountry = country

    # response
    return {"status": "success", minDeathsCountry: minDeaths, "params": {min_date, max_date}}

@app.get("/avg_deaths")
async def avgDeaths():

    """
    this method will return the average deaths combined in all countries
    - ** Params: **
        None
    - ** Returns: **
        - (float): the average deaths across all countries
    
    #### Example
        [http://127.0.0.1:8000/api/v1/avg-deaths]
    
    #### Response
        {
            "status": "success",
            "average deaths": 21765828.924050633
        }

    """

    # to store the death count for each country
    deaths = defaultdict(int)

    # storing the deaths for country
    for row in db:
        deaths[row[2]] += int(row[7])

    # getting total deaths for all countries combined
    deathCount = sum(deaths.values())

    # the average death
    avgDeath = deathCount / len(deaths)

    # response
    return {"status": "success", "average deaths": avgDeath}

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, log_level="debug", reload=True) #host="127.0.0.1"