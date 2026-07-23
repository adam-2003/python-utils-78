class Constants:
    PI = 3.14159
    E = 2.71828
    GRAVITY = 9.80665
    SPEED_OF_LIGHT = 299792458

    @staticmethod
    def get_constants():
        return {
            'PI': Constants.PI,
            'E': Constants.E,
            'GRAVITY': Constants.GRAVITY,
            'SPEED_OF_LIGHT': Constants.SPEED_OF_LIGHT,
        }

    @staticmethod
    def is_valid_constant(name):
        return name in Constants.get_constants()

    @staticmethod
    def value_of(name):
        return Constants.get_constants().get(name, None)