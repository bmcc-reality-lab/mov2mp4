import os
import moviepy.editor as mp
from pathlib import Path
from glob import glob
from argparse import ArgumentParser


def mov2mp4(input_path: Path, output_path: Path) -> None:
    # Get video
    clip = mp.VideoFileClip(input_path)

    # Resize video as MoviePy reads aspect ratio incorrectly
    clip = clip.resize((clip.size[1], clip.size[0]))

    # Write to MP4
    clip.rewrite_videofile(
        output_path,
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='temp-audio.m4a',
        audio=True,
        verbose=False,
        logger=None
    )
    clip.close()

if __name__ == '__main__':
    output_dir = './output/'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        
    paths = glob('./input/*')
    for path in paths:
        input_path = Path(path)
        output_path = Path(output_dir + input_path.stem + '.mp4')
        mov2mp4(input_path, output_path)