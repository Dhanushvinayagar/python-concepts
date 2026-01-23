import threading
import time

def download_file(file_id):
    print(f"Downloading file {file_id}...")
    time.sleep(2)  # Simulate waiting for I/O
    print(f"Finished file {file_id}")


# without multithreading
start = time.time()

for i in range(5):
    download_file(i)

print("Total time:", time.time() - start)

threads = []

# with multithreading
start = time.time()

for i in range(5):
    t = threading.Thread(target=download_file, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Total time:", time.time() - start)
