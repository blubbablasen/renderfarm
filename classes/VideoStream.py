class VideoStream:
    def __init__(self):

        self.__index = None
        self.__codec_name = None
        self.__codec_long_name = None
        self.__profile = None
        self.__codec_type = None
        self.__codec_time_base = None
        self.__codec_tag_string = None
        self.__codec_tag = None
        self.__width = None
        self.__height = None
        self.__coded_width = None
        self.__coded_height = None
        self.__closed_captions = None
        self.__has_b_frames = None
        self.__sample_aspect_ratio = None
        self.__display_aspect_ratio = None
        self.__pix_fmt = None
        self.__level = None
        self.__color_range = None
        self.__color_space = None
        self.__color_transfer = None
        self.__color_primaries = None
        self.__chroma_location = None
        self.__field_order = None
        self.__refs = None
        self.__is_avc = None
        self.__nal_length_size = None
        self.__id = None
        self.__r_frame_rate = None
        self.__avg_frame_rate = None
        self.__time_base = None
        self.__start_pts = None
        self.__start_time = None
        self.__duration_ts = None
        self.__duration = None
        self.__bits_per_raw_sample = None
        self.__disposition = {}

    def get_index(self):
        return self.__index

    def set_index(self, integer):
        if isinstance(integer, int):
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

    def get_profile(self):
        return self.__profile

    def set_profile(self, string):
        if isinstance(string, str):
            self.__profile = string
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

    def get_width(self):
        return self.__width

    def set_width(self, integer):
        if isinstance(integer, int):
            self.__width = integer
            return True
        return False

    def get_height(self):
        return self.__height

    def set_height(self, integer):
        if isinstance(integer, int):
            self.__height = integer
            return True
        return False

    def get_coded_width(self):
        return self.__coded_width

    def set_coded_width(self, integer):
        if isinstance(integer, int):
            self.__coded_width = integer
            return True
        return False

    def get_coded_height(self):
        return self.__coded_height

    def set_coded_height(self, integer):
        if isinstance(integer, int):
            self.__coded_height = integer
            return True
        return False

    def get_closed_captions(self):
        return self.__closed_captions

    def set_closed_captions(self, integer):
        if isinstance(integer, int):
            self.__closed_captions = integer
            return True
        return False

    def get_has_b_frames(self):
        return self.__has_b_frames

    def set_has_b_frames(self, integer):
        if isinstance(integer, int):
            self.__has_b_frames = integer
            return True
        return False

