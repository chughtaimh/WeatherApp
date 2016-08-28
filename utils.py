# Contains utility functions for the Weather App.

from collections import namedtuple

Weather = namedtuple('Weather', ['city', 'temp', 'cond', 'humidity'])


def validate_zipcode(func):
    """Validates that the return value of a function :func: is a valid zip
    code."""
    def inner(text):
        val = func(text)
        try:
            int(val)
        except ValueError:
            raise ValueError('{} is not a valid numeric zip code'.format(val))
        if len(val) == 5:
            return val
        else:
            raise ValueError("{} is not a valid 5-digit zip code.".format(val))
    return inner


@validate_zipcode
def user_response(text):
    """Requests a response from the user and returns the response."""
    return raw_input(text)


def remove_tabs_new_lines(text):
    """Removes tabs and new line characters from :text: and returns."""
    return text.replace('\n', '').replace('\t', '')
