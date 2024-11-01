import re
import subprocess
from prettytable import PrettyTable

def get_wifi_profiles():
    # Use nmcli to get a list of saved Wi-Fi profiles
    profiles_output = subprocess.check_output("nmcli connection show", shell=True).decode("utf-8")
    # Update the regex to match Wi-Fi profiles with spaces and special characters
    profiles = re.findall(r"^(.*?)\s+[a-f0-9:-]+\s+wifi\s", profiles_output, re.MULTILINE)
    return [profile.strip() for profile in profiles]

def get_wifi_password(profile):
    # Get the Wi-Fi password for a given profile using --show-secrets
    try:
        password_output = subprocess.check_output(f"nmcli connection show \"{profile}\" --show-secrets", shell=True).decode("utf-8")
        password = re.search(r"psk\s*:\s*(.*)", password_output)
        if password:
            return password.group(1).strip()
        else:
            return "No password set"
    except subprocess.CalledProcessError:
        return "Error retrieving password"

def main():
    profiles = get_wifi_profiles()
    wifi_details = []

    for profile in profiles:
        password = get_wifi_password(profile)
        wifi_details.append({"Profile": profile, "Password": password})

    # Create a PrettyTable instance
    table = PrettyTable()
    table.field_names = ["Profile", "Password"]

    # Center align the header and left align the data
    for field in table.field_names:
        table.align[field] = "c"  # Center align headers
    table.align["Profile"] = "l"  # Left align Profile data
    table.align["Password"] = "l"  # Left align Password data

    # Add rows to the table
    for wifi in wifi_details:
        table.add_row([wifi['Profile'], wifi['Password']])

    # Display the Wi-Fi details in a table format
    print(table)

if __name__ == "__main__":
    main()
