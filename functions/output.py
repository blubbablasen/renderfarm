from config import config, output
from functions.localhost import remove_pidfile
from time import sleep
import os


def verbose(status_obj):
    os.system('clear')
    if config["debug"]:
        print("Systemstatus")
        status_obj.show()

    for elem in output:
        print("  " + str(elem))

    if status_obj.get_terminate_exec():
        if status_obj.get_writing_pid_file():
            remove_pidfile(config["pid_filename"], status_obj)
            exit("\n\nProgramm wurde vorzeitig beendet.")
    if config["delay"]:
        sleep(2)
