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
mount_remotehost(config["ssh_path"]+config["ssh_id_filename"],
                 config["remotehost"], config["remotehost_port"],
                 config["remotehost_mountdir"], config["local_mount_path"],
                 status_obj, output)
verbose(status_obj)

# Job running-File is present
another_job_is_running(config["local_mount_path"]+config["running_filename"],
                       status_obj, output)
verbose(status_obj)

# FFMPEG Config found
ffmpeg_obj = ffmpeg_cfg_found(config["local_mount_path"]+config["ffmpeg_cfg_filename"],
                              status_obj, output)
verbose(status_obj)

# Parsing FFMPEG Config
parse_ffmpeg_cfg(config["local_mount_path"]+config["ffmpeg_cfg_filename"],
                 ffmpeg_obj, status_obj, output)
verbose(status_obj)

# Erstelle Filmliste
create_film_list(config["local_mount_path"], ffmpeg_obj, status_obj, output)
verbose(status_obj)

# Erstelle Job Liste
job_liste = create_jobs_objects(ffmpeg_obj, status_obj, output)
verbose(status_obj)

# Zerteile Dateiname in Filmname, FFMPEG Parameter und Dateiendung
split_file_name(ffmpeg_obj, job_liste, status_obj)
verbose(status_obj)

show_for_xml_file(config["local_mount_path"], job_liste, ffmpeg_obj, status_obj)
verbose(status_obj)

# Ordne aus den FFMPEG Parametern die Aufgaben zu dem Objekt zu
extract_parameter(ffmpeg_obj, job_liste, status_obj)
verbose(status_obj)

# erstelle für jeden Film eine XML-Information, um Eingangseigenschaften des Films festzulegen.
grep_file_information(config["local_mount_path"], job_liste, status_obj, output)
verbose(status_obj)

# Berechne die überflüssigen Ränder der Filme.
# calculate_edges_top_down(config["local_mount_path"], job_liste, status_obj)
# verbose(status_obj)

# show_fast_results(config["local_mount_path"], job_liste, status_obj)
# verbose(status_obj)

# Remotehost unmount
umount_remotehost(config["local_mount_path"], status_obj, output)
verbose(status_obj)

remove_pidfile(config["pid_filename"], status_obj, output)
verbose(status_obj)
print("\n\nEnde")

if job_liste and config["debug"]:
    print("Programm Konfiguration")
    for key, value in config.items():
        print("\t", key, ": ", value)

    print("\nffmpeg Objekt")
    ffmpeg_obj.show()
    for job in job_liste:
        print("\n Job:", job.get_input_film_name())
        job.show()
        print("\n Container Streams:")
        for video_stream in job.get_video_list():
            print()
            video_stream.show()
        for audio_stream in job.get_audio_list():
            print()
            audio_stream.show()
