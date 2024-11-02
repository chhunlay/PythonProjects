import subprocess
import speedtest

def get_current_wifi():
    # Get the Wi-Fi SSID (full name) and IP address
    try:
        # Retrieve the full SSID
        ssid_command = "iwgetid -r"
        ssid_output = subprocess.check_output(ssid_command, shell=True).decode('utf-8').strip()
        print(f"Detected SSID: {ssid_output}")  # Debug output

        # Retrieve the IP address
        ip_command = "hostname -I | awk '{print $1}'"
        ip_output = subprocess.check_output(ip_command, shell=True).decode('utf-8').strip()
        print(f"Detected IP: {ip_output}")  # Debug output

    except subprocess.CalledProcessError as e:
        return {"Error": "Could not retrieve Wi-Fi information"}

    # Get the Wi-Fi password
    password = "Not accessible"
    try:
        # Properly quote the SSID to handle spaces
        password_command = f"sudo grep '^psk=' /etc/NetworkManager/system-connections/{ssid_output}"
        print(f"Running command to get password: {password_command}")  # Debug output
        password_output = subprocess.check_output(password_command, shell=True).decode('utf-8').strip()
        password = password_output.split('=')[1].strip()
    except subprocess.CalledProcessError:
        password = "Not available"
    except IndexError:
        password = "Not found"

    # Get upload and download speed
    try:
        speed_test = speedtest.Speedtest()
        speed_test.get_best_server()  # Get the best server
        download_speed = speed_test.download(timeout=10) / 1_000_000  # Convert to Mbps
        upload_speed = speed_test.upload(timeout=10) / 1_000_000      # Convert to Mbps
    except Exception as e:
        download_speed = "Error"
        upload_speed = "Error"

    return {
        "Full Wi-Fi Name (SSID)": ssid_output,
        "IP Address": ip_output,
        "Password": password,
        "Download Speed (Mbps)": download_speed,
        "Upload Speed (Mbps)": upload_speed
    }

if __name__ == "__main__":
    wifi_info = get_current_wifi()
    for key, value in wifi_info.items():
        print(f"{key}: {value}")
