import time
import pandas as pd
from config import VirtualSensor
from thresholds import classify_temperature
from response_manager import take_action
from logger import log_to_console, log_to_file
from CLI_display import display_status
from GUI_display import launch_temperature_gui
from email_alert import send_email_alert
from datetime import datetime

sensor = VirtualSensor(mode='trend')

temp_log = [] #GUI temperature log

#Email alert setup
prev_state = None
last_email_time = 0
email_cooldown = 600

try:
    for _ in range(200):
        temp = sensor.read_raw()
        state = classify_temperature(temp)
        response = take_action(state)
        log_to_console(temp, state)
        log_to_file(temp, state)
        display_status(temp, state, response)

        # Appending to GUI log
        temp_log.append({"Timestamp": datetime.now(), "Temperature": temp, "State": state}) 

        # Email alert 
        if state == "CRITICAL" and (prev_state != "CRITICAL" or (time.time() - last_email_time > email_cooldown)):
            send_email_alert(temp)
            last_email_time = time.time()
        prev_state = state

        time.sleep(1)

except KeyboardInterrupt:
    print("Monitoring stopped by user.")

df = pd.DataFrame(temp_log) # Convert to DataFrame for GUI display
launch_temperature_gui(df) # This will launch the GUI to visualize the temperature data
