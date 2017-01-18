import os


def len_counting(list_to_count, dict_of_lens):
    """
    Counts counts and sets max width of column

    Args:
        list_to_count: list of items
        dict_of_lens: dictionary of item lengths

    Returns:
         dict_of_lens: dictionary with updated values
    """
    for i in range(len(list_to_count)):
        if len(list_to_count[i]) > dict_of_lens[i]:
            dict_of_lens[i] = len(list_to_count[i])

    return dict_of_lens


def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of objects - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """

    len_of_items = {x: 0 for x in range(len(title_list))}

    title_lengths = len_counting(title_list, len_of_items)

    for line in table:
        max_lengths = len_counting(line, title_lengths)

    # top bar
    table_body = "-" * (sum(max_lengths.values()) + len(max_lengths)*3 - 1)
    string_in_between = ""
    string_to_print = ""

    # titles
    for i in range(len(title_list)):
        string_to_print += "|{:^{line_len}}".format(title_list[i], line_len=max_lengths[i]+2)
        string_in_between += "|" + "-" * (max_lengths[i]+2)

    strings_to_print = [string_to_print + "|"]

    # values
    for i in range(len(table)):
        string_to_print = ""

        for j in range(len(title_list)):
            string_to_print += "|{:^{line_len}}".format(table[i][j], line_len=max_lengths[j]+2)
        strings_to_print.append(string_in_between + "|")
        strings_to_print.append(string_to_print + "|")

    # wrap_up
    strings_to_print.insert(0, ("/" + table_body + "\\"))
    strings_to_print.append("\\" + table_body + "/")
    return "\n" + "\n".join(strings_to_print) + "\n"


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """
    os.system("clear")
    print("{}:".format(title))
    for i, v in enumerate(list_options):
        print("  ({}) {}".format(int(i+1), v))
    print("  (0)", exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    if title:
        print(title)
    for item in list_labels:
        inputs.append(input(item))
    return inputs
