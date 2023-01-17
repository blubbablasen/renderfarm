import xml.sax


class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.__tag = None
        self.__attribute = None
        self.__filename = None
        self.__cut_list = []
        self.__start = None
        self.__end = None

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.__tag = tag
        if tag == "property" and attributes["name"] == "resource":
            self.__attribute = attributes["name"]
        else:
            self.__attribute = None

        if tag == "entry" and attributes["producer"][0:6] == "chain0":
            self.__start = attributes["in"]
            self.__end = attributes["out"]

        if tag == "entry" and attributes["producer"][0:5] == "chain":
            cut_in = attributes["in"]
            cut_out = attributes["out"]
            self.__cut_list.append({cut_in: cut_out})

    def characters(self, content):
        # Dateiname
        if self.__tag == "property" and self.__attribute == "resource" \
                and content.strip() != "" and content != "0":
            self.__filename = content

    def get_cut_list(self):
        return self.__cut_list

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def get_filename(self):
        return self.__filename
