import os
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# Get port from Render's environment variable or default to 10000
PORT = int(os.environ.get('PORT', 10000))

# Your core AI horror story generator logic (placeholder)
def generate_story(part):
    print(f"[{time.strftime('%H:%M:%S')}] Generating Part {part} of the horror story...")
    # TODO: Add your story generation, AI voice, and video creation here

# Simulated post function (expand with auto-posting logic later)
def post_to_platforms(part):
    print(f"[{time.strftime('%H:%M:%S')}] Posting Part {part} to TikTok, YouTube Shorts, IG Reels, and X...")
    # TODO: Add posting via APIs or automation tools like N8N, Zapier, etc.

# Your scheduled loop
def run_daily_schedule():
    schedule = {
        "09:00": 1,
        "12:00": 2,
        "15:00": 3,
        "18:00": 4
    }
    posted_today = set()

    while True:
        current_time = time.strftime("%H:%M")
        if current_time in schedule and current_time not in posted_today:
            part = schedule[current_time]
            generate_story(part)
            post_to_platforms(part)
            posted_today.add(current_time)

        if current_time == "00:00":  # Reset each new day
            posted_today.clear()

        time.sleep(30)

# Lightweight web server to keep Render happy
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OniTales Horror Engine is running.')

def start_web_server():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Web server running on port {PORT}...")
    httpd.serve_forever()

# Run everything
if __name__ == "__main__":
    threading.Thread(target=start_web_server, daemon=True).start()
    run_daily_schedule()
