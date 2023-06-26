import IntelligentSuggestor
import WeatherForecasting
import argparse
import Service
import sys


# Database Detials
db_congig = {'DRIVER_NAME': 'SQL Server','SERVER_NAME': 'mtejasvi-z01\SQLEXPRESS','DATABASE_NAME': 'master'}


def getWeatherDetailsWithSuggestions(args):
    forecaster = WeatherForecasting.WeatherForecasting(args.city)
    weatherData = forecaster.getWeatherData()
    suggestions = IntelligentSuggestor.GetSuggestions(weatherData[1]['main'], args.city)
    strWeatherData = f"The weather in {args.city} shows {weatherData[1]['description']}\nHere are the weather details below - \n\n"\
                     f"Current Temprature = {weatherData[0]['temp']}{chr(176)}C\n"\
                     f"Max Temperature = {weatherData[0]['temp_max']}{chr(176)}C\n"\
                     f"Min Temperature = {weatherData[0]['temp_min']}{chr(176)}C\n"\
                     f"Humidity = {weatherData[0]['humidity']}%\n"\
                     f"Wind Speed = {weatherData[2]} meter/sec\n\n"\
                     f"Let me suggest you some places to visit, eateries to dine-out & recipes to cook in this weather.\n\n"\
                     f"Places to visit are listed below -\n\n"\
                     f"{suggestions[1]}\n\n"\
                     f"Places to dine-out are listed below -\n\n"\
                     f"{suggestions[2]}\n\n"\
                     f"Recepies to cook are listed below -\n\n"\
                     f"{suggestions[3]}\n\n"\
                     #f"Governoment Alerts - {weatherData[1]}\n"
    return strWeatherData, suggestions, weatherData[1]['main'], weatherData[1]['description']


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', type=str, default='Pune', help='Enter the name of the city')
    arguments = parser.parse_args()
    output = getWeatherDetailsWithSuggestions(arguments)
    sys.stdout.write(output[0])

    addToBucketList = input("Do you like to add the above to your bucket list? (Y/N) : ")

    if addToBucketList.lower() == 'y':
        # Add to bucket list
        service = Service.Service(db_congig['DRIVER_NAME'], db_congig['SERVER_NAME'], db_congig['DATABASE_NAME'])
        conn = service.get_connection()

        taskLists = service.get_data(f"select * from TaskLists order by taskId desc", conn)
        taskId = int(taskLists[0][0]) + 1 if len(taskLists) > 0 else 1
        service.insert_data(f"insert into TaskLists values({taskId}, 'Places to visit in {arguments.city}', 'Places to visit in {arguments.city} in {output[3]} weather')", conn)
        for place in output[1][0]['PlacesToVisit']:
            taskItems = service.get_data(f"select * from TaskItems order by itemId desc", conn)
            itemId = int(taskItems[0][0]) + 1 if len(taskItems) > 0 else 1
            service.insert_data(f"insert into TaskItems values({itemId}, '{place}', {taskId})", conn)

        taskLists = service.get_data(f"select * from TaskLists order by taskId desc", conn)
        taskId = int(taskLists[0][0]) + 1 if len(taskLists) > 0 else 1
        service.insert_data(f"insert into TaskLists values({taskId}, 'Places to dine-out in {arguments.city}', 'Places to dine-out in {arguments.city} in {output[3]} weather')", conn)    
        for restaurants in output[1][0]['Eateries']:
            taskItems = service.get_data(f"select * from TaskItems order by itemId desc", conn)
            itemId = int(taskItems[0][0]) + 1 if len(taskItems) > 0 else 1
            service.insert_data(f"insert into TaskItems values({itemId}, '{restaurants}', {taskId})", conn)

        taskLists = service.get_data(f"select * from TaskLists order by taskId desc", conn)
        taskId = int(taskLists[0][0]) + 1 if len(taskLists) > 0 else 1
        service.insert_data(f"insert into TaskLists values({taskId}, 'Recepies to cook in {arguments.city}', 'Recepies to cook in {arguments.city} in {output[3]} weather')", conn)
        for recipes in output[1][0]['Recipes']:
            taskItems = service.get_data(f"select * from TaskItems order by itemId desc", conn)
            itemId = int(taskItems[0][0]) + 1 if len(taskItems) > 0 else 1
            service.insert_data(f"insert into TaskItems values({itemId}, '{recipes}', {taskId})", conn)
        service.close_connection(conn)    
        print("\n\nThank you for using our service. Your bucket list has been updated.")
        print()
    else:
        # Do not add to bucket list
        print("\n\nThank you for using our service.")
        print()
