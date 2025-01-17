__author__ = 'jason'

from .PyJavapInternal import FieldAccessFlags

class Field(object):

    def __init__(self, name, descriptor, access):
        if type(name) == bytes:
            name = name.decode()
        if type(descriptor) == bytes:
            descriptor = descriptor.decode()
        if type(access) == bytes:
            access = access.decode()
        self.name = name
        self.descriptor = descriptor
        self.access = access
        self.attrCount = 0
        self.attributes = []

    def addAttribute(self, attribute):
        self.attrCount += 1
        self.attributes.append(attribute)

    def __str__(self):
        result = "Name: " + str(self.name) + "(" + str(self.descriptor) + ")"
        result += " Access: " + FieldAccessFlags.flagToStr(self.access)

        result += "\n"

        if len(self.attributes):
            result += "\tAttributes\n"
            for attr in self.attributes:
                result += "\t" + str(attr) + "\n"

        return result






