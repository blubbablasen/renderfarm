#!/usr/bin/env python3
from sys import argv
from config import *
from classes.Status import *
from functions.localhost import *
from functions.remotehost import *
from functions.ffmpeg import *
from functions.output import verbose

os.system('clear')
status_obj = Status()

# Übergabeparameter aus dem Terminal (Liste)
if len(argv) > 1:
    terminal_param(argv, config)

# PID
create_pidfile(config["pid_filename"], status_obj, output)

# All OS Binaries are available
os_env_require(binaries, status_obj, output)
verbose(status_obj)

# Ping Localhost is Online and Remotehost is Online
ping(config["ip_online_check"], status_obj, output)
verbose(status_obj)
ping(config["remotehost"], status_obj, output)
verbose(status_obj)

# Local Mount-directory exist
local_mountdir_exist(config["local_mount_path"], status_obj, output)
verbose(status_obj)

# Local Mount-directory is free
local_mountpoint_is_free(config["local_mount_path"], status_obj, output)
verbose(status_obj)

# SSH ID File exist
ssh_id_file_exist(config["ssh_path"] + config["ssh_id_filename"], status_obj, output)
verbose(status_obj)

# SSH ID File sha256sum is valid
ssh_sha256sum_calc(config["ssh_path"] + config["ssh_id_filename"],
                   config["ssh_sha256sum"], status_obj, output
                   )
verbose(status_obj)

# Mount Remotehost via SSH
mount_remotehost(config["ssh_path"] + config["ssh_id_filename"],
                 config["remotehost"], config["remotehost_port"],
                 config["remotehost_mountdir"], config["local_mount_path"],
                 status_obj, output)
verbose(status_obj)

# Job running-File is present
another_job_is_running(config["local_mount_path"] + config["running_filename"],
                       status_obj, output)
verbose(status_obj)

# FFMPEG Config found
ffmpeg_obj = ffmpeg_cfg_found(config["local_mount_path"] + config["ffmpeg_cfg_filename"],
                              status_obj, output)
verbose(status_obj)

# Parsing FFMPEG Config
parse_ffmpeg_cfg(config["local_mount_path"] + config["ffmpeg_cfg_filename"],
                 ffmpeg_obj, status_obj, output)
verbose(status_obj)

convert_job(config["convert_files_path"], config["ffmpeg_verbose"], status_obj, output)
verbose(status_obj)

ejob_obj = edit_job(config["edit_files_path"], status_obj, output)
verbose(status_obj)

split_file_name(ejob_obj, status_obj)
verbose(status_obj)

extract_parameter(ffmpeg_obj, ejob_obj, status_obj)
verbose(status_obj)

grep_file_information(config["edit_files_path"], ejob_obj, status_obj, output)



# Remotehost unmount
umount_remotehost(config["local_mount_path"], status_obj, output)
verbose(status_obj)

remove_pidfile(config["pid_filename"], status_obj, output)
verbose(status_obj)
print("\n\nEnde")

if config["debug"]:
    print("Programm Konfiguration")
    for key, value in config.items():
        print("\t", key, ": ", value)

    print("\nffmpeg Objekt")
    ffmpeg_obj.show()

    print("\nEdit Objekt: ", ejob_obj.get_full_file_name())
    ejob_obj.show()
    print("\nVideostreams:")
    for videostream in ejob_obj.get_video_list():
        videostream.show()
    print("\nAudiostreams:")
    for audiostream in ejob_obj.get_audio_list():
        audiostream.show()
