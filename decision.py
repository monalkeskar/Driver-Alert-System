import time

phone_start_time = None
focus_counter = 0
last_alert_time = 0

ALERT_COOLDOWN = 2

def decision_engine(data):
    global phone_start_time, focus_counter, last_alert_time

    phones = data.get("phones", [])
    head_direction = data.get("head_direction", "center")

    current_time = time.time()

    # -------------------------
    # PHONE LOGIC (PRIORITY)
    # -------------------------
    if len(phones) > 0:
        if phone_start_time is None:
            phone_start_time = current_time

        elif current_time - phone_start_time > 2.5:
            
            if current_time - last_alert_time > ALERT_COOLDOWN:
                last_alert_time = current_time
            return "phone_alert"   # <-- ALWAYS return

    else:
        phone_start_time = None

    # -------------------------
    # FOCUS LOGIC
    # -------------------------
    if head_direction == "down":
        focus_counter += 1

        if focus_counter > 12:
            if current_time - last_alert_time > ALERT_COOLDOWN:
                last_alert_time = current_time
            return "focus_alert"   # <-- ALWAYS return

    else:
        focus_counter = 0

    return "safe"