import xml.sax


class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.__v_index = None
        self.__v_codec_name = None
        self.__v_codec_long_name = None
        self.__v_profile = None
        self.__v_codec_type = None
        self.__v_width = None
        self.__v_height = None
        self.__v_sample_aspect_ratio = None
        self.__v_display_aspect_ratio = None
        self.__v_pix_fmt = None
        self.__v_field_order = None
        self.__v_frame_rate = None
        self.__a_index = None
        self.__a_codec_name = None
        self.__a_codec_long_name = None
        self.__a_codec_type = None
        self.__a_sample_fmt = None
        self.__a_sample_rate = None
        self.__a_channels = None
        self.__a_channel_layout = None

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "stream" and attributes["codec_type"] == "video":
            self.__v_index = attributes["index"]
            self.__v_codec_name = attributes["codec_name"]
            self.__v_codec_long_name = attributes["codec_long_name"]
            self.__v_profile = attributes["profile"]
            self.__v_codec_type = attributes["codec_type"]
            self.__v_width = attributes["width"]
            self.__v_height = attributes["height"]
            self.__v_sample_aspect_ratio = attributes["sample_aspect_ratio"]
            self.__v_display_aspect_ratio = attributes["display_aspect_ratio"]
            self.__v_pix_fmt = attributes["pix_fmt"]
            try:
                self.__v_field_order = attributes["field_order"]
            except KeyError:
                self.__v_field_order = None
            self.__v_frame_rate = attributes["r_frame_rate"]

        if tag == "stream" and attributes["codec_type"] == "audio":
            self.__a_index = attributes["index"]
            self.__a_codec_name = attributes["codec_name"]
            self.__a_codec_long_name = attributes["codec_long_name"]
            self.__a_codec_type = attributes["codec_type"]
            self.__a_sample_fmt = attributes["sample_fmt"]
            self.__a_sample_rate = attributes["sample_rate"]
            self.__a_channels = attributes["channels"]
            self.__a_channel_layout = attributes["channel_layout"]

    def get_v_index(self):
        return self.__v_index

    def get_a_index(self):
        return self.__a_index

    def get_v_codec_name(self):
        return self.__v_codec_name

    def get_v_codec_long_name(self):
        return self.__v_codec_long_name

    def get_v_profile(self):
        return self.__v_profile

    def get_v_width(self):
        return self.__v_width

    def get_v_height(self):
        return self.__v_height

    def get_v_sample_aspect_ratio(self):
        return self.__v_sample_aspect_ratio

    def get_v_display_aspect_ratio(self):
        return self.__v_display_aspect_ratio

    def get_v_pix_fmt(self):
        return self.__v_pix_fmt

    def get_v_field_order(self):
        return self.__v_field_order

    def get_v_frame_rate(self):
        return self.__v_frame_rate

    def show(self):
        print("\t\tVideo Index:\t\t\t->", self.__v_index)
        print("\t\tCodec Name:\t\t\t->", self.__v_codec_name)
        print("\t\tVoller Codec Name:\t\t->", self.__v_codec_long_name)
        print("\t\tCodec Profil:\t\t\t->", self.__v_profile)
        print("\t\tVideo Breite:\t\t\t->", self.__v_width)
        print("\t\tVideo Höhe:\t\t\t->", self.__v_height)
        print("\t\tVideo SAR:\t\t\t->", self.__v_sample_aspect_ratio)
        print("\t\tVideo DAR:\t\t\t->", self.__v_display_aspect_ratio)
        print("\t\tPixelformat:\t\t\t->", self.__v_pix_fmt)
        print("\t\tHalbbild-Darstellung\t\t->", self.__v_field_order)
        print("\t\tBildrate:\t\t\t->", self.__v_frame_rate)
        print("\t\tAudio Index:\t\t\t->", self.__a_index)
        print("\t\tCodec Name:\t\t\t->", self.__a_codec_name)
        print("\t\tVoller Codec Name:\t\t->", self.__a_codec_long_name)
        print("\t\tSample-Genauigkeit:\t\t->", self.__a_sample_fmt)
        print("\t\tSample Rate:\t\t\t->", self.__a_sample_rate)
        print("\t\tAudio Kanäle:\t\t\t->", self.__a_channels)
        print("\t\tAudio Layout:\t\t\t->", self.__a_channel_layout)
