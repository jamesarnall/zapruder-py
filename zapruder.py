from moviepy.editor import *

frame_dir  = 'frames/'
frame_rate = 18.3

frame_set = []


def makeFileName(num):
	if (num < 10): return 'z00' + str(num) + '.jpg'
	if (num < 100): return 'z0' + str(num) + '.jpg'
	return 'z' + str(num) + '.jpg'

for x in range(1,487):
	print(frame_dir + makeFileName(x))
	frame_set.append(ImageClip(frame_dir + makeFileName(x)).set_duration(1/frame_rate))

video_clip = concatenate_videoclips(frame_set)

video_clip.write_videofile("zapruder.mp4", fps=frame_rate)