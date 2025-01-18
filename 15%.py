#   tsk.tax.cpu  #
import time
import math
import threading

def cpu_intensive_task():
    while time.time() - cpu_intensive_task.start_time < 30:
        for i in range(100000):
            math.sqrt(i * i + 1)

cpu_intensive_task.start_time = time.time()
threads = []
num_threads = 4 # Number of threads (adjust to your CPU core count)
for _ in range(num_threads):
    thread = threading.Thread(target=cpu_intensive_task)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() # Wait for all threads to finish

# ---------------------------------------------------------------  #
import time
import threading

def cpu_intensive_task(stop_event):
    # Function to perform CPU-intensive calculations
    while not stop_event.is_set():
        # Perform some heavy calculations
        [x**2 for x in range(10**6)]

def main():
    # Create an event to signal threads to stop
    stop_event = threading.Event()

    # Create multiple threads to maximize CPU usage
    threads = []
    for _ in range(4):  # Adjust the number of threads based on your CPU cores
        thread = threading.Thread(target=cpu_intensive_task, args=(stop_event,))
        threads.append(thread)
        thread.start()

    # Let the threads run for 30 seconds
    time.sleep(30)

    # Signal threads to stop
    stop_event.set()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("CPU task completed.")

if __name__ == "__main__":
    main()
