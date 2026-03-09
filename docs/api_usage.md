# OpenWeather API Usage

The pipeline uses the OpenWeather API to fetch weather information.

## Endpoint

https://api.openweathermap.org/data/2.5/weather

## Example Request

https://api.openweathermap.org/data/2.5/weather?q=Chennai&appid=API_KEY&units=metric

## Returned Data

The API provides the following fields:

- Temperature
- Humidity
- Pressure
- Wind Speed
- Weather Condition

## Example Response

{
  "main": {
    "temp": 30.5,
    "humidity": 70,
    "pressure": 1012
  },
  "wind": {
    "speed": 4.5
  },
  "weather": [
    {
      "description": "clear sky"
    }
  ]
}