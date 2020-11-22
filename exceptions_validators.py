class Validator:
    @staticmethod
    def coord_validate(x):
        if not x.isdigit():
            raise TypeError
        if int(x) < 0 or int(x) > 7:
            raise ValueError


class BoardError(Exception):
    pass