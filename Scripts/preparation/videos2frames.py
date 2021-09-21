import argparse
import cv2
from glob import glob
from tqdm import tqdm

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract frames from videos')
    parser.add_argument('--videos_directory', type=str)
    parser.add_argument('--output_directory', type=str)
    config = parser.parse_args()

    vid_directory = config.videos_directory

    for file in tqdm(glob(vid_directory + '/*.MP4')):
        vidObj = cv2.VideoCapture(file)

        count = 0
        success, image = vidObj.read()
        while success:
            resized_down = cv2.resize(image, (416, 234), interpolation= cv2.INTER_LINEAR)
            cv2.imwrite(config.output_directory + '/' + file[-29:-4] + '/Annotations/frame_{0:06d}.JPG'.format(count), resized_down)
            count += 1
            success, image = vidObj.read()
