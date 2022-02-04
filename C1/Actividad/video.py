import os
import moviepy.video.io.ImageSequenceClip
from time import sleep
import glob

def create_video():
    image_folder='imagenes'
    fps=12
    image_files = [os.path.join(image_folder,img)
                for img in os.listdir(image_folder)
                if img.endswith(".png")]
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile('my_video.mp4')
    sleep(2)
    files = glob.glob('imagenes/*')
    for f in files:
        os.remove(f)


if __name__ == '__main__':
    image_folder='imagenes'
    for img in os.listdir(image_folder):
        print(img)