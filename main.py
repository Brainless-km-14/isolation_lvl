import threading
import time
from lab_1_db import lost_update,in_place_update,low_level_locking,optimistic_concurrency_control

start_time = time.time()

threads = []
for i in range(10):
    #thread = threading.Thread(target=lost_update)
    #thread = threading.Thread(target=in_place_update)
    #thread = threading.Thread(target=low_level_locking)
    thread = threading.Thread(target=optimistic_concurrency_control)

    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(time.time() - start_time)