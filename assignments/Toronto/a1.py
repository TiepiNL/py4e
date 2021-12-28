"""
Programming Assignment: Assignment 1: Time Zones
"""

def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.

    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    return time_2 - time_1


def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.

    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    # Retrieve the differnce in seconds and convert it to hours.
    return seconds_difference(time_1, time_2) / 60 / 60


def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    try:
        assert 0 <= minutes and minutes < 60
        assert 0 <= seconds and seconds < 60
    except AssertionError:
        # Preconditions not met
        quit()

    return hours + (minutes / 60) + (seconds / (60 * 60))


def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    """

    return hours % 24


def get_hours(seconds):
    """ (int) -> int
    seconds is the number of seconds since midnight. Return the number of hours
    that have elapsed since midnight, as seen on a 24-hour clock.

    >>> get_hours(3800)
    1
    >>> get_hours(2400)
    0
    >>> get_hours(50485)
    14
    """

    return to_24_hour_clock(seconds // 3600)


def get_minutes(seconds):
    """ (int) -> int
    seconds is the number of seconds since midnight. Return the number of minutes that
    have elapsed since midnight as seen on a clock.

    >>> get_minutes(3800)
    3
    >>> get_minutes(2400)
    40
    >>> get_minutes(50485)
    1
    """
    return seconds % 3600 // 60


def get_seconds(seconds):
    """ (int) -> int
    seconds is the number of seconds since midnight. Return the number of seconds that
    have elapsed since midnight as seen on a clock.

    >>> get_seconds(3800)
    20
    >>> get_seconds(2400)
    0
    >>> get_seconds(50485)
    25
    """
    return seconds % 60


def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """
    totalseconds = (time - utc_offset) * 3600
    hours = get_hours(totalseconds)
    minutes = get_minutes(totalseconds)
    seconds = get_seconds(totalseconds)
    return to_float_hours(hours, minutes, seconds)


def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """
    return time_to_utc(-utc_offset, time)
