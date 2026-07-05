from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# ---- SETTINGS ----
PERSON_CONF = 0.5
PHONE_CONF = 0.4
MIN_PHONE_AREA = 800

# ---- MEMORY (anti-flicker) ----
PHONE_HOLD_FRAMES = 6
last_phone = None
phone_timer = 0


def detect(frame):
    global last_phone, phone_timer

    results = model(frame)

    best_person = None
    best_phone = None

    for r in results:
        for box in r.boxes:

            cls = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Only person (0) and phone (67)
            if cls not in [0, 67]:
                continue

            width = x2 - x1
            height = y2 - y1
            area = width * height

            # -------- PERSON (largest = driver) --------
            if cls == 0:
                if conf < PERSON_CONF:
                    continue

                if best_person is None or area > best_person["area"]:
                    best_person = {
                        "box": [x1, y1, x2, y2],
                        "area": area
                    }

            # -------- PHONE --------
            elif cls == 67:
                if conf < PHONE_CONF or area < MIN_PHONE_AREA:
                    continue

                if best_phone is None or conf > best_phone["conf"]:
                    best_phone = {
                        "box": [x1, y1, x2, y2],
                        "conf": conf
                    }

    # -------- PHONE MEMORY (ANTI-FLICKER) --------
    if best_phone:
        last_phone = best_phone
        phone_timer = PHONE_HOLD_FRAMES
    else:
        if phone_timer > 0:
            phone_timer -= 1
            best_phone = last_phone
        else:
            last_phone = None

    # -------- CLEAN OUTPUT --------
    output = {
        "persons": [],
        "phones": []
    }

    if best_person:
        output["persons"].append(best_person["box"])

    if best_phone:
        output["phones"].append(best_phone["box"])

    return output


# Wrapper (important for main.py)
def detect_objects(frame):
    return detect(frame)