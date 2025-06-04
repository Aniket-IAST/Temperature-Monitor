def take_action(state):
    if state == "NORMAL":
        return "Status OK"
    elif state == "WARNING":
        return "Warning issued"
    elif state == "CRITICAL":
        return "Fan ON + Alert triggered"