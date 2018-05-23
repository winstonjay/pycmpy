


class Error(object):

    def __init__(self, code, string, *args, **kwargs):
        self.code = code
        self.message = string.format(*args, **kwargs)

    def __str__(self):
        return ("{classname} {name}:\n\t{message}".format(
                classname=self.__name__,
                name=self.code,
                mesaage=self.message))


(ILLEGAL_TOKEN,
 UNEXPECTED_TOKEN,
 UNDECLARED_SYMBOL,
 UNDECLARED_FUNCTION
) = range(4)

class ParseError(Error):
    pass