#!/bin/sh

HB="/usr/local/bin/HandBrakeCLI"
INPUT=$1
OUTPUT=$2

FILE="-f av_mp4"
VIDEO="-e x264 -q 19 --cfr"
AUDIO="-a 1 --audio-copy-mask ac3"

$HB -i "$INPUT" -o "$OUTPUT" $VIDEO $AUDIO
