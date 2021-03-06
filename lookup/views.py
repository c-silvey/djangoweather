from django.shortcuts import render

def dashboard(request):
    import json
    import requests
    from uszipcode import SearchEngine, SimpleZipcode, Zipcode

    if request.method == 'POST':
        zipcode = request.POST['zipsearch']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=0F165C58-600F-450D-91F7-90B66B9B8B46")

        try:
            api = json.loads(api_request.content)
        
        except Exception as e:
            api = "Error..."

    else:
    
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=93405&distance=25&API_KEY=0F165C58-600F-450D-91F7-90B66B9B8B46")

    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error..."

#cases for O3  
    try:
        if api[0]['ParameterName'] == 'O3':
            O3_aqi = api[0]['AQI']
            if api[0]['Category']['Number'] == 1:
                O3_name = api[0]['Category']['Name'] + ' (0 - 50)'
                O3_description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
                O3_color = 'good'
            elif api[0]['Category']['Number'] == 2:
                O3_name = api[0]['Category']['Name'] + ' (51 - 100)'
                O3_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                O3_color = 'moderate'
            elif api[0]['Category']['Number'] == 3:
                O3_name = api[0]['Category']['Name'] + ' (101 - 200)'
                O3_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                O3_color = 'usg'
            elif api[0]['Category']['Number'] == 4:
                O3_name = api[0]['Category']['Name'] + ' (201 - 250)'
                O3_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
                O3_color = 'unhealthy'
            elif api[0]['Category']['Number'] == 5:
                O3_name = api[0]['Category']['Name'] + ' (251 - 300)'
                O3_description = 'Health alert: The risk of health effects is increased for everyone.'
                O3_color = 'veryunhealthy'
            elif api[0]['Category']['Number'] == 6:
                O3_name = api[0]['Category']['Name'] + ' (301+)'
                O3_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
                O3_color = 'hazardous'
            else:
                pass

        elif api[1]['ParameterName'] == 'O3':
            O3_aqi = api[1]['AQI']
            if api[1]['Category']['Number'] == 1:
                O3_name = api[1]['Category']['Name'] + ' (0 - 50)'
                O3_description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
                O3_color = 'good'
            elif api[1]['Category']['Number'] == 2:
                O3_name = api[1]['Category']['Name'] + ' (51 - 100)'
                O3_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                O3_color = 'moderate'
            elif api[1]['Category']['Number'] == 3:
                O3_name = api[1]['Category']['Name'] + ' (101 - 200)'
                O3_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                O3_color = 'usg'
            elif api[1]['Category']['Number'] == 4:
                O3_name = api[1]['Category']['Name'] + ' (201 - 250)'
                O3_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
                O3_color = 'unhealthy'
            elif api[1]['Category']['Number'] == 5:
                O3_name = api[1]['Category']['Name'] + ' (251 - 300)'
                O3_description = 'Health alert: The risk of health effects is increased for everyone.'
                O3_color = 'veryunhealthy'
            elif api[1]['Category']['Number'] == 6:
                O3_name = api[1]['Category']['Name'] + ' (301+)'
                O3_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
                O3_color = 'hazardous'
            else:
                pass

        elif api[2]['ParameterName'] == 'O3':
            O3_aqi = api[2]['AQI']
            if api[2]['Category']['Number'] == 1:
                O3_name = api[2]['Category']['Name'] + ' (0 - 50)'
                O3_description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
                O3_color = 'good'
            elif api[2]['Category']['Number'] == 2:
                O3_name = api[2]['Category']['Name'] + ' (51 - 100)'
                O3_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                O3_color = 'moderate'
            elif api[2]['Category']['Number'] == 3:
                O3_name = api[2]['Category']['Name'] + ' (101 - 200)'
                O3_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                O3_color = 'usg'
            elif api[2]['Category']['Number'] == 4:
                O3_name = api[2]['Category']['Name'] + ' (201 - 250)'
                O3_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
                O3_color = 'unhealthy'
            elif api[2]['Category']['Number'] == 5:
                O3_name = api[2]['Category']['Name'] + ' (251 - 300)'
                O3_description = 'Health alert: The risk of health effects is increased for everyone.'
                O3_color = 'veryunhealthy'
            elif api[2]['Category']['Number'] == 6:
                O3_name = api[2]['Category']['Name'] + ' (301+)'
                O3_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
                O3_color = 'hazardous'
            else:
                pass
        else:
            pass
    except IndexError:
        O3_aqi = 'No Data'
        O3_name = 'No Data'
        O3_description = 'No Data'
        O3_color = 'alert-dark'

#cases for PM2
    try:
        if api[0]['ParameterName'] == 'PM2.5':
            PM2_aqi = api[0]['AQI']
            if api[0]['Category']['Number'] == 1:
                PM2_name = api[0]['Category']['Name'] + ' (0 - 50)'
                PM2_description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
                PM2_color = 'good'
            elif api[0]['Category']['Number'] == 2:
                PM2_name = api[0]['Category']['Name'] + ' (51 - 100)'
                PM2_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                PM2_color = 'moderate'
            elif api[0]['Category']['Number'] == 3:
                PM2_name = api[0]['Category']['Name'] + ' (101 - 200)'
                PM2_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                PM2_color = 'usg'
            elif api[0]['Category']['Number'] == 4:
                PM2_name = api[0]['Category']['Name'] + ' (201 - 250)'
                PM2_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
                PM2_color = 'unhealthy'
            elif api[0]['Category']['Number'] == 5:
                PM2_name = api[0]['Category']['Name'] + ' (251 - 300)'
                PM2_description = 'Health alert: The risk of health effects is increased for everyone.'
                PM2_color = 'veryunhealthy'
            elif api[0]['Category']['Number'] == 6:
                PM2_name = api[0]['Category']['Name'] + ' (301+)'
                PM2_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
                PM2_color = 'hazardous'
            else:
                pass

        elif api[1]['ParameterName'] == 'PM2.5':
            PM2_aqi = api[1]['AQI']
            if api[1]['Category']['Number'] == 1:
                PM2_name = api[1]['Category']['Name'] + ' (0 - 50)'
                PM2_description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
                PM2_color = 'good'
            elif api[1]['Category']['Number'] == 2:
                PM2_name = api[1]['Category']['Name'] + ' (51 - 100)'
                PM2_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                PM2_color = 'moderate'
            elif api[1]['Category']['Number'] == 3:
                PM2_name = api[1]['Category']['Name'] + ' (101 - 200)'
                PM2_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                PM2_color = 'usg'
            elif api[1]['Category']['Number'] == 4:
                PM2_name = api[1]['Category']['Name'] + ' (201 - 250)'
                PM2_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
                PM2_color = 'unhealthy'
            elif api[1]['Category']['Number'] == 5:
                PM2_name = api[1]['Category']['Name'] + ' (251 - 300)'
                PM2_description = 'Health alert: The risk of health effects is increased for everyone.'
                PM2_color = 'veryunhealthy'
            elif api[1]['Category']['Number'] == 6:
                PM2_name = api[1]['Category']['Name'] + ' (301+)'
                PM2_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
                PM2_color = 'hazardous'
            else:
                pass

        elif api[2]['ParameterName'] == 'PM2.5':
            PM2_aqi = api[2]['AQI']
            if api[2]['Category']['Number'] == 1:
                PM2_name = api[2]['Category']['Name'] + ' (0 - 50)'
                PM2_description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
                PM2_color = 'good'
            elif api[2]['Category']['Number'] == 2:
                PM2_name = api[2]['Category']['Name'] + ' (51 - 100)'
                PM2_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                PM2_color = 'moderate'
            elif api[2]['Category']['Number'] == 3:
                PM2_name = api[2]['Category']['Name'] + ' (101 - 200)'
                PM2_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                PM2_color = 'usg'
            elif api[2]['Category']['Number'] == 4:
                PM2_name = api[2]['Category']['Name'] + ' (201 - 250)'
                PM2_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
                PM2_color = 'unhealthy'
            elif api[2]['Category']['Number'] == 5:
                PM2_name = api[2]['Category']['Name'] + ' (251 - 300)'
                PM2_description = 'Health alert: The risk of health effects is increased for everyone.'
                PM2_color = 'veryunhealthy'
            elif api[2]['Category']['Number'] == 6:
                PM2_name = api[2]['Category']['Name'] + ' (301+)'
                PM2_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
                PM2_color = 'hazardous'
            else:
                pass
        else:
            pass
    except IndexError:
        PM2_aqi = 'No Data'
        PM2_name = 'No Data'
        PM2_description = 'No Data'
        PM2_color = 'alert-dark'

#cases for PM10

    try:
        if api[0]['ParameterName'] == 'PM10':
            PM10_aqi = api[0]['AQI']
            if api[0]['Category']['Number'] == 1:
                PM10_name = api[0]['Category']['Name'] + ' (0 - 50)'
                PM10_description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
                PM10_color = 'good'
            elif api[0]['Category']['Number'] == 2:
                PM10_name = api[0]['Category']['Name'] + ' (51 - 100)'
                PM10_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                PM10_color = 'moderate'
            elif api[0]['Category']['Number'] == 3:
                PM10_name = api[0]['Category']['Name'] + ' (101 - 200)'
                PM10_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                PM10_color = 'usg'
            elif api[0]['Category']['Number'] == 4:
                PM10_name = api[0]['Category']['Name'] + ' (201 - 250)'
                PM10_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
                PM10_color = 'unhealthy'
            elif api[0]['Category']['Number'] == 5:
                PM10_name = api[0]['Category']['Name'] + ' (251 - 300)'
                PM10_description = 'Health alert: The risk of health effects is increased for everyone.'
                PM10_color = 'veryunhealthy'
            elif api[0]['Category']['Number'] == 6:
                PM10_name = api[0]['Category']['Name'] + ' (301+)'
                PM10_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
                PM10_color = 'hazardous'
            else:
                pass

        elif api[1]['ParameterName'] == 'PM10':
            PM10_aqi = api[1]['AQI']
            if api[1]['Category']['Number'] == 1:
                PM10_name = api[1]['Category']['Name'] + ' (0 - 50)'
                PM10_description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
                PM10_color = 'good'
            elif api[1]['Category']['Number'] == 2:
                PM10_name = api[1]['Category']['Name'] + ' (51 - 100)'
                PM10_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                PM10_color = 'moderate'
            elif api[1]['Category']['Number'] == 3:
                PM10_name = api[1]['Category']['Name'] + ' (101 - 200)'
                PM10_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                PM10_color = 'usg'
            elif api[1]['Category']['Number'] == 4:
                PM10_name = api[1]['Category']['Name'] + ' (201 - 250)'
                PM10_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
                PM10_color = 'unhealthy'
            elif api[1]['Category']['Number'] == 5:
                PM10_name = api[1]['Category']['Name'] + ' (251 - 300)'
                PM10_description = 'Health alert: The risk of health effects is increased for everyone.'
                PM10_color = 'veryunhealthy'
            elif api[1]['Category']['Number'] == 6:
                PM10_name = api[1]['Category']['Name'] + ' (301+)'
                PM10_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
                PM10_color = 'hazardous'
            else:
                pass
        
        elif api[2]['ParameterName'] == 'PM10':
            PM10_aqi = api[2]['AQI']
            if api[2]['Category']['Number'] == 1:
                PM10_name = api[2]['Category']['Name'] + ' (0 - 50)'
                PM10_description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
                PM10_color = 'good'
            elif api[2]['Category']['Number'] == 2:
                PM10_name = api[2]['Category']['Name'] + ' (51 - 100)'
                PM10_description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                PM10_color = 'moderate'
            elif api[2]['Category']['Number'] == 3:
                PM10_name = api[2]['Category']['Name'] + ' (101 - 200)'
                PM10_description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                PM10_color = 'usg'
            elif api[2]['Category']['Number'] == 4:
                PM10_name = api[2]['Category']['Name'] + ' (201 - 250)'
                PM10_description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
                PM10_color = 'unhealthy'
            elif api[2]['Category']['Number'] == 5:
                PM10_name = api[2]['Category']['Name'] + ' (251 - 300)'
                PM10_description = 'Health alert: The risk of health effects is increased for everyone.'
                PM10_color = 'veryunhealthy'
            elif api[2]['Category']['Number'] == 6:
                PM10_name = api[2]['Category']['Name'] + ' (301+)'
                PM10_description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
                PM10_color = 'hazardous'
            else:
                pass
        else:
            pass
    except IndexError:
        PM10_aqi = 'No Data'
        PM10_name = 'No Data'
        PM10_description = 'No Data'
        PM10_color = 'alert-dark'

    return render(request, 'dashboard.html', {'api': api, 'O3_aqi': O3_aqi, 'O3_name': O3_name, 'O3_description': O3_description, 'O3_color': O3_color, 'PM2_aqi': PM2_aqi, 'PM2_name': PM2_name, 'PM2_description': PM2_description, 'PM2_color': PM2_color, 'PM10_aqi': PM10_aqi, 'PM10_name': PM10_name, 'PM10_description': PM10_description, 'PM10_color': PM10_color})



    

def home(request):
    return render(request, 'home.html', {})
    


def about(request):
    return render(request, 'about.html', {})