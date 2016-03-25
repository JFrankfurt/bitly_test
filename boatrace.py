# -*- coding: utf-8 -*-
"""
Calculates average of times from a set starting point.

The list of finish times should be provided in format: hh:mm xM, DAY n

example usage:
    startTime = "08:00 AM, DAY 1"
    finishTimes = ["08:01 AM, DAY 1", "12:00 PM, DAY 65", "12:00 AM, DAY 34"]

    x = Race(startTime, finishTimes)
    x.avgMinutes()

@author: Jordan Frankfurt
"""

from decimal import *


class Race:
    def __init__(self, startDate, finishTimes):
        self.startDate = startDate
        self.finishTimes = finishTimes
        self._constraints(startDate, finishTimes)

    def _getnM(self, time):
        if (time[6:7] is 'P' and time[:2] is not '12'):
            return 12
        else:
            return 0

    def _getDays(self, time):
        return int(time[-2:])

    def _getHours(self, time):
        return int(time[:2])

    def _getMinutes(self, time):
        return int(time[3:5])

    def _timeInMinutes(self, time):
        hours = self._getnM(time)
        days = self._getDays(time)
        hours += self._getHours(time)
        minutes = self._getMinutes(time)

        minutes += days * 1440
        minutes += hours * 60

        return minutes

    # Averages the finishTimes provided
    def avgMinutes(self):
        # reduce the average by the start date in minutes
        minutes = self._timeInMinutes(self.startDate) * -1 * len(self.finishTimes)

        # iterate through list and slices strings into ints
        for x in range(len(self.finishTimes)):
            minutes += self._timeInMinutes(self.finishTimes[x])

        # Decimal doesn't like rounding things unnecessarily
        if (len(finishTimes) is 1):
            print(minutes)
            return minutes

        # Calculate and return average finish time in minutes
        averageMinutes = Decimal(minutes)/Decimal(len(finishTimes))
        averageMinutes = averageMinutes.quantize(
                Decimal('1.'),
                rounding=ROUND_HALF_UP
                )
        print(averageMinutes)
        return averageMinutes

    # Error handling
    def _constraints(self, startDate, finishTimes):
        if (type(finishTimes) is not list or type(startDate) is not str):
            raise Exception('One of your arguments was the wrong type.')
        if (len(finishTimes) > 50 or len(finishTimes) < 1):
            raise Exception('Boats, mang, you got the wrong #. 0 < boats < 51')
        for x in range(len(finishTimes)):
            if (self._timeInMinutes(startDate) > self._timeInMinutes(finishTimes[x])):
                raise Exception("""
                    The time in index {:d} is less than the start time.
                        """.format(x))
            if (len(finishTimes[x]) > 16):
                raise Exception("""
                    Time length must be <= 16.
                    You *might* have included too many days.
                    0 < days < 100
                    Check index {:d}.
                        """.format(x))
            if (self._getDays(finishTimes[x]) < 1):
                raise Exception("""
                    You likely had too few days.
                    days > 0
                    Check index {:d}.
                        """.format(x))
            if (self._getHours(finishTimes[x]) > 12):
                raise Exception("""
                    You likely had too large a number for hours.
                    0 <= hours < 13
                    Check index {:d}.
                        """.format(x))
            if (self._getMinutes(finishTimes[x]) > 59):
                raise Exception("""
                    You likely had too large a number of minutes.
                    0 <= minutes < 60
                    Check index {:d}.
                        """.format(x))

startTime = "08:00 AM, DAY 1"
finishTimes = ["08:01 AM, DAY 1", "08:01 AM, DAY 3", "08:00 AM, DAY 1"]

x = Race(startTime, finishTimes)
x.avgMinutes()
