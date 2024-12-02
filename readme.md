# File Activity Monitor with SHA-256 Hash Calculation
This script monitors a specified directory for newly created files, calculates the SHA-256 hash of these files, and records the timestamps of file creation events. It also calculates and prints the time difference between the last two file creation events.

Set the directory you want to monitor by modifying the watch_path variable.

### How It Works
1. Monitoring Directory: The script uses pyinotify to watch for file creation events in the specified directory (watch_path).
2. File Creation Event: When a new file is created, the on_file_activity_detected function is triggered.
3. SHA-256 Calculation: The script calculates the SHA-256 hash of the newly created file.
4. Timestamp Management: The script writes the current timestamp to a file (timestamps.txt) and reads it to calculate the time difference between the last two file creation events.

### Functions
`calculate_sha(file_path)`
Calculates the SHA-256 hash of the specified file.
- file_path: Path to the file.
- Returns the SHA-256 hash as a hexadecimal string.
`on_file_activity_detected(event)`
Triggered when a new file is created. Prints the file path and its SHA-256 hash, and reads the time difference from the timestamps.txt file.
- event: Event object containing details of the file activity.
`write_timestamp_to_file(timestamp, file_path)`
Writes the given timestamp to the timestamps.txt file.
- timestamp: Current timestamp.
- file_path: Path to the timestamps.txt file.
`read_time_difference_from_file(file_path)`
Reads the timestamps.txt file and calculates the time difference between the last two file creation events.
- file_path: Path to the timestamps.txt file.

The script will start monitoring the specified directory and print the details of newly created files, including their SHA-256 hashes and the time difference between file creations.

### Stopping the Script
To stop the script, press Ctrl+C. This will stop the notifier loop and print "Watcher stopped."

### Notes
- Ensure the watch_path directory exists before running the script.
- The `timestamps.txt` file is created in the `watch_path` directory to store timestamps of file creation events.

This script is useful for monitoring directory activities, verifying file integrity with SHA-256 hashes, and tracking the timing of file creation events.