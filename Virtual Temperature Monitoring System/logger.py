from datetime import datetime
def log_to_console(temp, state):
    current_time= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} | Temperature: {temp}°C | State: {state}")

def log_to_file(temp, state, log_file="temperature_log.csv"):
    current_time= datetime.now().strftime("%H:%M:%S")
    with open(log_file, 'a') as f:
        f.write(f"{current_time},{temp},{state}\n")