from time import localtime

output = []

config = {
    # Lokale Pfade
    "home_directory_path": "./",
    "local_mount_path": "../mount/",
    "ssh_path": "../.ssh/",
    # Remote Pfade
    "waiting_files_path": "../mount/waiting/",
    "progress_files_path": "../mount/progress/",
    "done_files_path": "../mount/done/",
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
    "version": "Version 20230114-01 - EntwicklungsRelease"
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
