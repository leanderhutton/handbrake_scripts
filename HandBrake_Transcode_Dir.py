#!/usr/bin/env python

import os,sys,subprocess

handbrake = "/usr/local/bin/HandBrakeCLI"
fileopts = "-f av_mp4"
videoopts = "-e x264 -q 19 --cfr --x264-preset medium"
audioopts = "-a 1 --audio-copy-mask ac3"

def usage():
	print ("Usage: Handbrake_Transcode_Dir.py \"source_directory\" \"destination_directory\"")



def main():
	if len(sys.argv) == 1:
		print "Not enough arguments"
		usage()
		exit(2)
	if len(sys.argv) > 3:
		print "Too many arguments"
		usage()
		exit(2)
	else:
		source = sys.argv[1]
		dest = sys.argv[2]
		for file in os.listdir(source):
			sourcefile = "\"" + source + "/" + file + "\""
			filename = os.path.splitext(file)[0]
			destfile = "\"" + dest + "/" + filename + ".mp4" + "\""
			cmd = handbrake + " -i " + sourcefile + " -o " + " " + destfile + " " + fileopts + " " + videoopts + " " + audioopts
			subprocess.call(cmd, shell=True) 

if __name__ == "__main__":
	main()
