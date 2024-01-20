# ISS Tracker & Notification System 🛰️🌌

This Python script tracks the International Space Station (ISS) using its real-time coordinates obtained from the Open Notify API. If the ISS is within a specified range of your location, the script sends an email alert during the night hours.

## Features
- **Real-time ISS Tracking:** Utilizes the Open Notify API to fetch the ISS's current latitude and longitude.
- **Location-based Alert:** Checks whether the ISS is within a predefined range of your location (latitude and longitude).
- **Sunrise-Sunset Data:** Retrieves sunrise and sunset times using the Sunrise-Sunset API to determine night hours.
- **Email Notification:** Sends an email alert if the ISS is visible during the night.

## How to Use
1. Replace `MY_LAT` and `MY_LONG` with your latitude and longitude.
2. Replace `MY_EMAIL` and `PASSWORD` with your Gmail credentials.
3. Run the script to continuously monitor the ISS location.

## Dependencies
- **Requests:** Handles API requests.
- **Datetime:** Manages date and time.
- **Smtplib:** Allows sending email alerts.
- **Time:** Enables time-related functions.


**Note:** Make sure to enable 'Less secure app access' for your Gmail account for successful email sending.

Feel free to explore and enhance this ISS Tracker script! 🚀✨
