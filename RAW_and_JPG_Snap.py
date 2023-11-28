import time
import os
from datetime import datetime
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
directory = "/home/admin"    ###Set the Directory in Which Files are saved
#if not os.path.exists(directory):  ###Add this later for feature corrections
    #os.makedirs(directory)

preview_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration(raw={}, display=None)
picam2.configure(preview_config)

### Create a class to ensure that filenames are unique when saving
def generate_unique_filename(extension):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{timestamp}.{extension}"

picam2.start()
time.sleep(0.5)  ###Sped up wait before function

r = picam2.switch_mode_capture_request_and_stop(capture_config)
jpeg_filename = generate_unique_filename("jpg")  ### Save as JPG
r.save("main", (os.path.join(directory, jpeg_filename)))
dng_filename = generate_unique_filename("dng")  ## Save as DNG
r.save_dng((os.path.join(directory, dng_filename)))
