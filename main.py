import time

def generate_story():
    print("Generating horror story part...")
    # Placeholder: Insert AI story generation logic here

def post_to_platforms():
    print("Posting to X, YouTube Shorts, Instagram Reels...")
    # Placeholder: Insert API calls or automation logic here

def run_daily_schedule():
    schedule = ["09:00", "12:00", "15:00", "18:00"]
    while True:
        current_time = time.strftime("%H:%M")
        if current_time in schedule:
            generate_story()
            post_to_platforms()
            time.sleep(60)  # prevent double posts
        time.sleep(30)

if __name__ == "__main__":
    run_daily_schedule()
