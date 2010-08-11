ffmpeg -i %03d.jpg -acodec null -f avi -vcodec mpeg4 -b 800k -g 300 -bf 2 moo.avi
