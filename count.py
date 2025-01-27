import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert seconds to minutes and seconds
        time_str = f"{mins:02d}:{secs:02d}"
        print(time_str, end='\r')  # Print the time, overwrite the line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrease the seconds by 1
    
    print("00:00")  # When the countdown finishes
    print("Time's up!")

def main():
    try:
        total_seconds = int(input("Enter the countdown time in seconds: "))
        print("\nStarting Countdown...")
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid integer value.")

if __name__ == "__main__":
    main()
