from collections import OrderedDict


class FinTS3Segment:
    def __init__(self):
        raise NotImplementedError()

    def get_counter(self):
        return self.elements['head']['counter']

    def set_counter(self, counter):
        self.elements['head']['counter'] = counter

    # Parse/encode binary dataelements while ignoring the size
    def __parse_binary(self, DE):
        if DE[0:1] == '@':
            bdata = DE.split('@')
            return bytes(bdata[2], 'ISO-8859-2')
        return DE

    def __encode_binary(self, DE):
        if type(DE) is bytes:
            return str('@{0}@{1}'.format(len(DE), str(DE, 'ISO-8859-2')))
        return str(DE)

    def from_ascii(self, ascii):
        for i, DG in enumerate(ascii.split('+')):
            key = list(self.elements.keys())[i]

            if type(self.elements[key]) is OrderedDict:

                for ii, DE in enumerate(DG.split(':')):
                    kkey = list(self.elements[key].keys())[ii]
                    self.elements[key][kkey] = self.__parse_binary(DE)

            else:
                self.elements[key] = self.__parse_binary(DG)

    def to_ascii(self):
        ascii = ''

        for key in self.elements.keys():
            if type(self.elements[key]) is OrderedDict:
                for element in self.elements[key]:
                    ascii += self.__encode_binary(self.elements[key][element]) + ':'
                ascii = ascii[:-1]
            else:
                ascii += self.__encode_binary(self.elements[key])
            ascii += '+'
        ascii = ascii[:-1]

        return ascii
