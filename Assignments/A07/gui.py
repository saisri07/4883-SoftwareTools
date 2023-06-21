import PySimpleGUI as sg
from datetime import datetime
import get_weather

def currentDate(returnType='tuple'):
    """ Get the current date and return it as a tuple, list, or dictionary.
    Args:
        returnType (str): The type of object to return. Valid values are 'tuple', 'list', or 'dict'.
    """
    now = datetime.now()
    if returnType == 'tuple':
        return now.month, now.day, now.year
    elif returnType == 'list':
        return [now.month, now.day, now.year]
    return {
        'day': now.day,
        'month': now.month,
        'year': now.year
    }

def buildWeatherURL(month=None, day=None, year=None, airport=None, filter=None):
    """ A gui to pass parameters to get the weather from the web.
    Args:
        month (int): The month to get the weather for.
        day (int): The day to get the weather for.
        year (int): The year to get the weather for.
    Returns:
        Should return a URL like this, but replace the month, day, and year, filter, and airport with the values passed in.
        https://www.wunderground.com/history/daily/KCHO/date/2020-12-31
    """
    current_month, current_day, current_year = currentDate('tuple')

    if not month:
        month = current_month
    if not day:
        day = current_day
    if not year:
        year = current_year

    # Create the GUI's layout using combo boxes for user input
    layout = [
        [sg.Text('Month'), sg.Combo(list(range(1, 13)), default_value=month, size=(10, 1))],
        [sg.Text('Day'), sg.Combo(list(range(1, 32)), default_value=day, size=(10, 1))],
        [sg.Text('Year'), sg.Combo(list(range(current_year, 2024)), default_value=year, size=(10, 1))],
        [sg.Text('Code'), sg.InputText()],
        [sg.Text('Daily / Weekly / Monthly'), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Get The Weather', layout)

    event, values = window.read()
    window.close()

    month = values[0]
    day = values[1]
    year = values[2]
    code = values[3]
    filter = values[4]

    sg.popup('You entered', f"Month: {month}, Day: {day}, Year: {year}, Code: {code}, Filter: {filter}")

    # Return the URL to pass to wunderground to get appropriate weather data
    return f"https://www.wunderground.com/history/{filter}/{code}/date/{year}-{month}-{day}"






if __name__ == '__main__':
    url=buildWeatherURL()
    get_weather.test(url)

