#!/usr/bin/env python

import os
import sys
from pprint import pprint
import wit
from StringIO import StringIO

def readYaml(self,fname):
		f = open( fname )
		dict = yaml.safe_load(f)
		f.close()
		
		return dict

self.info = self.readYaml('/Users/kevin/Dropbox/accounts.yaml')
wit_token = self.info['WIT_TOKEN']


try:
    import pyaudio
except ImportError:
    print('Error: Make sure you install PyAudio before running this example.')
    sys.exit()

try:
    import wit
except ImportError:
    # Wit isn't installed, so we'll add the parent directory to the system
    # path and try again
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.append(path)
    import wit

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 3
# Change this based on your OSes settings. This should work for OSX, though.
ENDIAN = 'little'
CONTENT_TYPE = \
    'raw;encoding=signed-integer;bits=16;rate={0};endian={1}'.format(
        RATE, ENDIAN)


def record_and_stream():
    p = pyaudio.PyAudio()

    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE,
        input=True, frames_per_buffer=CHUNK)

    print("* recording and streaming")

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        yield stream.read(CHUNK)

    print("* done recording and streaming")

    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == '__main__':
    output_file = StringIO()

    w = wit.Wit(wit_token)
    result = w.post_speech(record_and_stream(), content_type=CONTENT_TYPE)
    pprint(result)