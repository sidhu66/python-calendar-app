This Python script implements a basic calendar management system. The script defines functions to add, display, and delete events in a calendar database. The user interacts with the program through a command-line interface, entering commands to perform various operations on the calendar.

Here's a breakdown of the key functionalities:

1. **Adding Events (`command_add`):** Users can add events to the calendar by specifying the date, start time, end time, and event details. The script validates the input and updates the calendar accordingly.

2. **Displaying Events (`command_show`):** Users can view all events in the calendar. The script sorts the events in decreasing date order and increasing time order within each date.

3. **Deleting Events (`command_delete`):** Users can delete a specific event by providing the date and start time. If the specified event exists, it is removed from the calendar. If the date becomes empty after deletion, the date is removed from the calendar as well.

4. **Saving and Loading (`save_calendar` and `load_calendar`):** The calendar can be saved to and loaded from a text file named 'calendar.txt'. The file stores events in a specific format, allowing persistence between program runs.

5. **Parsing User Commands (`parse_command`):** The script parses user commands, validates input, and returns corresponding actions. It provides helpful error messages when the commands are not well-formed.

6. **Help Message (`command_help`):** Users can access a help message describing the available commands and their usage.

The script includes functions for validating calendar dates and natural numbers, helping ensure that the input adheres to expected formats.

Lastly, the script includes a main block to run doctests for the functions, checking if they behave as expected.


