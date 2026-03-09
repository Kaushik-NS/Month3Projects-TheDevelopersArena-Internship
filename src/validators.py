def validate_weather(weather):

    if weather["temperature"] < -100 or weather["temperature"] > 70:
        return False

    if weather["humidity"] < 0 or weather["humidity"] > 100:
        return False

    if weather["pressure"] < 800 or weather["pressure"] > 1200:
        return False

    return True