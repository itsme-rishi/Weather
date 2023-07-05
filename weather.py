import requests
my_api="e74d15b81b5759c45104c8edd0d8e752"
location=input("enter city :")
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
website_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+my_api
get_link=requests.get(website_link)
data=get_link.json()
print("{}".format(data))
if data['cod']=='404' :
    print('city not found please check the spelling:{}'.format(location))
else :
    max_temp=data['main']['temp_max']-273.15
    windspeed=data['wind']['speed']
    min_temp=data['main']['temp_min']-273.15
    curr_temp=data['main']['temp']-273.15
    hum=data['main']['humidity']
    feels_like=data['main']['feels_like']-273.15
    print("Temperatute right now is {:.1f} deg C".format(curr_temp))
    print("Temperature can a reach a max of :{:.1f} deg C".format(max_temp))
    print("Temperatue can fall upto :{:.1f} deg C".format(min_temp))
    print("Feels like :{:.1f} deg C".format(feels_like))
    print("Humidity :",hum,"%")
    print("Wind speed :{}kmph".format(windspeed))

