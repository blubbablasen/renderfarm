import os


def terminal_param(argv, config):
    if "--help" in argv:
        print(argv[0], "[ --parameter1 --parameter2 optional[argument] ]\n")
        print("--help\t\t\tRuft die Hilfe auf und beendet das Programm sofort.")
        print("--verbose\t\tDeutlich mehr Ausgabe wären der Laufzeit.")
        print("--delay\t\t\tZwischen jedem Schritt wird ein 2 Sekunden Delay eingebaut.")
        print("--sha256sum\t\tSHA in der Konfiguration überschreiben.")
        print("--test\t\t\tParameterübergabe mit Argument")
        print("--version\t\tGibt die Programmversion aus und beendet das Programm sofort.")
        exit(0)

    if "--version" in argv:
        print(argv[0], config["version"])
        exit(0)

    # entferne Index 0 (Programmname) aus der Liste
    del argv[0]

    if "--verbose" in argv:
        config["debug"] = True
        config["ffmpeg_verbose"] = "32"
        # entferne --verbose aus der Liste
        argv.remove("--verbose")

    if "--delay" in argv:
        config["delay"] = True
        # entferne --delay aus der Liste
        argv.remove("--delay")

    if "--sha256sum" in argv:
        # Argument für Parameter wird einen Index nach --sha256sum erwartet.
        index_shift = argv.index("--sha256sum") + 1
        try:
            # Teste das Argument besteht aus Hexadezimal-Zeichen
            int(str(argv[index_shift]), 16)
            # Überschreibe in der Config den Schlüssel ssh_sha256sum
            config["ssh_sha256sum"] = argv[index_shift]
            # Lösche das Argument aus der Liste
            del argv[index_shift]
            # Lösche --sha256sum aus der Liste
            argv.remove("--sha256sum")
        except ValueError:
            print("Der übermittelte Wert ist kein gültiger Hash.", argv[index_shift])
            exit()
        except IndexError:
            print("--sha256sum erwartet ein Argument.")
            exit()
        except:
            print("Unerwarteter Fehler. Bring deine Katze in Sicherheit!")
            exit()

    if "--test" in argv:
        # Argument für Parameter wird einen Index nach --test erwartet.
        index_shift = argv.index("--test") + 1
        try:
            # Ausgabe des Test-Argumentes
            print(argv[index_shift])
            # Lösche das Argument aus der Liste
            del argv[index_shift]
            # Lösche --test aus der Liste
            argv.remove("--test")
            exit()
        except IndexError:
            print("--test erwartet ein Argument.")
            exit()

    # Falls in der Liste etwas übrig bleibt wird es ausgegeben.
    if len(argv) > 0:
        print("Unbekannter Parameter", argv)
        exit()


def create_pidfile(pid_filename, status_obj, output):
    if os.path.isfile(pid_filename):
        with open(pid_filename, "r") as pidfile:
            status_obj.set_competing_application(True)
            status_obj.set_competing_application_pid(int(pidfile.read()))
            output.append(
                "Warnung:\tDie Anwendung läuft bereits mit der PID " + str(status_obj.get_competing_application_pid())
            )
    else:
        with open(pid_filename, "w") as pidfile:
            pidfile.write(str(os.getpid()))
            output.append("Info:\t\tpidfile wurde erfolgreich erstellt.")
            status_obj.set_pid(os.getpid())
            status_obj.set_writing_pid_file(True)


def remove_pidfile(pid_filename, status_obj, output):
    if os.path.isfile(pid_filename):
        with open(pid_filename, "r") as pidfile:
            if int(pidfile.read()) == status_obj.get_pid():
                os.remove(pid_filename)
                output.append("Info:\t\tpidfile zum Prozess wurde entfernt.")
            else:
                output.append("Warnung:\tZu entfernende pidfile gehört nicht zum aktuellen Prozess!")
    else:
        output.append("Keine PID-Datei? Soll das so?")


def os_env_require(binaries, status_obj, output):
    bin_install = []
    for key, value in binaries.items():
        if os.system(f'{key} --help > /dev/null 2>&1') != 32512:
            binaries[key] = True
        else:
            binaries[key] = False
            bin_install.append(key)
    if len(bin_install) == 0:
        output.append("Info:\t\tAlle benötigten Programme sind installiert.")
        status_obj.set_os_bin_available(True)
    else:
        output.append("Warnung:\tFolgende Programme konnten auf dem System nicht gefunden werden: " + str(bin_install))


def ping(ping_target, status_obj, output):
    if os.system(f'ping -c4 {ping_target} > /dev/null 2>&1') == 0:
        output.append("Info:\t\t" + ping_target + " antwortet.")
        if ping_target == "8.8.8.8":
            status_obj.set_localhost_is_online(True)
        else:
            status_obj.set_remotehost_is_online(True)
    else:
        output.append("Warnung:\t" + ping_target + " antwortet nicht!")
        if ping_target == "8.8.8.8":
            status_obj.set_localhost_is_online(False)
        else:
            status_obj.set_remotehost_is_online(False)


def local_mountdir_exist(local_mount_path, status_obj, output):
    if not os.path.exists(local_mount_path):
        output.append("Info:\t\t" + local_mount_path + " gibt es nicht.")
        output.append("Info:\t\tVersuche  " + local_mount_path + " zu erstellen.")
        try:
            os.makedirs(local_mount_path, exist_ok=True)
            output.append("Info:\t\t" + local_mount_path + " konnte erstellt werden.")
            status_obj.set_local_mountdir_exist(True)
        except OSError:
            output.append("Warnung:\t" + local_mount_path + " konnte nicht erstellt werden! Fehlende Rechte?")
            status_obj.set_local_mountdir_exist(False)
    else:
        output.append("Info:\t\tVerzeichnis für den Mountpoint existiert.")
        status_obj.set_local_mountdir_exist(True)


def local_mountpoint_is_free(local_mount_path, status_obj, output):
    if not status_obj.get_local_mountdir_exist():
        output.append("Warning:\tEs kann nicht überprüft werden ob  " + local_mount_path + "  ein Mountpoint ist.")
        return

    if os.system(f'mountpoint {local_mount_path} > /dev/null 2>&1') == 256:
        output.append("Info:\t\t" + local_mount_path + " ist kein Mountpoint und somit frei.")
        status_obj.set_local_mountdir_is_free(True)
    else:
        output.append("Warnung:\t" + local_mount_path + " scheint durch einen anderen Prozess belegt.")
        status_obj.set_local_mountdir_is_free(False)


def ssh_id_file_exist(ssh_file, status_obj, output):
    if not os.path.isfile(ssh_file):
        output.append("Warnung:\tSSH ID File wurde NICHT gefunden.")
        status_obj.set_ssh_id_file_exist(False)
        return

    output.append("Info:\t\tSSH ID File gefunden.")
    status_obj.set_ssh_id_file_exist(True)


def ssh_sha256sum_calc(ssh_file, ssh_sha256sum, status_obj, output):
    if not status_obj.get_ssh_id_file_exist():
        return

    with os.popen(f'sha256sum {ssh_file}') as result:
        if result.read().split()[0] == ssh_sha256sum:
            output.append("Info:\t\tSSH ID File ist gültig.")
            status_obj.set_ssh_sha256sum_valid(True)
        else:
            output.append("Warnung:\tSSH ID File ist NICHT gültig.")
            status_obj.set_ssh_sha256sum_valid(False)
