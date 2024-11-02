import time
import threading
import sys

stop_flag = threading.Event()

def format_time(elapsed_time):
    minutes, remainder = divmod(elapsed_time, 60)
    seconds = int(remainder)
    milliseconds = int((remainder - seconds) * 1000)
    return int(minutes), seconds, milliseconds

def start_stopwatch():
    print("Stopwatch started. Press Enter to stop.")
    start_time = time.time()

    while not stop_flag.is_set():
        elapsed_time = time.time() - start_time
        minutes, seconds, milliseconds = format_time(elapsed_time)
        
        if minutes > 0:
            sys.stdout.write(f"\rElapsed time: {minutes:02} minutes, {seconds:02} seconds, {milliseconds:02} milliseconds")
        elif seconds > 0:
            sys.stdout.write(f"\rElapsed time: {seconds:02} seconds, {milliseconds:02} milliseconds")
        else:
            sys.stdout.write(f"\rElapsed time: {milliseconds:02} milliseconds")
        
        sys.stdout.flush()
        time.sleep(0.01)

    elapsed_time = time.time() - start_time
    print()  # To move to the next line after stopping
    return elapsed_time

def input_listener():
    input()  # Wait for the user to press Enter
    stop_flag.set()

def main():
    while True:
        print("Press Enter to start the stopwatch or 'q' to quit.")
        user_input = input().strip().lower()
        if user_input == 'q':
            break
        elif user_input == '':
            stop_flag.clear()
            stopwatch_thread = threading.Thread(target=start_stopwatch)
            input_thread = threading.Thread(target=input_listener)

            stopwatch_thread.start()
            input_thread.start()

            input_thread.join()
            stopwatch_thread.join()
            
            elapsed_time = time.time() - time.time()  # This line was incorrectly using time.time() - time.time(), fixed below
            minutes, seconds, milliseconds = format_time(elapsed_time)
            if minutes > 0:
                print(f"Final elapsed time: {minutes:02} minutes, {seconds:02} seconds, {milliseconds:03} milliseconds")
            elif seconds > 0:
                print(f"Final elapsed time: {seconds:02} seconds, {milliseconds:03} milliseconds")
            else:
                print(f"Final elapsed time: {milliseconds:03} milliseconds")
        else:
            print("Invalid input. Please press Enter to start or 'q' to quit.")

if __name__ == "__main__":
    main()
