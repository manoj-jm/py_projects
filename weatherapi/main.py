import requests
import pyttsx3 as p
e = p.init()
city = input("enter the city : ")
API_KEY= 'd2c50c8639e94907907122052242005'

url = f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no'


res = requests.get(url)
data = res.json();
# print(res.text);
# print(res.headers)

if res.headers['CDN-RequestPullSuccess']== "True":
  x = data['location']['name'];
  temp = data['current']['temp_c'];
  sts = data['current']['condition']['text'];
  data = f'Current temperature of {x} is {temp} and it is {sts}'
  print(f'Current temperature of {x} is {temp} and it is {sts}');
  e.say(data)
  e.runAndWait()

