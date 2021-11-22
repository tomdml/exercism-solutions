import calendar

ordinal = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
           'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}


def meetup(year, month, desc, day):
    c = calendar.Calendar()

    filterdays = [d for d
                  in c.itermonthdates(year, month)
                  if d.weekday() == ordinal[day] and d.month == month]

    if desc == 'teenth':
        return [d for d in filterdays if 13 <= d.day <= 19][0]
    else:
        try:
            return filterdays[int(desc[0]) - 1 if desc[0].isdigit() else -1]
        except IndexError:
            raise MeetupDayException('Invalid input!')


class MeetupDayException(Exception):
    pass
