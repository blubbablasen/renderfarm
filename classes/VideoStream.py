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

    def get_sample_aspect_ratio(self):
        return self.__sample_aspect_ratio

    def set_sample_aspect_ratio(self, string):
        if isinstance(string, str):
            self.__sample_aspect_ratio = string
            return True
        return False

    def get_display_aspect_ratio(self):
        return self.__display_aspect_ratio

    def set_display_aspect_ratio(self, string):
        if isinstance(string, str):
            self.__display_aspect_ratio = string
            return True
        return False

    def get_pix_fmt(self):
        return self.__pix_fmt

    def set_pix_fmt(self, string):
        if isinstance(string, str):
            self.__pix_fmt = string
            return True
        return False

    def get_level(self):
        return self.__level

    def set_level(self, integer):
        if isinstance(integer, int):
            self.__level = integer
            return True
        return False

    def get_color_range(self):
        return self.__color_range

    def set_color_range(self, string):
        if isinstance(string, str):
            self.__color_range = string
            return True
        return False

    def get_color_space(self):
        return self.__color_space

    def set_color_space(self, string):
        if isinstance(string, str):
            self.__color_space = string
            return True
        return False

    def get_color_transfer(self):
        return self.__color_transfer

    def set_color_transfer(self, string):
        if isinstance(string, str):
            self.__color_transfer = string
            return True
        return False

    def get_color_primaries(self):
        return self.__color_primaries

    def set_color_primaries(self, string):
        if isinstance(string, str):
            self.__color_primaries = string
            return True
        return False

    def get_chroma_location(self):
        return self.__chroma_location

    def set_chroma_location(self, string):
        if isinstance(string, str):
            self.__chroma_location = string
            return True
        return False

    def get_field_order(self):
        return self.__field_order

    def set_field_order(self, string):
        if isinstance(string, str):
            self.__field_order = string
            return True
        return False

    def get_refs(self):
        return self.__refs

    def set_refs(self, integer):
        if isinstance(integer, int):
            self.__refs = integer
            return True
        return False

    def get_is_avc(self):
        return self.__is_avc

    def set_is_avc(self, string):
        if isinstance(string, str):
            self.__is_avc = string
            return True
        return False

    def get_nal_length_size(self):
        return self.__nal_length_size

    def set_nal_length_size(self, string):
        if isinstance(string, str):
            self.__nal_length_size = string
            return True
        return False

    def get_id(self):
        return self.__id

    def set_id(self, string):
        if isinstance(string, str):
            self.__id = string
            return True
        return False

    def get_r_frame_rate(self):
        return self.__r_frame_rate

    def set_r_frame_rate(self, string):
        if isinstance(string, str):
            self.__r_frame_rate = string
            return True
        return False

    def get_avg_frame_rate(self):
        return self.__avg_frame_rate

    def set_avg_frame_rate(self, string):
        if isinstance(string, str):
            self.__avg_frame_rate = string
            return True
        return False

    def get_time_base(self):
        return self.__time_base

    def set_time_base(self, string):
        if isinstance(string, str):
            self.__time_base = string
            return True
        return False

    def get_start_pts(self):
        return self.__start_pts

    def set_start_pts(self, integer):
        if isinstance(integer, int):
            self.__start_pts = integer
            return True
        return False

    def get_start_time(self):
        return self.__start_time

    def set_start_time(self, string):
        if isinstance(string, str):
            self.__start_time = string
            return True
        return False

    def get_duration_ts(self):
        return self.__duration_ts

    def set_duration_ts(self, integer):
        if isinstance(integer, int):
            self.__duration_ts = integer
            return True
        return False

    def get_duration(self):
        return self.__duration

    def set_duration(self, string):
        if isinstance(string, str):
            self.__duration = string
            return True
        return False

    def get_bits_per_raw_sample(self):
        return self.__bits_per_raw_sample

    def set_bits_per_raw_sample(self, string):
        if isinstance(string, str):
            self.__bits_per_raw_sample = string
            return True
        return False

    def get_disposition(self):
        return self.__disposition

    def set_disposition(self, dictionary):
        if isinstance(dictionary, dict):
            self.__disposition = dictionary
            return True
        return False

    def show(self):
        print("\t\tStream Index:\t\t", self.__index)
        print("\t\tCodec Name:\t\t", self.__codec_name)
        print("\t\tCodec Long Name:\t", self.__codec_long_name)
        print("\t\tProfile:\t\t", self.__profile)
        print("\t\tCodec Type:\t\t", self.__codec_type)
        print("\t\tCodec Time Base:\t", self.__codec_time_base)
        print("\t\tCodec Tag String:\t", self.__codec_tag_string)
        print("\t\tCodec Tag:\t\t", self.__codec_tag)
        print("\t\tWidth:\t\t\t", self.__width)
        print("\t\tHeight:\t\t\t", self.__height)
        print("\t\tCoded Width:\t\t", self.__coded_width)
        print("\t\tCoded Height:\t\t", self.__coded_height)
        print("\t\tClosed Captions:\t", self.__closed_captions)
        print("\t\tHas B Frames:\t\t", self.__has_b_frames)
        print("\t\tSample Aspect Ratio:\t", self.__sample_aspect_ratio)
        print("\t\tDisplay Aspect Ratio:\t", self.__display_aspect_ratio)
        print("\t\tPix Fmt:\t\t", self.__pix_fmt)
        print("\t\tLevel:\t\t\t", self.__level)
        print("\t\tColor Range:\t\t", self.__color_range)
        print("\t\tColor Space:\t\t", self.__color_space)
        print("\t\tColor Transfer:\t\t", self.__color_transfer)
        print("\t\tColor Primaries:\t", self.__color_primaries)
        print("\t\tChroma Location:\t", self.__chroma_location)
        print("\t\tField Order:\t\t", self.__field_order)
        print("\t\tRefs:\t\t\t", self.__refs)
        print("\t\tIs AVC:\t\t\t", self.__is_avc)
        print("\t\tNal Length Size:\t", self.__nal_length_size)
        print("\t\tID:\t\t\t", self.__id)
        print("\t\tR Frame Rate:\t\t", self.__r_frame_rate)
        print("\t\tAVG Frame Rate:\t\t", self.__avg_frame_rate)
        print("\t\tTime Base:\t\t", self.__time_base)
        print("\t\tStart PTS:\t\t", self.__start_pts)
        print("\t\tStart Time:\t\t", self.__start_time)
        print("\t\tDuration TS:\t\t", self.__duration_ts)
        print("\t\tDuration:\t\t", self.__duration)
        print("\t\tBits Per Raw Sample:\t", self.__bits_per_raw_sample)
        print("\t\tDisposition:\t\t", self.__disposition)
