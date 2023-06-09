# RTSP in Conky with FFMPEG
This project demonstrates how to stream video from an `RTSP` source and display it in a `Conky` window using `FFMPEG` and `OpenCV`.

## Requirements
```
Python 3.6+
Conky 1.10+
FFMPEG 3.0+
OpenCV 3.0+
```

---

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

---

## Configuration
The configuration.ini file contains the following settings:

`stream_address`: The RTSP stream address.
`username`: The username for accessing the RTSP stream.
`password`: The password for accessing the RTSP stream.
`width`: The width of the video stream.
`height`: The height of the video stream.
`scale`: The scaling factor for the video stream.

### example `configuration.ini`

```
[RTSP]
stream_url = rtsp://username:password@your-stream-address
scale_width = 400
scale_height = 300

[Conky]
conky_window_name = Video Stream
update_interval = 5
```

The RTSP section includes the URL of the RTSP stream, as well as the desired `width` and `height` of the scaled video frames. The Conky section includes the `name` of the Conky window that will display the video stream, as well as the `update interval` (in seconds) for refreshing the video stream in the Conky window.

You can adjust the values in this file to match your specific needs and preferences.

---

## Acknowledgements:
This project was heavily inspired by a 404'ed [Stack Overflow](https://stackoverflow.com/) post.

---

## 🤪 Conky Meta

- [888v](https://github.com/apple-fritter/888v): Virtual webcam clone with Conky overlay; Bash.
- [.conkyrc](https://github.com/apple-fritter/.conkyrc): conky configuration file.
- [moonphase.py](https://github.com/apple-fritter/conky.moonphase.py): RSS reader for Conky that reads in a TSV based list of feeds. Python.
- [RTSP-view.py](https://github.com/apple-fritter/conky.RTSP-view.py): Script that displays an RTSP stream. Python.
- [tide.py](https://github.com/apple-fritter/conky.tide.py): Script that displays the local tide using the Tidal API. Python.
- [twitter.py](https://github.com/apple-fritter/conky.twitter.py): Script that displays a user's Twitter notifications. Python.

---

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

---

## License

These files released under the [MIT License](LICENSE).
