import time

def countdown(seconds):
    min = seconds // 60
    seconds = seconds % 60
    print(f"Countdown: {min:02}:{seconds:02}", end="\r")
    time.sleep(1)
    seconds -= 1

    if seconds >= 0:
        countdown(seconds)
    else:
        print("Time's up!")

if __name__ == "__main__":
    countdown(10)  