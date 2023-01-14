import xml.sax


class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.__cut_list = []

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "entry" and attributes["producer"][0:5] == "chain":
            cut_in = attributes["in"]
            cut_out = attributes["out"]
            self.__cut_list.append({cut_in: cut_out})

    def get_cut_list(self):
        return self.__cut_list
