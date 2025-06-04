def classify_temperature(temp, normal_max=50, warning_max=75):
    if temp <= normal_max:
        return "NORMAL"
    elif temp <= warning_max:
        return "WARNING"
    else:
        return "CRITICAL"