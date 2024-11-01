import os
import re
import subprocess

def get_wifi_profiles():
    # Use nmcli to get a list of saved Wi-Fi profiles
    profiles_output = subprocess.check_output("nmcli connection show", shell=True).decode("utf-8")
    profiles = re.findall(r"([^\s]+)\s+[a-f0-9:-]+\s+wifi\s", profiles_output)
    return profiles

def get_wifi_password(profile):
    # Get the Wi-Fi password for a given profile
    try:
        password_output = subprocess.check_output(f"nmcli connection show \"{profile}\"", shell=True).decode("utf-8")
        password = re.search(r"802-11-wireless-security.psk\s*:\s*(.*)", password_output)
        return password.group(1) if password else None
    except subprocess.CalledProcessError:
        return None

def main():
    profiles = get_wifi_profiles()
    wifi_details = []

    for profile in profiles:
        password = get_wifi_password(profile)
        wifi_details.append({"Profile": profile, "Password": password})

    # Display Wi-Fi details
    for wifi in wifi_details:
        print(f"Profile: {wifi['Profile']}, Password: {wifi['Password']}")

if __name__ == "__main__":
    main()
