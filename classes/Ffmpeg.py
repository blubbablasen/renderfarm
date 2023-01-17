class Ffmpeg:
    def __init__(self):
        self.__edit_list = []
        self.__xml_list = []
        self.__total = 0
        self.__v_encoders = []
        self.__v_presets = []
        self.__v_filters = []
        self.__v_qcontrols = []
        self.__a_encoders = []
        self.__a_filters = []
        self.__avail_extension = []

    def get_xml_list(self):
        return self.__xml_list

    def set_xml_list(self, xml_list):
        if isinstance(xml_list, list) and len(xml_list) >= 1:
            self.__xml_list = xml_list
            return True
        return False

    def get_edit_list(self):
        return self.__edit_list

    def set_edit_list(self, edit_list):
        if isinstance(edit_list, list) and len(edit_list) >= 1:
            self.__edit_list = edit_list
            self.__total = len(edit_list)
            return True
        return False

    def get_v_qcontrols(self):
        return self.__v_qcontrols

    def set_v_qcontrols(self, liste):
        if isinstance(liste, list):
            self.__v_qcontrols = liste
            return True
        return False

    def get_total(self):
        return int(self.__total)

    def get_v_encoders(self):
        return self.__v_encoders

    def set_v_encoders(self, v_encoders):
        if isinstance(v_encoders, list) and len(v_encoders) >= 1:
            self.__v_encoders = v_encoders
            return True
        return False
    
    def get_v_presets(self):
        return self.__v_presets

    def set_v_presets(self, v_presets):
        if isinstance(v_presets, list):
            self.__v_presets = v_presets
            return True
        return False

    def get_v_filters(self):
        return self.__v_filters

    def set_v_filters(self, v_filters):
        if isinstance(v_filters, list):
            self.__v_filters = v_filters
            return True
        return False
    
    def get_a_encoders(self):
        return self.__a_encoders

    def set_a_encoders(self, a_encoders):
        if isinstance(a_encoders, list):
            self.__a_encoders = a_encoders
            return True
        return False

    def get_a_filters(self):
        return self.__a_filters

    def get_avail_file_extensions(self):
        return self.__avail_extension

    def set_avail_file_extensions(self, liste):
        if isinstance(liste, list):
            self.__avail_extension = liste
            return True
        return False

    def show(self):
        print("\tEdit-Liste:\t\t\t->", self.__edit_list)
        print("\tFilme insgesamt:\t\t->", self.__total)
        print("\tXML Dateien:\t\t\t->", self.__xml_list)
        print("\tVideo-Encoder Liste:\t\t->", self.__v_encoders)
        print("\tVideo-Encoder Presets:\t\t->", self.__v_presets)
        print("\tVideofilter Liste:\t\t->", self.__v_filters)
        print("\tVideoqualitätskontrolle\t\t->", self.__v_qcontrols)
        print("\tAudio-Encoder Liste:\t\t->", self.__a_encoders)
        print("\tAudiofilter Liste:\t\t->", self.__a_filters)
        print("\tVerfügbare Dateiendungen:\t->", self.__avail_extension)
