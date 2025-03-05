import time
import json
import psutil
import plyer
import subprocess

# Load config file
with open("config.json", "r") as file:
    config = json.load(file)

SCREEN_TIME_LIMIT = config["screen_time_limit"]  # in minutes
ALERT_INTERVAL = config["alert_interval"]  # in minutes

def is_user_active():
    """Check if the user is active using xdotool."""
    try:
        last_event = subprocess.getoutput("xdotool getmouselocation --shell | grep WINDOW")
        return bool(last_event)  # If mouse moves, user is active
    except Exception:
        return True  # Assume active if check fails

def get_active_time():
    """Calculate system uptime in minutes."""
    uptime_seconds = time.time() - psutil.boot_time()
    return uptime_seconds / 60  # Convert to minutes

def send_alert():
    """Send a desktop notification when screen time exceeds the limit."""
    plyer.notification.notify(
        title="⚠️ Screen Time Alert!",
        message=f"You have been using your screen for more than {SCREEN_TIME_LIMIT} minutes. Take a break!",
        timeout=10
    )

if __name__ == "__main__":
    print("🔍 Screen Time Monitor Running...")

    while True:
        active_time = get_active_time()

        if active_time > SCREEN_TIME_LIMIT and is_user_active():
            send_alert()
            time.sleep(ALERT_INTERVAL * 60)  # Wait before sending another alert
        else:
            time.sleep(60)  # Check every minute
