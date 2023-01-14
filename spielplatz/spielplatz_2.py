import re
from xml.sax import make_parser, handler
import os
from sys import argv
from shlex import quote
import json

with open("crimson_tide_-_in_tiefster_gefahr_(1995).250001.json", "r") as f:
    data = json.load(f)

video_list = []
audio_list = []

for stream in data['streams']:
    if stream["codec_type"] == "video":
        for key, value in stream.items():
            pass
            # videostream = VideoStream()
        # video_list.append(videostream)

    elif stream["codec_type"] == "audio":
        pass
        # print(stream)
        # for key, value in stream.items():
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
