# Video Streaming in Conky with FFMPEG
This project demonstrates how to stream video from an `RTSP` source and display it in a `Conky` window using `FFMPEG` and `OpenCV`.

## Requirements
```
Python 3.6+
Conky 1.10+
FFMPEG 3.0+
OpenCV 3.0+
```

## Installation
Install the required software:

```bash
sudo apt-get install python3 conky ffmpeg libopencv-dev
```
#### Clone this repository:
```bash
git clone https://github.com/username/repo.git
```

Edit the config.ini file with your RTSP stream credentials and settings.

#### Run the stream.py script:

```bash
python3 stream.py
```

#### Launch Conky with the provided conkyrc configuration file:

```bash
conky -c conkyrc
```

> The video stream should now be displayed in the Conky window.

## Configuration
The config.ini file contains the following settings:

`stream_address`: The RTSP stream address.
`username`: The username for accessing the RTSP stream.
`password`: The password for accessing the RTSP stream.
`width`: The width of the video stream.
`height`: The height of the video stream.
`scale`: The scaling factor for the video stream.

## Acknowledgements:
This project was heavily inspired by [this Stack Overflow post](https://stackoverflow.com/questions/42166489/day-of-the-week-in-feb-2017/42166510#42166510).

## License

These files released under the [MIT License](LICENSE).
