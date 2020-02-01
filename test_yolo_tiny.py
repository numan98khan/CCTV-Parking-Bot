# wget https://pjreddie.com/media/files/yolov3.weights
# python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
# python yolo_video.py [OPTIONS...] --image, for image detection mode, OR
# python yolo_video.py [--input video_path] [output_path (optional)]

import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image

detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)