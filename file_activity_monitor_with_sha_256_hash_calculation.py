#!pip install pyinotify

import pyinotify
import hashlib
import os
import time

watch_path = './sample_data/'

def calculate_sha(file_path):
    sha = hashlib.sha256()

    with open(file_path, 'rb') as f:
        chunk_size = 8192
        for chunk in iter(lambda: f.read(chunk_size), b''):
            sha.update(chunk)

    return sha.hexdigest()

def on_file_activity_detected(event):
    new_file_path = event.pathname
    print(f"File created: {new_file_path}")

    # Calculate the SHA hash of the newly created file
    sha_result = calculate_sha(new_file_path)
    print(f"SHA256 hash of '{new_file_path}': {sha_result}")

    # Read and print the time difference
    read_time_difference_from_file()

def write_timestamp_to_file(timestamp, file_path= watch_path + 'timestamps.txt'):
    with open(file_path, 'a') as f:
        f.write(f"{timestamp}\n")

def read_time_difference_from_file(file_path= watch_path + 'timestamps.txt'):
    try:
        with open(file_path, 'r') as f:
            timestamps = [float(line.strip()) for line in f.readlines()]

        if len(timestamps) >= 2:
            time_difference = timestamps[-1] - timestamps[-2]
            print(f"Time difference between the last two file creations: {time_difference:.2f} seconds")
        else:
            print("Insufficient data to calculate time difference.")
    except FileNotFoundError:
        print("Timestamps file not found.")


# Usage
# Create an inotify object
wm = pyinotify.WatchManager()

# Set up a watch on the specified directory
watch_mask = pyinotify.IN_CREATE  # Watch for file creation events
handler = pyinotify.ProcessEvent()
notifier = pyinotify.Notifier(wm, handler)

# Add a watch to the specified directory
wm.add_watch(watch_path, watch_mask)

# Set up the event handler
handler.process_IN_CREATE = on_file_activity_detected

try:
    # Start the notifier loop
    print(f"Watching directory: {watch_path}")
    notifier.loop()
except KeyboardInterrupt:
    # Stop the notifier on keyboard interrupt
    notifier.stop()
    print("Watcher stopped.")


"""
Watching directory: ./sample_data/
File created: /content/sample_data/.~timestamps.txt
SHA256 hash of '/content/sample_data/.~timestamps.txt': e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Time difference between the last two file creations: 51.51 seconds
File created: /content/sample_data/.~timestamps.txt
SHA256 hash of '/content/sample_data/.~timestamps.txt': ad3aa73348d59f65bfce1855a534f3ca1ffe1d1d93c7624ee1c1946d9c0c5bc8
Time difference between the last two file creations: 61.51 seconds
"""

time.sleep(3)
# Write the current timestamp to the file
current_timestamp = time.time()
print(f"adding current_timestamp: {current_timestamp}")
write_timestamp_to_file(current_timestamp)
print(f"adding current_timestamp: [done]")

"""
adding current_timestamp: 1710056594.4155414
adding current_timestamp: [done]
"""