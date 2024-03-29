import os
'''

IMPORTANT NOTE: Do NOT change any of the function names or their signatures
(the parameters they take).
Your functions must behave exactly as described. Please check correctness by
running DocTests  included in function headers. You may not use any print or
input statements in your code.

Manage a calendar database.

A calendar is a dictionary keyed by date ("YYYY-MM-DD") with value being a list
of strings, the events on the specified date.

'''


# -----------------------------------------------------------------------------
# Please implement the following calendar commands
# -----------------------------------------------------------------------------

def command_help():
    """
    () -> str
    This function is already implemented. Please do not change it.
    Returns a help message for the system. That is...
    """

    help_me = """
    Help for Calendar. The calendar commands are

    add DATE START END DETAILS               add the event DETAILS at the specified DATE with specific START and END time
    show                                     show all events in the calendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from
                                   the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user data follows command:

    command: add 2018-10-12 18 19 dinner with jane
    success

    command: show
        2018-10-12 : 
            start : 08:00, 
			end : 09:00,
			title : Eye doctor
			
            start : 12:30,
			end : 13:00,
			title : lunch with sid
            
			start : 18:00,
			end : 19:00, 
			title : dinner with jane
        2018-10-29 : 
            start : 10:00,
			end : 11:00,
			title : Change oil in blue car
			
            start : 12:00,
			end : 14:00,
			title : Fix tree near front walkway
			
            start : 18:00,
			end : 19:00,
			title : Get salad stuff, leuttice, red peppers, green peppers
        2018-11-06 : 
            start : 18:00,
			end : 22:00,
			title : Sid's birthday

    command: delete 2018-10-29 10
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2018-12-21
    2016-01-02

    START and END has a format HH where HH is an hour in 24h format, for example
    09
    21

    Event DETAILS consist of alphabetic characters,
    no tabs or newlines allowed.
    """
    return help_me


def command_add(date, start_time, end_time, title, calendar):
    """
    (str, int, int, str, dict) -> boolean
    Add title to the list at calendar[date]
    Create date if it was not there
    Adds the date if start_time is less or equal to the end_time

    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer from 0-23 representing the start time
    end_time: An integer from 0-23 representing the start time
    title: A string describing the event
    calendar: The calendar database
    return: boolean of whether the even was successfully added

    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 10, 9, "go out with friends after test", calendar)
    False
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], \
    "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    """

    # YOUR CODE GOES HERE
    if start_time > end_time or start_time > 24 or end_time > 24 or start_time < 0 or end_time < 0:
        return False
    elif date in calendar.keys():

        calendar.setdefault(date, []).insert(0,{"start": start_time, "end": end_time, "title": title})
        return True
    else:
        calendar[date] = [{"start": start_time, "end": end_time, "title": title}]

        return True





def command_show(calendar):
    r"""
    (dict) -> str
    Returns the list of events for calendar sorted in decreasing date order
    and increasing time order within the date
    as a string, see examples below for a sample formatting
    calendar: the database of events

    Example:
    >>> calendar = {}
    >>> command_add("2018-01-15", 11, 13, "Eye doctor", calendar)
    True
    >>> command_add("2018-01-15", 8, 9, "lunch with sid", calendar)
    True
    >>> command_add("2018-02-10", 12, 23, "Change oil in blue car", calendar)
    True
    >>> command_add("2018-02-10", 20, 22, "dinner with Jane", calendar)
    True
    >>> command_add("2017-12-22", 5, 8, "Fix tree near front walkway", calendar)
    True
    >>> command_add("2017-12-22", 13, 15, "Get salad stuff", calendar)
    True
    >>> command_add("2018-05-06", 19, 23, "Sid's birthday", calendar)
    True
    >>> command_show(calendar)
    "\n2018-05-06 : \n    start : 19:00,\n    end : 23:00,\n    title : Sid's birthday\n2018-02-10 : \n    start : 12:00,\n    end : 23:00,\n    title : Change oil in blue car\n\n    start : 20:00,\n    end : 22:00,\n    title : dinner with Jane\n2018-01-15 : \n    start : 08:00,\n    end : 09:00,\n    title : lunch with sid\n\n    start : 11:00,\n    end : 13:00,\n    title : Eye doctor\n2017-12-22 : \n    start : 05:00,\n    end : 08:00,\n    title : Fix tree near front walkway\n\n    start : 13:00,\n    end : 15:00,\n    title : Get salad stuff"
    """
    keys_sorted = []
    ans = ''
    keys_sorted = sorted(calendar, reverse=True)
    starttime_sort = {}
    count = []
    for keys in keys_sorted:
        # events = sorted(calendar[keys])
        starttime_sort[keys] = sorted(calendar[keys], key=lambda k: k['start'])
    for key in starttime_sort:
        for j in starttime_sort[key]:
            ans += '\n' + (str(key) + ' : \n   ', '' + '\n   ')[key == count] + ' start : ' + \
                   (str(j['start']), '0' + str(j['start']))[j['start'] < 10] + ':00,\n    end : ' + \
                   (str(j['end']), '0' + str(j['end']))[j['end'] < 10] + ':00,\n    title : ' + str(j['title'])
            count = key

    return ans




def command_delete(date, start_time, calendar):
    """
    (str, int, dict) -> str
    Delete the entry at calendar[date][start_time]
    If calendar[date] is empty, remove this date from the calendar.
    If the entry does not exist, do nothing
    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer indicating the start of the event in calendar[date] to delete
    calendar: The calendar database
    return: a string indicating any errors, True for no errors

    Example:


    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": \
    [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], "2018-02-28": [{"start": 11, "end": 12, \
    "title": "Python class"}]}
    True
    >>> command_delete("2015-01-01", 1, calendar)
    '2015-01-01 is not a date in the calendar'
    >>> command_delete("2018-03-11", 3, calendar)
    'There is no event with start time of 3 on date 2018-03-11 in the calendar'
    >>> command_delete("2018-02-28", 11, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}]}
    True
    >>> command_delete("2018-03-11", 14, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}]}
    True
    >>> command_delete("2018-03-13", 13, calendar)
    True
    >>> calendar == {}
    True

    """

    # YOUR CODE GOES HERE
    ind = 0
    count = 0

    if date in calendar:
        if len(calendar[date]) > 0:
            for i in range(len(calendar[date])):
                count = count + 1
                if start_time == calendar[date][i]["start"]:

                    del calendar[date][i]
                    if len(calendar[date]) == 0:
                        del calendar[date]
                    return True
            else:
                return "There is no event with start time of " + str(start_time) + " on date " + str(
                    date) + " in the calendar"
        else:
            del calendar[date]
            return False
    else:
        return date + " is not a date in the calendar"





# -----------------------------------------------------------------------------
# Functions dealing with calendar persistence
# -----------------------------------------------------------------------------

"""
The calendar is read and written to disk.

...

date_i is "YYYY-MM-DD"'
description can not have tab or new line characters in them.

"""


def save_calendar(calendar):
    """
    (dict) -> bool
    Save calendar to 'calendar.txt', overwriting it if it already exists. The calendar events do not have
    to be saved in any particular order

    The format of calendar.txt is the following:

    date_1:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n
    date_2:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n
    date_n:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n

    Example: The following calendar...



        2018-03-13 : 
                start : 13:00,
                end : 13:00,
                title : Have fun
        2018-03-11 : 
                start : 10:00,
                end : 12:00,
                title : Another event on this date

                start : 14:00,
                end : 16:00,
                title : CSCA08 test 2
        2018-02-28 : 
                start : 11:00,
                end : 12:00,
                title : Python class

     appears in calendar.txt as ...

    2018-03-13:13-13 Have fun
    2018-03-11:10-12 Another event on this date    14-16 CSCA08 test 2
    2018-02-28:11-12 Python class

    calendar: dictionary containing a calendar
    return: True if the calendar was saved.
    """
    # YOUR CODE GOES HERE
    keys_sorted = []
    ans = ''
    keys_sorted = sorted(calendar, reverse=True)
    starttime_sort = {}
    count = []
    for keys in keys_sorted:
        # events = sorted(calendar[keys])
        starttime_sort[keys] = sorted(calendar[keys], key=lambda k: k['start'])

    ''' Putting SHOW CODE IN BETWEEN'''
    file = 'calendar.txt'
    ans = ''
    count = []
    line_no = 0
    for key in starttime_sort:
        for j in starttime_sort[key]:
            ans += (('\n', '')[line_no == 0] + str(key) + ':', '' + '\t')[key == count] + ("0", "")[
                j['start'] > 9] + str(j['start']) + "-" + ("0", "")[j['end'] > 9] + str(
                j['end']) + " " + str(j['title'])
            count = key
            line_no += 1
    ans += ('\n', '')[len(starttime_sort) == 0]
    with open(file, 'w') as my_file:
        my_file.write(ans)
        return True


def load_calendar():
    '''
    () -> dict
    Load calendar from 'calendar.txt'. If calendar.txt does not exist,
    create and return an empty calendar. For the format of calendar.txt
    see save_calendar() above.

    return: calendar.

    '''

    # YOUR CODE GOES HERE
    check = os.path.isfile("Calendar.txt")
    file = "Calendar.txt"
    calendar = {}
    collect = {}

    if check:
        with open(file, 'r') as my_file:
            data = my_file.readlines()
            for line in data:
                output = line.rstrip().split(":")
                date = output[0]
                output1 = output[1].split("\t")
                stuff = []
                for i in range(0, len(output1)):
                    output2 = output1[i].split(" ", 1)
                    output3 = output2[0].split("-")
                    start = output3[0]
                    end = output3[1]
                    event = output2[1]
                    collect = {'start': int(start), 'end': int(end), 'title': event}
                    stuff += [collect]
                    calendar[date] = stuff
            return calendar




    else:
        with open(file, 'w') as my_file2:
            my_file2.write("")
        return calendar


# -----------------------------------------------------------------------------
# Functions dealing with parsing commands
# -----------------------------------------------------------------------------


def is_command(command):
    '''
    (str) -> bool
    Return whether command is a valid command
    Valid commands are any of the options below
    "add", "delete", "quit", "help", "show"
    You are not allowed to use regular expressions in your implementation.
    command: string
    return: True if command is one of ["add", "delete", "quit", "help", "show"]
    false otherwise
    Example:
    >>> is_command("add")
    True
    >>> is_command(" add ")
    False
    >>> is_command("List")
    False

    '''

    # YOUR CODE GOES HERE
    air = 0
    check = ["add", "delete", "quit", "help", "show"]
    for i in range(len(check)):
        air = air + 1
        if command == check[i]:
            return True
        elif air >= len(check):
            return False
        else:
            continue





def is_calendar_date(date):
    '''
    (str) -> bool
    Return whether date looks like a calendar date
    date: a string
    return: True, if date has the form "YYYY-MM-DD" and False otherwise
    You are not allowed to use regular expressions in your implementation.
    Also you are not allowed to use isdigit() or the datetime module functions.

    Example:

    >>> is_calendar_date("15-10-10") # invalid year
    False
    >>> is_calendar_date("2015-10-15")
    True
    >>> is_calendar_date("2015-5-10") # invalid month
    False
    >>> is_calendar_date("2015-15-10") # invalid month
    False
    >>> is_calendar_date("2015-05-10")
    True
    >>> is_calendar_date("2015-10-55") # invalid day
    False
    >>> is_calendar_date("2015-55") # invalid format
    False
    >>> is_calendar_date("jane-is-gg") # YYYY, MM, DD should all be digits
    False

    Note: This does not validate days of the month, or leap year dates.

    >>> is_calendar_date("2015-04-31") # True even though April has only 30 days.
    True

    '''
    # Algorithm: Check length, then pull pieces apart and check them. Use only
    # basic string
    # manipulation, comparisons, and type conversion. Please do not use any
    # powerful date functions
    # you may find in python libraries.
    # 2015-10-12
    # 0123456789

    # YOUR CODE GOES HERE
    info = date.rstrip().split('-')
    if len(info[0]) == 4:
        if len(info[1]) == 2:
            if info[1] > "0" and info[1] < "13":
                if len(info[2]) == 2:
                    if info[2] > "0" and info[2] < "32":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False




def is_natural_number(str):
    '''
    (str) -> bool
    Return whether str is a string representation of a natural number,
    that is, 0,1,2,3,...,23,24,...1023, 1024, ...
    In CS, 0 is a natural number
    param str: string
    Do not use string functions
    return: True if num is a string consisting of only digits. False otherwise.
    Example:

    >>> is_natural_number("0")
    True
    >>> is_natural_number("05")
    True
    >>> is_natural_number("2015")
    True
    >>> is_natural_number("9 3")
    False
    >>> is_natural_number("sid")
    False
    >>> is_natural_number("2,192,134")
    False

    '''
    # Algorithm:
    # Check that the string has length > 0
    # Check that all characters are in ["0123456789"]

    # YOUR CODE GOES HERE
    count = 0
    if len(str) < 1:
        return False
    else:
        for i in range(len(str)):
            count = count + 1
            if ord(str[i]) < 48 or ord(str[i]) > 57:
                return False
            elif count >= len(str):
                return True


def parse_command(line):
    '''
    (str) -> list
    Parse command and arguments from the line. Return a list
    [command, arg1, arg2, ...]
    Return ["error", ERROR_DETAILS] if the command is not valid.
    Return ["help"] otherwise.
    The valid commands are

    1) add DATE START_TIME END_TIME DETAILS
    2) show
    3) delete DATE START_TIME
    4) quit
    5) help

    line: a string command
    return: A list consiting of [command, arg1, arg2, ...].
    Return ["error", ERROR_DETAILS], if line can not be parsed.
    ERROR_DETAILS displays how to use the

    Example:
    >>> parse_command("add 2015-10-21 10 11 budget meeting")
    ['add', '2015-10-21', 10, 11, 'budget meeting']
    >>> parse_command("")
    ['help']
    >>> parse_command("not a command")
    ['help']
    >>> parse_command("help")
    ['help']
    >>> parse_command("add")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22 7 7 Tims with Sally.")
    ['add', '2015-10-22', 7, 7, 'Tims with Sally.']
    >>> parse_command("add 2015-10-35 7 7 Tims with Sally.")
    ['error', 'not a valid calendar date']
    >>> parse_command("show")
    ['show']
    >>> parse_command("show calendar")
    ['error', 'show']
    >>> parse_command("delete")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22 11")
    ['error', 'not a valid calendar date']
    >>> parse_command("delete 2015-10-22 3,14")
    ['error', 'not a valid event start time']
    >>> parse_command("delete 2015-10-22 14")
    ['delete', '2015-10-22', '14']
    >>> parse_command("quit")
    ['quit']

    '''
    # HINT: You can first split, then join back the parts of
    # the final argument.
    # YOUR CODE GOES HERE
    valid = ["add", "show", "delete", "quit", "help"]
    check = line.rstrip().split(' ', 4)
    if check[0] in valid:
        if check[0] == "show":
            if len(check) > 1:
                return ['error', 'show']
            return ["show"]
        if check[0] == "quit":
            if len(check) > 1:
                return ['error', 'quit']
            return ["quit"]
        if check[0] == "add":

            if len(check) != 5:
                return ['error', 'add DATE START_TIME END_TIME DETAILS']
            info = check[1].rstrip().split('-')
            if len(info[0]) == 4:
                if len(info[1]) == 2:
                    if info[1] > "0" and info[1] < "13":
                        if len(info[2]) == 2:
                            if info[2] > "0" and info[2] < "32":
                                if check[2] > "0" or check[2] < "25":
                                    if check[3] > '0' or check[3] < '25':
                                        check[2] = int(check[2])
                                        check[3] = int(check[3])
                                        return check
                                    else:
                                        return ["error", ""]
                                else:
                                    return ["error", ""]
                            else:
                                return ["error", "not a valid calendar date"]
                    else:
                        return ["error", "not a valid calendar month"]
            else:
                return ['error', 'not a valid calendar date']
        if check[0] == "delete":
            if len(check) != 3:
                return ['error', 'delete DATE START_TIME']
            info = check[1].rstrip().split('-')
            if len(check) == 3:
                if len(info[0]) == 4:
                    if len(info[1]) == 2:
                        if info[1] > "0" and info[1] < "13":
                            if len(info[2]) == 2:
                                if info[2] > "0" and info[2] < "32":
                                    if len(check[2]) == 2 or len(check[2]) == 1:
                                        if check[2] > '0' or check[2] < '25':
                                            supkadna = [check[0], check[1], int(check[2])]
                                            return supkadna
                                        else:
                                            return ["error", "not a valid event start time"]
                                    else:
                                        return ["error", "not a valid event start time"]
                                else:
                                    return ["error", "not a valid calendar date"]
                            else:
                                return ["error", "not a valid calendar date"]
                        else:
                            return ["error", "not a valid calendar date"]
                    else:
                        return ["error", "not a valid calendar date"]
                else:
                    return ["error", "not a valid calendar date"]
            else:
                return ["error", "delete DATE START_TIME"]
        else:
            return ['help']
    else:
        return ["help"]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
