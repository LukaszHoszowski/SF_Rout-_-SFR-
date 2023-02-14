import os
import sys


def loading_cli_arguments():
    try:
        cli_path_input = sys.argv[1]
        cli_path_output = sys.argv[2]
    except:
        cli_path_input = ''
        cli_path_output = ''

    abs_path = os.path.join(os.path.dirname( __file__ ), '..' )    

    if cli_path_input:
        report_list = cli_path_input
    else:
        report_list = abs_path + str(os.getenv("REPORT_LIST"))

    if cli_path_output:
        report_directory = cli_path_output
    else:
        report_directory = abs_path + str(os.getenv("REPORT_DIRECTORY"))    

    return abs_path, report_list, report_directory