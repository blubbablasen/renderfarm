import os
from time import localtime

output = []

config = {
    # Lokale Pfade
    "home_directory_path": "/home/convert_job/",
    "local_mount_path": "/home/convert_job/mount/",
    "ssh_path": "/home/convert_job/.ssh/",
    # Remote Pfade
    "waiting_files_path": "/home/convert_job/mount/00_waiting/",
    "convert_files_path": "/home/convert_job/mount/01_convert/",
    "edit_files_path": "/home/convert_job/mount/02_edit/",
    "done_files_path": "/home/convert_job/mount/03_done/",
    # Dateinamen
    "pid_filename": "pidfile",
    "running_filename": "running.pid",
    "ffmpeg_cfg_filename": "ffmpeg.cfg",
    "ssh_id_filename": "convert_job",
    # Sonstiges
    "ip_online_check": "8.8.8.8",
    "hour": localtime().tm_hour,
    "ssh_sha256sum": "66bc2f2aba887e875dce3749703b2a7a0bb8094e1a6eacc50c51430e44ec6782",
    "remotehost": "homeserver.blubbablasen.de",
    "remotehost_port": 34,
    "remotehost_mountdir": "/samba/convert_job",
    "delay": False,
    "debug": False,
    "ffmpeg_verbose": "-8",
    "version": "Version 2023011802 - EntwicklungsRelease"
}

binaries = {
    "cat": False,
    "ping": False,
    "sync": False,
    "tail": False,
    "egrep": False,
    "sshfs": False,
    "ffmpeg": False,
    "ffprobe": False,
    "mountpoint": False,
    "sha256sum": False
}
