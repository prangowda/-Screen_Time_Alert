 🖥️ Screen Time Monitor & Alert (Linux)

## 📌 Overview
The **Screen Time Monitor & Alert System** is a **Linux-based** application that tracks your total screen usage and alerts you when your screen time exceeds a predefined limit. It runs **silently in the background** and sends **desktop notifications** if the user exceeds the set limit.

This project is ideal for **improving digital well-being** and **reducing excessive screen time**.

---

## 🚀 Features
✅ **Tracks screen time** in real-time  
✅ **Sends desktop notifications** when the screen time exceeds the limit  
✅ **Monitors user activity** using `xdotool`  
✅ **Runs in the background** without disturbing user workflow  
✅ **Customizable settings** via `config.json`  

---

## 📁 Project Structure
```
📦 Screen_Time_Alert
 ┣ 📜 screen_time_monitor.py   # Main script for tracking screen time
 ┣ 📜 config.json              # Configuration file for time limit
 ┣ 📜 README.md                # Project documentation
 ┣ 📜 requirements.txt         # Required dependencies
```

---

## 🛠 Technologies Used
- **Python** - Core programming language  
- **xdotool** - Detects user activity (mouse movement)  
- **Psutil** - Fetches system uptime  
- **Plyer** - Sends desktop notifications  

---

## 🔗 Dependencies
The following libraries are required for the project:

```
psutil
plyer
```

---

## ⚙️ Installation & Setup

### 1️⃣ Install Required Dependencies
```bash
sudo apt update
sudo apt install xdotool  # Required for detecting user activity
pip install -r requirements.txt
```

### 2️⃣ Run the Program
```bash
python screen_time_monitor.py
```

### 3️⃣ (Optional) Run as Background Process
To keep the monitor running even after closing the terminal:
```bash
nohup python screen_time_monitor.py &
```

---

## 📜 Configuration
You can **modify the screen time limit and alert frequency** in the `config.json` file.

```json
{
    "screen_time_limit": 120,   // Alert after 120 minutes (2 hours)
    "alert_interval": 30        // Notify every 30 minutes if exceeded
}
```

- `screen_time_limit`: Maximum screen time before alert (in minutes).  
- `alert_interval`: Time interval before the next alert (in minutes).  

---

## 📖 How It Works
1️⃣ The script **monitors system uptime** and tracks **active screen usage**.  
2️⃣ It **detects user activity** using `xdotool` to check mouse movement.  
3️⃣ If the **screen time exceeds the set limit**, a **desktop notification** appears.  
4️⃣ The script waits for **30 minutes** before sending another alert.  

---

## 📸 Screenshot (Example Notification)
When the screen time exceeds the limit, the system sends a notification like this:

![Screen Time Alert Example](https://user-images.githubusercontent.com/12345678/example.jpg)  


---

## 🛠️ Future Enhancements
✅ **Add a GUI for customization**  
✅ **Generate daily reports on screen time**  
✅ **Provide graphical statistics**  

