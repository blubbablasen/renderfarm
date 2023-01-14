import re
from xml.sax import make_parser, handler
import os
from sys import argv
from shlex import quote
import json


class AudioStream:
    def __init__(self, index, codec_name, codec_long_name, codec_type, codec_time_base, codec_tag_string, codec_tag, sample_fmt, sample_rate, channels,
        channel_layout, bits_per_sample, dmix_mode, ltrt_cmixlev, ltrt_surmixlev, loro_cmixlev, loro_surmixlev, id, r_frame_rate, avg_frame_rate, time_base,
        start_pts, start_time, duration_ts, duration, bit_rate, disposition, tags):

        self.__index = index
        self.__codec_name = codec_name
        self.__codec_long_name = codec_long_name
        self.__codec_type = codec_type
        self.__codec_time_base = codec_time_base
        self.__codec_tag_string = codec_tag_string
        self.__codec_tag = codec_tag
        self.__sample_fmt = sample_fmt
        self.__sample_rate = sample_rate
        self.__channels = channels
        self.__channel_layout = channel_layout
        self.__bits_per_sample = bits_per_sample
        self.__dmix_mode = dmix_mode
        self.__ltrt_cmixlev = ltrt_cmixlev
        self.__ltrt_surmixlev = ltrt_surmixlev
        self.__loro_cmixlev = loro_cmixlev
        self.__loro_surmixlev = loro_surmixlev
        self.__id = id
        self.__r_frame_rate = r_frame_rate
        self.__avg_frame_rate = avg_frame_rate
        self.__time_base = time_base
        self.__start_pts = start_pts
        self.__start_time = start_time
        self.__duration_ts = duration_ts
        self.__duration = duration
        self.__bit_rate = bit_rate
        self.__disposition = disposition
        self.__tags = tags


with open("crimson_tide_-_in_tiefster_gefahr_(1995).250001.json", "r") as f:
    data = json.load(f)

video_list = []
audio_list = []

for stream in data['streams']:
    if stream["codec_type"] == "video":
        for key, value in stream.items():
            
        #videostream = VideoStream()
        #video_list.append(videostream)

    elif stream["codec_type"] == "audio":
        pass
        #print(stream)
        #for key, value in stream.items():
        #    print(key, value)
        #    audiostream = AudioStream()
        #    audio_list.append(audiostream)
 
'''
def parse_ffmpeg_cfg():
    cut_list = {}
    with open("the_imitation_game_-_ein_streng_geheimes_leben_(2014).250100.mlt", "r") as file:
        for line in file.readlines():
            if line.strip()[0:18] == '<entry producer="c':
                cut_list.update({re.findall("[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}", line)[0]:re.findall("[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}", line)[1]})
    print(cut_list)
parse_ffmpeg_cfg()
'''

'''
class xml_parse(handler.ContentHandler):
    def startElement(self, name, attrs):
        print(name, attrs["in"])



parser = make_parser()	#erzeugt ein Parser-Objekt.

xml = xml_parse()	#erzeugt das Objekt

parser.setContentHandler(xml)	#übergibt der Methode setContentHandler() das xml Objekt

parser.parse("the_imitation_game_-_ein_streng_geheimes_leben_(2014).250100.mlt") #dem Parser das XML-Dokument übergeben.
'''
'''
import xml.sax
class Streams(xml.sax.ContentHandler):
    def __init__(self):
        self.__count = 0

   # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "steam"
                #cut_in = attributes["in"]
                #cut_out = attributes["out"]
                #self.__cut_list.update({cut_in:cut_out})

    #def get_cut_list(self):
        #return self.__cut_list

# create an XMLReader
parser = xml.sax.make_parser()

# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# override the default ContextHandler
Handler = XMLHandler()
parser.setContentHandler(Handler)
parser.parse("the_imitation_game_-_ein_streng_geheimes_leben_(2014).250100.mlt")
print(Handler.get_cut_list())
'''
'''
def grep_file_information():
    file = quote("the_imitation_game_-_ein_streng_geheimes_leben_(2014).250100.mov")
    blubb = os.system("ffprobe "+file)
    print(blubb)
    
grep_file_information()
'''
'''
with open("crimson_tide_-_in_tiefster_gefahr_(1995).250001.xml", "r") as f:
    count = 0
    for line in f.readlines():
        if len(re.findall('^\ +<stream.*codec_type=\"(video|audio)\"', line)) > 0:
            count += 1
    print(count)
'''