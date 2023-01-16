class CurrentJob:
    def __init__(self, job_id):
        self.__job_id = job_id
        self.__full_file_name = None
        self.__v_encoder = None
        self.__v_preset = None
        self.__v_filter = None
        self.__v_qcontrol = None
        self.__v_crop = {}
        self.__a_encoder = None
        self.__a_qcontrol = None
        self.__ff_parameter = None
        self.__cut_parts = []
        self.__i_film_name = None
        self.__i_extension = None
        self.__o_scale_size = None
        self.__o_pix_fmt = None
        self.__o_fps = None
        self.__o_film_name = None
        self.__o_extension = None
        self.__video_list = []
        self.__audio_list = []

    def get_audio_list(self):
        return self.__audio_list

    def set_audio_list(self, audio_list):
        if isinstance(audio_list, list):
            self.__audio_list = audio_list
            return True
        return False

    def get_scale_size(self):
        return self.__o_scale_size

    def set_scale_size(self, string):
        if isinstance(string, str):
            self.__o_scale_size = string
            return True
        return False

    def get_crop(self):
        return self.__v_crop

    def set_crop(self, string):
        if isinstance(string, str):
            self.__v_crop = string
            return True
        return False

    def get_video_list(self):
        return self.__video_list

    def set_video_list(self, video_list):
        if isinstance(video_list, list):
            self.__video_list = video_list
            return True
        return False

    def get_audio_list(self):
        return self.__audio_list

    def set_audio_list(self, audio_list):
        if isinstance(audio_list, list):
            self.__audio_list = audio_list
            return True
        return False

    def get_input_fps(self):
        return self.__i_fps

    def get_full_file_name(self):
        return self.__full_file_name

    def set_full_file_name(self, string):
        if isinstance(string, str):
            self.__full_file_name = string
            return True
        return False

    def get_input_pix_fmt(self):
        return self.__i_pix_fmt

    def get_cut_parts(self):
        return self.__cut_parts

    def set_cut_parts(self, liste):
        if isinstance(liste, list):
            self.__cut_parts = liste
            return True
        return False

    def get_job_id(self):
        return int(self.__job_id)

    def get_v_qcontrol(self):
        return self.__v_qcontrol

    def set_v_qcontrol(self, string):
        if isinstance(string, str):
            self.__v_qcontrol = string
            return True
        return False

    def get_v_encoder(self):
        return self.__v_encoder

    def set_v_encoder(self, string):
        if isinstance(string, str):
            self.__v_encoder = string
            return True
        return False

    def get_v_preset(self):
        return self.__v_encoder

    def set_v_preset(self, string):
        if isinstance(string, str):
            self.__v_preset = string
            return True
        return False

    def get_v_filter(self):
        return self.__v_filter

    def set_v_filter(self, string):
        if isinstance(string, str):
            self.__v_filter = string
            return True
        return False

    def get_a_encoder(self):
        return self.__a_encoder

    def set_a_encoder(self, string):
        if isinstance(string, str):
            self.__a_encoder = string
            return True
        return False

    def get_input_film_name(self):
        return self.__i_film_name

    def set_input_film_name(self, string):
        if isinstance(string, str):
            self.__i_film_name = string
            self.__o_film_name = self.__i_film_name.lower().replace(" ", "")
            return True
        return False

    def get_output_film_name(self):
        return self.__o_film_name

    def get_ff_parameter(self):
        return self.__ff_parameter

    def set_ff_parameter(self, string):
        if isinstance(string, str) and \
           len(string) == 6:
            self.__ff_parameter = string
            return True
        return False

    def get_input_extension(self):
        return self.__i_extension

    def set_input_extension(self, string):
        if isinstance(string, str):
            self.__i_extension = string

    def get_output_extension(self):
        return self.__o_extension

    def set_output_extension(self, string):
        if isinstance(string, str):
            self.__o_extension = string
            return True
        return False

    def show(self):
        print("\tJob ID:\t\t\t\t->", self.__job_id)
        print("\tVollständiger Dateiname:\t->", self.__full_file_name)
        print("\tVideo-Encoder:\t\t\t->", self.__v_encoder)
        print("\tVideo-Encoder Komprimierung\t->", self.__v_preset)
        print("\tVideo Filter\t\t\t->", self.__v_filter)
        print("\tVideo-Encoder Qualität:\t\t->", self.__v_qcontrol)
        print("\tVideo Ränder:\t\t\t->", self.__v_crop)
        print("\tAudio-Encoder:\t\t\t->", self.__a_encoder)
        print("\tAudio-Encoder Qualität:\t\t->", self.__a_qcontrol)
        print("\tSchnitt Liste:\t\t\t->", self.__cut_parts)
        print("\tFFMPEG Film Parameter:\t\t->", self.__ff_parameter)
        print("\tAktueller Film Name:\t\t->", self.__i_film_name)
        print("\tEingangs Dateierweiterung:\t->", self.__i_extension)
        print("\tAusgangs Auflösung:\t\t->", self.__o_scale_size)
        print("\tAusgangs Pixelformat:\t\t->", self.__o_pix_fmt)
        print("\tAusgangs Bildrate:\t\t->", self.__o_fps)
        print("\tAusgangs Film Name:\t\t->", self.__o_film_name)
        print("\tAusgangs Dateierweiterung:\t->", self.__o_extension)
