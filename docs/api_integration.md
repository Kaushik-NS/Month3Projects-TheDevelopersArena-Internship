# API Integration

The system uses the OpenWeather API.

## Endpoint

https://api.openweathermap.org/data/2.5/weather

## Example Request

https://api.openweathermap.org/data/2.5/weather?q=Chennai&appid=API_KEY&units=metric

## Example Response

{
 "main": {
   "temp": 30.5,
   "humidity": 70,
   "pressure": 1012
 },
 "wind": {
   "speed": 4.2
 },
 "weather": [
   {
     "description": "clear sky"
   }
 ]
}