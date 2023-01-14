from module.config import info
import os


def mount_remotehost(ssh_file, remotehost, remotehost_port, remotehost_mountdir, local_mount_path, status_obj):
    if status_obj.get_localhost_is_online() and status_obj.get_remotehost_is_online() and \
       status_obj.get_local_mountdir_exist() and status_obj.get_local_mountdir_is_free() and \
       status_obj.get_ssh_id_file_exist() and status_obj.get_ssh_sha256sum_valid():
        if os.system(
                f"sshfs -o IdentityFile={ssh_file},sshfs_sync -p {remotehost_port} convert_job@{remotehost}:{remotehost_mountdir} {local_mount_path}") == 0:
            status_obj.set_local_mountdir_is_free(False)
            status_obj.set_remotehost_is_mount(True)
            info.append("Info:\t\tRemote-Dateisystem wurde erfolgreich lokal eingehangen.")
        else:
            info.append("Exit:\t\tRemote-Dateisystem wurde NICHT erfolgreich eingehangen!")
            status_obj.set_terminate_exec(True)
            status_obj.set_remotehost_is_mount(False)
    else:
        info.append("Exit:\t\tDas Remote-Dateisystem kann nicht eingehangen werden!")
        status_obj.set_terminate_exec(True)
        status_obj.set_remotehost_is_mount(False)


def umount_remotehost(local_mount_path, status_obj):
    if status_obj.get_competing_application():
        info.append("Info:\t\tRemote-Dateisystem " + local_mount_path + " wird nicht ausgehangen. " + str(
            status_obj.get_competing_application_pid()) + " Prozess im gange.")
        status_obj.set_unmount_remotehost(False)
    if status_obj.get_remotehost_is_mount() and \
            status_obj.get_job_is_running() == False:
        os.system("sync")
        if os.system(f"umount {local_mount_path}") == 0:
            status_obj.set_local_mountdir_is_free(True)
            status_obj.set_remotehost_is_mount(False)
            info.append("Info:\t\tRemote-Dateisystem wurde erfolgreich ausgehangen.")
            status_obj.set_unmount_remotehost(True)
        else:
            info.append("Warnung:\tRemote-Dateisystem " + local_mount_path + " konnte nicht ausgehangen werden!")
            status_obj.set_unmount_remotehost(False)
