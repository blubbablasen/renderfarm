class Status:
    def __init__(self):
        self.__competing_application = False
        self.__competing_application_pid = None
        self.__pid = None
        self.__writing_pid_file = False
        self.__os_bin_available = False
        self.__localhost_is_online = False
        self.__remotehost_is_online = False
        self.__local_mountdir_exist = False
        self.__local_mountdir_is_free = False
        self.__ssh_id_file_exist = False
        self.__ssh_sha256sum_valid = False
        self.__remotehost_is_mount = False
        self.__job_is_running = False
        self.__ffmpeg_cfg_found = False
        self.__ffmpeg_parse_cfg = False
        self.__convert_job_to_do = False
        self.__job_to_do = False
        self.__unmount_remotehost = None
        self.__terminate_exec = False

    def get_convert_job_to_do(self):
        return self.__convert_job_to_do

    def set_convert_job_to_do(self, boolean):
        if isinstance(boolean, bool):
            self.__convert_job_to_do = boolean
            return True
        return False

    def get_competing_application(self):
        return self.__competing_application

    def get_competing_application_pid(self):
        return self.__competing_application_pid

    def get_pid(self):
        return self.__pid

    def get_writing_pid_file(self):
        return self.__writing_pid_file

    def get_os_bin_available(self):
        return self.__os_bin_available

    def get_localhost_is_online(self):
        return self.__localhost_is_online

    def get_remotehost_is_online(self):
        return self.__remotehost_is_online

    def get_local_mountdir_exist(self):
        return self.__local_mountdir_exist
    
    def get_local_mountdir_is_free(self):
        return self.__local_mountdir_is_free

    def get_ssh_id_file_exist(self):
        return self.__ssh_id_file_exist

    def get_ssh_sha256sum_valid(self):
        return self.__ssh_sha256sum_valid

    def get_remotehost_is_mount(self):
        return self.__remotehost_is_mount
    
    def get_job_is_running(self):
        return self.__job_is_running
    
    def get_ffmpeg_cfg_found(self):
        return self.__ffmpeg_cfg_found

    def get_ffmpeg_parse_cfg(self):
        return self.__ffmpeg_parse_cfg
    
    def get_job_to_do(self):
        return self.__job_to_do
    
    def get_unmount_remotehost(self):
        return self.__unmount_remotehost

    def get_terminate_exec(self):
        return self.__terminate_exec

    def set_competing_application(self, boolean):
        if isinstance(boolean, bool):
            self.__competing_application = boolean
            return True
        return False

    def set_competing_application_pid(self, integer):
        if not isinstance(integer, int) or integer < 1 or integer > 4194304:
            return False
        self.__competing_application_pid = integer
        return True

    def set_pid(self, integer):
        if integer < 1 or integer > 4194304 or not isinstance(integer, int):
            return False
        self.__pid = integer
        return True
    
    def set_writing_pid_file(self, boolean):
        if isinstance(boolean, bool):
            self.__writing_pid_file = boolean
            return True
        return False

    def set_os_bin_available(self, boolean):
        if isinstance(boolean, bool):
            self.__os_bin_available = boolean
            return True
        return False

    def set_localhost_is_online(self, boolean):
        if isinstance(boolean, bool):
            self.__localhost_is_online = boolean
            return True
        return False

    def set_remotehost_is_online(self, boolean):
        if isinstance(boolean, bool):
            self.__remotehost_is_online = boolean
            return True
        return False

    def set_local_mountdir_exist(self, boolean):
        if isinstance(boolean, bool):
            self.__local_mountdir_exist = boolean
            return True
        return False

    def set_local_mountdir_is_free(self, boolean):
        if isinstance(boolean, bool):
            self.__local_mountdir_is_free = boolean
            return True
        return False

    def set_ssh_id_file_exist(self, boolean):
        if isinstance(boolean, bool):
            self.__ssh_id_file_exist = boolean
            return True
        return False

    def set_ssh_sha256sum_valid(self, boolean):
        if isinstance(boolean, bool):
            self.__ssh_sha256sum_valid = boolean
            return True
        return False

    def set_remotehost_is_mount(self, boolean):
        if isinstance(boolean, bool):
            self.__remotehost_is_mount = boolean
            return True
        return False

    def set_job_is_running(self, boolean):
        if isinstance(boolean, bool):
            self.__job_is_running = boolean
            return True
        return False

    def set_ffmpeg_cfg_found(self, boolean):
        if isinstance(boolean, bool):
            self.__ffmpeg_cfg_found = boolean
            return True
        return False

    def set_ffmpeg_parse_cfg(self, boolean):
        if isinstance(boolean, bool):
            self.__ffmpeg_parse_cfg = boolean
            return True
        return False

    def set_job_to_do(self, boolean):
        if isinstance(boolean, bool):
            self.__job_to_do = boolean
            return True
        return False

    def set_unmount_remotehost(self, boolean):
        if isinstance(boolean, bool):
            self.__unmount_remotehost = boolean
            return True
        return False

    def set_terminate_exec(self, boolean):
        if isinstance(boolean, bool):
            self.__terminate_exec = boolean
            return True
        return False

    def show(self):
        print("\tCompeting Application\t\t->", self.__competing_application)
        print("\tCompeting Application PID\t->", self.__competing_application_pid)
        print("\tSetting PID\t\t\t->", self.__pid)
        print("\tWriting PID-File\t\t->", self.__writing_pid_file, "\n")
        print("\tAll OS Binaries are available\t->", self.__os_bin_available, "\n")
        print("\tLocalhost is online\t\t->", self.__localhost_is_online)
        print("\tRemotehost is online\t\t->", self.__remotehost_is_online)
        print("\tLocal Mount-Directory exist\t->", self.__local_mountdir_exist)
        print("\tLocal Mount-Directory is free\t->", self.__local_mountdir_is_free)
        print("\tSSH ID File exist\t\t->", self.__ssh_id_file_exist)
        print("\tSSH sha256sum is valid\t\t->", self.__ssh_sha256sum_valid, "\n")
        print("\tRemotehost is mount\t\t->", self.__remotehost_is_mount)
        print("\tJob is running\t\t\t->", self.__job_is_running)
        print("\tFFMPEG Config found\t\t->", self.__ffmpeg_cfg_found)
        print("\tFFMPEG parsing Config\t\t->", self.__ffmpeg_parse_cfg, "\n")
        print("\tConvert Job to do?\t\t->", self.__convert_job_to_do)
        print("\tAnything to do?\t\t\t->", self.__job_to_do)
        print("\tRemotehost unmount\t\t->", self.__unmount_remotehost, "\n")
        print("\tProgramm abgebrochen\t\t->", self.__terminate_exec, "\n\n")
