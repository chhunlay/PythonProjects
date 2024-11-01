import speedtest
from datetime import datetime
from tqdm import tqdm
import os
import time

def main():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create a list of steps to display progress
    steps = ["Initializing", "Fetching servers", "Selecting best server", "Performing download test", "Performing upload test", "Calculating results"]
    
    # Create a tqdm progress bar
    progress_bar = tqdm(total=len(steps), desc="Speed Test Progress", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} steps', dynamic_ncols=True)
    
    # Step 1: Initializing
    st = speedtest.Speedtest()
    progress_bar.update(1)
    time.sleep(1)  # Simulating the step duration

    # Step 2: Fetching servers
    st.get_servers()
    progress_bar.update(1)
    time.sleep(1)  # Simulating the step duration

    # Step 3: Selecting best server
    st.get_best_server()
    progress_bar.update(1)
    time.sleep(1)  # Simulating the step duration

    # Step 4: Performing download test
    download_speed = st.download()
    progress_bar.update(1)
    time.sleep(1)  # Simulating the step duration

    # Step 5: Performing upload test
    upload_speed = st.upload()
    progress_bar.update(1)
    time.sleep(1)  # Simulating the step duration

    # Step 6: Calculating results
    progress_bar.update(1)
    
    # Convert the speeds from bits per second to megabits per second
    download_speed_mbps = download_speed / 1_000_000
    upload_speed_mbps = upload_speed / 1_000_000
    
    # Get the current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Prepare the result string
    result = (
        f"Date and Time: {current_time}\n"
        f"Download speed: {download_speed_mbps:.2f} Mbps\n"
        f"Upload speed: {upload_speed_mbps:.2f} Mbps\n"
        "-------------------------------\n"
    )
    
    # Print the results
    print(result)
    
    # Ensure the logs directory exists within the script directory
    log_dir = os.path.join(script_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    # Save the results to a file in the logs directory within the script directory
    log_file_path = os.path.join(log_dir, "speedtest_results.txt")
    with open(log_file_path, "a") as file:
        file.write(result)
    
    # Close the progress bar
    progress_bar.close()

if __name__ == "__main__":
    main()
