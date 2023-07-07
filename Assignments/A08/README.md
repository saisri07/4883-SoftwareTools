# Assignment-8

## Sai Teja Sripathi

## Description:

FastAPI was used to establish a RESTful API for this project that gives users access to COVID-19 data. The API enables APIs to retrieve various statistics pertaining to COVID-19 cases and retrieves data from a publicly accessible data source.

## File Contents:
|   #   | File                  | Description                                        |
| :---: | :-------------------- | -------------------------------------------------- |
|   1   | [api.py](api.py)      | Python code for api request.      |
|   2   | [data.csv](data.csv)  | Dataset which has all covid data        |
|   3   | [requirements.txt](requirements.txt)  | contains required module that needs to installed       |

## Endpoints:

<img width="1415" alt="Screenshot 2023-07-07 at 11 28 40 AM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/5d870c95-9e65-43d3-b365-30a3a3ad01df">


## /Countries

* Retrieves a list of unique countries with COVID-19 data.

<img width="1216" alt="Screenshot 2023-07-07 at 3 42 52 PM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/de85d496-482b-4214-928c-901751a85f92">


## /Regions

* Retrieves a list of unique WHO regions with COVID-19 data.

  <img width="1216" alt="Screenshot 2023-07-07 at 3 42 52 PM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/6498e75b-831c-4ca5-b324-02bf12c117cf">


## /Deaths

* Retrieves total deaths for all countries.

<img width="1410" alt="Screenshot 2023-07-07 at 3 45 09 PM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/17878b4d-ef5d-4d65-99ca-7f8cb5a5354d">


## /deaths?country=Brazil

* Retrieves the total deaths for the given country.

<img width="1192" alt="Screenshot 2023-07-07 at 1 23 14 PM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/6039adb5-7f58-419c-9a71-5a9d75509334">

## /deaths?region=AFRO

* Retrieves the total deaths for the given region.

<img width="1189" alt="Screenshot 2023-07-07 at 1 24 11 PM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/ab386a6c-97e5-4592-93a3-a2f1d55f3ef9">

## /deaths?country=France&year=2020

* Retrieves the total deaths for the given country in a specified year.

<img width="1190" alt="Screenshot 2023-07-07 at 1 25 01 PM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/5503c4f3-8a98-45b6-9083-7c292ba397b1">

## /deaths?region=AFRO&year=2020

* Retrieves the total deaths for the given region in a specified year.

<img width="1193" alt="Screenshot 2023-07-07 at 1 25 39 PM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/ec77e9b8-edb0-4458-adb5-092719bf2619">


## /max_deaths

* Retrieves the country that has maximum number of deaths.

<img width="1228" alt="Screenshot 2023-07-07 at 3 49 18 PM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/073c6e6d-d517-41a8-b33f-ff78f2ec6f70">

## /max_deaths?min_date=2021-06-01&max_date=2021-12-31

* Find the country with the most deaths between a range of dates

<img width="1393" alt="Screenshot 2023-07-07 at 4 08 53 PM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/81c068f4-5c0b-45e9-abc5-a345638ba29c">

## /min_deaths

* Retrieves the country that has maximum number of deaths.


<img width="1213" alt="Screenshot 2023-07-07 at 3 50 43 PM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/b98b5fab-dea5-4942-b04e-a551a9ef6cca">



## /min_deaths?min_date=2021-06-01&max_date=2021-12-31

* Retrieves the maximum number in given range of dates.

<img width="1200" alt="Screenshot 2023-07-07 at 3 37 15 PM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/462ca0ff-61e2-4aa4-8521-018745952cc7">

## /Avg_deaths

* Retrieves the country that has maximum number of deaths.


<img width="1228" alt="Screenshot 2023-07-07 at 3 46 39 PM" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/cc7ae899-e12f-4d60-82ff-84ab244210a6">


## Instructions:
* you can access the API at http://localhost:8000.


## Challenges Faced:









