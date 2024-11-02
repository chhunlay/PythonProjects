import subprocess
import speedtest
import time
import sys
from geopy.geocoders import Nominatim
from datetime import datetime
import os  # To clear the output

def display_progress(iteration, total):
    percentage = (iteration / total) * 100
    bar_length = 30  # Length of the progress bar
    block = int(round(bar_length * percentage / 100))
    progress_bar = "#" * block + "-" * (bar_length - block)
    sys.stdout.write(f"\r[{progress_bar}] {percentage:.2f}%")
    sys.stdout.flush()

def clear_progress():
    # Clear the progress bar line
    sys.stdout.write("\r" + " " * 40 + "\r")  # Clear the line
    sys.stdout.flush()

def get_current_wifi():
    total_steps = 5  # Total steps for progress
    for step in range(total_steps):
        display_progress(step, total_steps)
        time.sleep(0.5)  # Simulate some processing time

    try:
        # Retrieve the full SSID
        ssid_command = "iwgetid -r"
        ssid_output = subprocess.check_output(ssid_command, shell=True).decode('utf-8').strip()

        # Retrieve the IP address
        ip_command = "hostname -I | awk '{print $1}'"
        ip_output = subprocess.check_output(ip_command, shell=True).decode('utf-8').strip()

    except subprocess.CalledProcessError as e:
        return {"Error": f"Could not retrieve Wi-Fi information: {e}"}

    # Update progress
    display_progress(2, total_steps)
    
    # Get the Wi-Fi password
    password = "Not accessible"
    try:
        password_command = f"sudo grep '^psk=' /etc/NetworkManager/system-connections/{ssid_output} 2>/dev/null"
        password_output = subprocess.check_output(password_command, shell=True).decode('utf-8').strip()
        password = password_output.split('=')[1].strip()
    except subprocess.CalledProcessError:
        password = "Not available"
    except IndexError:
        password = "Not found"

    # Update progress
    display_progress(3, total_steps)

    # Get upload and download speed
    try:
        speed_test = speedtest.Speedtest()
        speed_test.get_best_server()  # Find the best server for testing
        download_speed = round(speed_test.download() / 1_000_000, 2)  # Convert to Mbps
        upload_speed = round(speed_test.upload() / 1_000_000, 2)      # Convert to Mbps
    except Exception as e:
        download_speed = "Error"
        upload_speed = "Error"
        print(f"Speed test error: {e}")

    # Get current location
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(ip_output)  # Get location based on IP address
        latitude = location.latitude if location else "Not available"
        longitude = location.longitude if location else "Not available"
    except Exception as e:
        latitude = "Error"
        longitude = "Error"

    # Get current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Final update
    display_progress(4, total_steps)
    time.sleep(0.5)  # Ensure the progress reaches 100% before printing
    display_progress(5, total_steps)  # Final progress step
    print()  # Move to the next line after progress completion

    # Clear the progress line
    clear_progress()

    return {
        "Full Wi-Fi Name (SSID)": ssid_output,
        "IP Address": ip_output,
        "Password": password,
        "Download Speed (Mbps)": download_speed,
        "Upload Speed (Mbps)": upload_speed,
        "Latitude": latitude,
        "Longitude": longitude,
        "Current Date and Time": current_datetime
    }

if __name__ == "__main__":
    wifi_info = get_current_wifi()
    
    # Print results
    print(f"Full Wi-Fi Name (SSID): {wifi_info.get('Full Wi-Fi Name (SSID)', 'Not available')}")
    print(f"IP Address: {wifi_info.get('IP Address', 'Not available')}")
    print(f"Password: {wifi_info.get('Password', 'Not available')}")
    print(f"Download Speed (Mbps): {wifi_info.get('Download Speed (Mbps)', 'Error')}")
    print(f"Upload Speed (Mbps): {wifi_info.get('Upload Speed (Mbps)', 'Error')}")
    print(f"Latitude: {wifi_info.get('Latitude', 'Not available')}")
    print(f"Longitude: {wifi_info.get('Longitude', 'Not available')}")
    print(f"Current Date and Time: {wifi_info.get('Current Date and Time', 'Not available')}")
