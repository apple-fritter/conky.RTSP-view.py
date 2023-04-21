import subprocess
import cv2

# Command to stream video and convert to PNG
command = "ffmpeg -rtsp_transport tcp -i rtsp://username:password@your-stream-address -f image2 -vcodec png - | convert -scale 400x300 - -"

# Start the subprocess and capture its output
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# Initialize OpenCV window
cv2.namedWindow("Video Stream")

# Continuously read the output from the subprocess and display it in the OpenCV window
while True:
    # Read the output from the subprocess
    output = process.stdout.read(400*300*3)

    # Convert the output to a NumPy array and reshape it to the correct dimensions
    image = cv2.imdecode(np.frombuffer(output, dtype='uint8'), cv2.IMREAD_COLOR).reshape(300, 400, 3)

    # Display the image in the OpenCV window
    cv2.imshow("Video Stream", image)

    # Wait for a key press and exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up the subprocess and OpenCV window
process.kill()
cv2.destroyAllWindows()
