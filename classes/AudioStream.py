class AudioStream:
    def __init__(self):

        self.__index = None
        self.__codec_name = None
        self.__codec_long_name = None
        self.__codec_type = None
        self.__codec_time_base = None
        self.__codec_tag_string = None
        self.__codec_tag = None
        self.__sample_fmt = None
        self.__sample_rate = None
        self.__channels = None
        self.__channel_layout = None
        self.__bits_per_sample = None
        self.__dmix_mode = None
        self.__ltrt_cmixlev = None
        self.__ltrt_surmixlev = None
        self.__loro_cmixlev = None
        self.__loro_surmixlev = None
        self.__id = None
        self.__r_frame_rate = None
        self.__avg_frame_rate = None
        self.__time_base = None
        self.__start_pts = None
        self.__start_time = None
        self.__duration_ts = None
        self.__duration = None
        self.__bit_rate = None
        self.__disposition = None
        self.__tags = None

    def get_index(self):
        return self.__index

    def set_index(self, integer):
        if isinstance(integer, bool):
            self.__index = integer
            return True
        return False

    def get_codec_name(self):
        return self.__codec_name

    def set_codec_name(self, string):
        if isinstance(string, str):
            self.__codec_name = string
            return True
        return False

    def get_codec_long_name(self):
        return self.__codec_long_name

    def set_codec_long_name(self, string):
        if isinstance(string, str):
            self.__codec_long_name = string
            return True
        return False

    def get_codec_type(self):
        return self.__codec_type

    def set_codec_type(self, string):
        if isinstance(string, str):
            self.__codec_type = string
            return True
        return False

    def get_codec_time_base(self):
        return self.__codec_time_base

    def set_codec_time_base(self, string):
        if isinstance(string, str):
            self.__codec_time_base = string
            return True
        return False

    def get_codec_tag_string(self):
        return self.__codec_tag_string

    def set_codec_tag_string(self, string):
        if isinstance(string, str):
            self.__codec_tag_string = string
            return True
        return False

    def get_codec_tag(self):
        return self.__codec_tag

    def set_codec_tag(self, string):
        if isinstance(string, str):
            self.__codec_tag = string
            return True
        return False

    def get_sample_fmt(self):
        return self.__sample_fmt

    def set_sample_fmt(self, string):
        if isinstance(string, str):
            self.__sample_fmt = string
            return True
        return False

    def get_sample_rate(self):
        return self.__sample_rate

    def set_sample_rate(self, string):
        if isinstance(string, str):
            self.__sample_rate = string
            return True
        return False

    def get_channels(self):
        return self.__channels

    def set_channels(self, integer):
        if isinstance(integer, int):
            self.__channels = integer
            return True
        return False

    def get_channel_layout(self):
        return self.__channel_layout

    def set_channel_layout(self, string):
        if isinstance(string, str):
            self.__channel_layout = string
            return True
        return False

    def get_bits_per_sample(self):
        return self.__bits_per_sample

    def set_bits_per_sample(self, integer):
        if isinstance(integer, int):
            self.__bits_per_sample = integer
            return True
        return False

    def get_dmix_mode(self):
        return self.__dmix_mode

    def set_dmix_mode(self, string):
        if isinstance(string, str):
            self.__dmix_mode = string
            return True
        return False

    def get_ltrt_cmixlev(self):
        return self.__ltrt_cmixlev

    def set_ltrt_cmixlev(self, string):
        if isinstance(string, str):
            self.__ltrt_cmixlev = string
            return True
        return False

    def get_ltrt_surmixlev(self):
        return self.__ltrt_surmixlev

    def set_ltrt_surmixlev(self, string):
        if isinstance(string, str):
            self.__ltrt_surmixlev = string
            return True
        return False

    def get_loro_cmixlev(self):
        return self.__loro_cmixlev

    def set_loro_cmixlev(self, string):
        if isinstance(string, str):
            self.__loro_cmixlev = string
            return True
        return False

