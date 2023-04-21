import subprocess
import cv2
import configparser

# Read configuration from configuration.ini file
config = configparser.ConfigParser()
config.read('configuration.ini')
stream_url = config.get('RTSP', 'stream_url')
scale_width = config.getint('RTSP', 'scale_width')
scale_height = config.getint('RTSP', 'scale_height')
conky_window_name = config.get('Conky', 'conky_window_name')
update_interval = config.getint('Conky', 'update_interval')

# Command to stream video and convert to PNG
command = f"ffmpeg -rtsp_transport tcp -i {stream_url} -f image2 -vcodec png - | convert -scale {scale_width}x{scale_height} - -"

# Start the subprocess and capture its output
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# Initialize OpenCV window
cv2.namedWindow(conky_window_name)

# Continuously read the output from the subprocess and display it in the OpenCV window
while True:
    # Read the output from the subprocess
    output = process.stdout.read(scale_width*scale_height*3)

    # Convert the output to a NumPy array and reshape it to the correct dimensions
    image = cv2.imdecode(np.frombuffer(output, dtype='uint8'), cv2.IMREAD_COLOR).reshape(scale_height, scale_width, 3)

    # Display the image in the OpenCV window
    cv2.imshow(conky_window_name, image)

    # Wait for a key press and exit if the 'q' key is pressed
    if cv2.waitKey(update_interval) & 0xFF == ord('q'):
        break

# Clean up the subprocess and OpenCV window
process.kill()
cv2.destroyAllWindows()
