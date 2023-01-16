from shlex import quote
import os


# Prüfe ob bereits ein anderer Prozess läuft
def another_job_is_running(running_file, status_obj, output):
    if not os.path.exists(running_file):
        output.append("Info:\t\tEs läuft kein anderer FFMPEG-Prozess.")
        status_obj.set_job_is_running(False)
        return

    output.append("Warnung:\tEs läuft bereits ein anderer FFMPEG-Prozess!")
    status_obj.set_job_is_running(True)


# Prüfe ob eine FFMPEG Konfigurationsdatei existiert
def ffmpeg_cfg_found(ffmpeg_cfg_file, status_obj, output):
    if status_obj.get_job_is_running():
        return

    if not os.path.exists(ffmpeg_cfg_file):
        output.append("Warnung:\tFFMPEG Konfiguration NICHT gefunden!")
        status_obj.set_ffmpeg_cfg_found(False)
        return

    output.append("Info:\t\tFFMPEG Konfiguration gefunden.")
    status_obj.set_ffmpeg_cfg_found(True)
    import classes.Ffmpeg
    ffmpeg_obj = classes.Ffmpeg.Ffmpeg()
    return ffmpeg_obj


# Lese die FFMPEG Konfigurationsdatei ein
def parse_ffmpeg_cfg(ffmpeg_cfg_file, ffmpeg_obj, status_obj, output):
    if status_obj.get_job_is_running() or not status_obj.get_ffmpeg_cfg_found():
        return

    v_encoders = []
    v_presets = []
    v_filters = []
    v_qcontrols = []
    a_encoders = []
    f_extensions = []
    with open(ffmpeg_cfg_file, "r") as file:
        for line in file.readlines():
            if line[0:3] == "v_e":
                v_encoders.append(line.split(sep="=", maxsplit=1)[1].split(sep="#", maxsplit=1)[0].strip())
            if line[0:3] == "v_p":
                v_presets.append(line.split(sep="=", maxsplit=1)[1].split(sep="#", maxsplit=1)[0].strip())
            if line[0:3] == "v_q":
                v_qcontrols.append(line.split(sep="=", maxsplit=1)[1].split(sep="#", maxsplit=1)[0].strip())
            if line[0:3] == "v_f":
                v_filters.append(line.split(sep="=", maxsplit=1)[1].split(sep="#", maxsplit=1)[0].strip())
            if line[0:3] == "a_e":
                a_encoders.append(line.split(sep="=", maxsplit=1)[1].split(sep="#", maxsplit=1)[0].strip())
            if line[0:3] == "f_e":
                f_extensions.append(line.split(sep="=", maxsplit=1)[1].split(sep="#", maxsplit=1)[0].strip())
    ffmpeg_obj.set_v_encoders(v_encoders)
    ffmpeg_obj.set_v_presets(v_presets)
    ffmpeg_obj.set_v_filters(v_filters)
    ffmpeg_obj.set_v_qcontrols(v_qcontrols)
    ffmpeg_obj.set_a_encoders(a_encoders)
    ffmpeg_obj.set_avail_file_extensions(f_extensions)
    status_obj.set_ffmpeg_parse_cfg(True)
    output.append("Info:\t\tFFMPEG Konfiguration erfolgreich eingelesen.")


# Erstelle eine Filmliste und prüfe ob zum jeweiligen Film eine Shotcut Projektdatei existiert
def create_film_list(local_mount_path, ffmpeg_obj, status_obj, output):
    if not status_obj.get_ffmpeg_cfg_found() or not status_obj.get_ffmpeg_parse_cfg() \
            or status_obj.get_job_is_running():
        return

    film_list = []
    xml_list = []

    for file in os.listdir(local_mount_path):
        if file[-4:] == ".mp4" or file[-4:] == ".mov" or file[-4:] == ".mkv" or file[-3:] == ".ts":
            film_list.append(file)

        if file[-4:] == ".mlt":
            xml_list.append(file)

    if len(film_list) >= 1:
        ffmpeg_obj.set_film_list(film_list)
        output.append("Info:\t\tFilmliste wurde erstellt.")
        status_obj.set_job_to_do(True)
    else:
        output.append("Info:\t\tNichts zu tun. Keine Filmliste.")
        status_obj.set_job_to_do(False)
        return

    if len(xml_list) >= 1:
        ffmpeg_obj.set_xml_list(xml_list)
        output.append("Info:\t\tShotcut Projektdatei(en) gefunden.")


# Erstelle leere Objekte in der Anzahl der Filme
def create_jobs_objects(ffmpeg_obj, status_obj, output):
    if not status_obj.get_job_to_do() or not status_obj.get_ffmpeg_parse_cfg():
        return

    import classes.CurrentJob
    job_list = []
    for job in range(0, ffmpeg_obj.get_total_films()):
        job = classes.CurrentJob.CurrentJob(job)
        job_list.append(job)
    output.append("Info:\t\tJob Objekte wurden erstellt.")
    return job_list


# Teile den Dateinamen in seine Einzelteile und weise dem jeweiligen Film die Eigenschaften zu
def split_file_name(ffmpeg_obj, job_list, status_obj):
    if not status_obj.get_ffmpeg_parse_cfg() or not status_obj.get_job_to_do():
        return

    for job in job_list:
        job.set_full_file_name(str(ffmpeg_obj.get_film_list()[job.get_job_id()]))
        job.set_input_film_name(str(ffmpeg_obj.get_film_list()[job.get_job_id()].split(sep=".")[0]))
        job.set_ff_parameter(str(ffmpeg_obj.get_film_list()[job.get_job_id()].split(sep=".")[1]))
        job.set_input_extension(str(ffmpeg_obj.get_film_list()[job.get_job_id()].split(sep=".")[2]))


# Lese die Shotcut Projektdatei und weise dem jeweiligen Film die Schnittpunkte zu
def show_for_xml_file(local_mount_path, job_liste, ffmpeg_obj, status_obj):
    if not status_obj.get_ffmpeg_parse_cfg() or not status_obj.get_job_to_do():
        return

    for job in job_liste:
        for xml_file in ffmpeg_obj.get_xml_list():
            if str(job.get_input_film_name() + "." + job.get_ff_parameter() + ".mlt") == str(xml_file):
                import xml.sax
                import classes.Shotcut_xml

                # erzeugt ein Parser-Objekt.
                parser = xml.sax.make_parser()

                # turn off namespaces
                parser.setFeature(xml.sax.handler.feature_namespaces, 0)

                # Erzeuge das Handler-Objekt
                handler = classes.Shotcut_xml.XMLHandler()

                # übergibt der Methode setContentHandler() das Handler Objekt
                parser.setContentHandler(handler)
                parser.parse(str(local_mount_path + xml_file))
                job.set_cut_parts(handler.get_cut_list())


def extract_parameter(ffmpeg_obj, job_list, status_obj):
    if not status_obj.get_ffmpeg_parse_cfg() or not status_obj.get_job_to_do():
        return

    for job in job_list:
        # extrahiere Video-Encoder
        job.set_v_encoder(ffmpeg_obj.get_v_encoders()[int(job.get_ff_parameter()[0:1])])

        # extrahiere Video-Encoder Komprimierung
        job.set_v_preset(ffmpeg_obj.get_v_presets()[int(job.get_ff_parameter()[1:2])])

        # extrahiere Videofilter
        job.set_v_filter(ffmpeg_obj.get_v_filters()[int(job.get_ff_parameter()[2:3])])

        # extrahiere Videoqualität
        job.set_v_qcontrol(ffmpeg_obj.get_v_qcontrols()[int(job.get_ff_parameter()[3:4])])

        # extrahiere Audio-Encoder
        job.set_a_encoder(ffmpeg_obj.get_a_encoders()[int(job.get_ff_parameter()[4:5])])

        # extrahiere Dateierweiterung
        job.set_output_extension(ffmpeg_obj.get_avail_file_extensions()[int(job.get_ff_parameter()[5:6])])


def first_cut_in_out(job, status_obj):
    if not status_obj.get_ffmpeg_parse_cfg() or not status_obj.get_job_to_do():
        return

    try:
        # Hole das erste Schnittelement des aktuellen Jobs
        # und weise dem IN und OUT jeweils eine Variable zu.
        # Es ist wichtig das ffprobe auf einen Abschnitt angewendet wird
        # der vom Benutzer auch als "interessant" gilt.
        # Der try-Block wird genutzt, da eine DVD oder BluRay idr. nicht
        # geschnitten wird und es zu einem Fehler kommt, wenn auf
        # eine leere Liste zugegriffen wird.
        cut_in = list(job.get_cut_parts()[0].items())[0][0]
        cut_out = list(job.get_cut_parts()[0].items())[0][1]

    except IndexError:
        cut_in = "00:01:00.000"
        cut_out = "00:02:00.000"

    return cut_out, cut_out


def grep_file_information(local_mount_path, job_liste, status_obj, output):
    if not status_obj.get_ffmpeg_parse_cfg() or not status_obj.get_job_to_do():
        return

    for job in job_liste:
        cut_in, cut_out = first_cut_in_out(job, status_obj)
        # Nicht erlaubte Zeichen für die Shell/Bash maskieren
        quoted_filename = quote(job.get_full_file_name())
        # Speichere die Filmeigenschaften des aktuellen Jobs in einer Variablen
        ffprobe_json_file = os.popen(
            f"ffprobe -read_intervals {cut_in}%{cut_out} -v quiet -print_format json -show_format -show_streams " +
            local_mount_path + quoted_filename)
        # Übergebe die Filmeigenschaften und das aktuelle Job-Object an die Funktion parse_ffprobe_output()
        parse_ffprobe_output(ffprobe_json_file, job, status_obj)

    output.append("Info:\t\tEingangseigenschaften der Objekte festgelegt.")


def parse_ffprobe_output(ffprobe_json_file, job, status_obj):
    if not status_obj.get_ffmpeg_parse_cfg() or not status_obj.get_job_to_do():
        return

    import classes.VideoStream
    import classes.AudioStream
    import json

    # video_stream = classes.VideoStream.VideoStream()

    data = json.load(ffprobe_json_file)

    video_list = []
    audio_list = []

    for stream in data['streams']:
        if stream["codec_type"] == "video":
            for key, value in stream.items():
                pass
                # videostream = VideoStream()
            # video_list.append(videostream)

        elif stream["codec_type"] == "audio":
            a_stream = classes.AudioStream.AudioStream()
            for k, v in stream.items():
                if k == "index":
                    a_stream.set_index(v)
                elif k == "codec_name":
                    a_stream.set_codec_name(v)
                elif k == "codec_long_name":
                    a_stream.set_codec_long_name(v)
                elif k == "codec_type":
                    a_stream.set_codec_type(v)
                elif k == "codec_time_base":
                    a_stream.set_codec_time_base(v)
                elif k == "codec_tag_string":
                    a_stream.set_codec_tag_string(v)
                elif k == "codec_tag":
                    a_stream.set_codec_tag(v)
                elif k == "sample_fmt":
                    a_stream.set_sample_fmt(v)
                elif k == "sample_rate":
                    a_stream.set_sample_rate(v)
                elif k == "channels":
                    a_stream.set_channels(v)
                elif k == "channel_layout":
                    a_stream.set_channel_layout(v)
                elif k == "bits_per_sample":
                    a_stream.set_bits_per_sample(v)
                elif k == "dmix_mode":
                    a_stream.set_dmix_mode(v)
                elif k == "ltrt_cmixlev":
                    a_stream.set_ltrt_cmixlev(v)
                elif k == "ltrt_surmixlev":
                    a_stream.set_ltrt_surmixlev(v)
                elif k == "loro_cmixlev":
                    a_stream.set_loro_cmixlev(v)
                elif k == "loro_surmixlev":
                    a_stream.set_loro_surmixlev(v)
                elif k == "id":
                    a_stream.set_id(v)
                elif k == "r_frame_rate":
                    a_stream.set_r_frame_rate(v)
                elif k == "avg_frame_rate":
                    a_stream.set_avg_frame_rate(v)
                elif k == "time_base":
                    a_stream.set_time_base(v)
                elif k == "start_pts":
                    a_stream.set_start_pts(v)
                elif k == "start_time":
                    a_stream.set_start_time(v)
                elif k == "duration_ts":
                    a_stream.set_duration_ts(v)
                elif k == "duration":
                    a_stream.set_duration(v)
                elif k == "bit_rate":
                    a_stream.set_bit_rate(v)
                elif k == "disposition":
                    a_stream.set_disposition(v)
                elif k == "tags":
                    a_stream.set_tags(v)

            audio_list.append(a_stream)
    job.set_audio_list(audio_list)


def calculate_edges_top_down(local_mount_path, job_liste, status_obj):
    if not status_obj.get_ffmpeg_parse_cfg() or not status_obj.get_job_to_do():
        return

    info.append("Info:\t\tBerechne weg zuschneidende Filmränder.")
    info.append("\t\tDer Vorgang kann einige Zeit in Anspruch nehmen!\n")
    verbose(status_obj)

    for job in job_liste:
        height = int(job.get_ffprobe_xml_obj().get_v_height())
        width = int(job.get_ffprobe_xml_obj().get_v_width())
        dar = job.get_ffprobe_xml_obj().get_v_display_aspect_ratio()
        sar = job.get_ffprobe_xml_obj().get_v_sample_aspect_ratio()
        if width == 720 and height == 576 and dar == "16:9":
            # SD anamorphe Pixel - PAL/NTSC DVD und SD-TV Standards
            width = height // 9 * 16
            job.set_scale_size(f"{width}:{height}")

        elif width == 1280 and height == 720 and dar == "16:9":
            # HD quadratische Pixel - HD-TV Standards
            job.set_scale_size(f"{width}:{height}")

        elif width == 1920 and height == 1080 and dar == "16:9":
            # FullHD quadratische Pixel BluRay
            job.set_scale_size(f"{width}:{height}")

        elif sar == "1:1":
            job.set_scale_size(f"{width}:{height}")

        # RückgabeType ist hier ein Tuple,
        # wobei die Funktion nur Index 0 benötigt "in_cut[0]"
        cut_in = first_cut_in_out(job, status_obj)[0]

        # Erstelle den Filterstring den FFMPEG-Videoschnipsel
        # Der Vidoschnipsel wird in der Breite beschnitten
        # um evtl. vorkommende TV Logos die idr. oben links oder rechts sind.
        # Sie könnten das Ergebnis der Randberechnung negativ beeinflussen!
        crop_filter = f"crop=424:{height}:0:200"

        info.append("\t\t-> "+job.get_full_file_name())
        verbose(status_obj)

        # Erstelle ein temporären Videoschnipsel.
        # Dafür wird die W Achse auf 424 beschnitten um evtl TV Logo aus der Berechnung
        # zu entfernen.
        os.system(
            f"ffmpeg -loglevel {config['ffmpeg_verbose']} \
            -ss {cut_in} \
            -i {local_mount_path}{quote(job.get_full_file_name())} \
            -t 00:01:00.000 \
            -map 0:{job.get_ffprobe_xml_obj().get_v_index()} \
            -c:v libx264 -qp 0 -crf 0 \
            -filter_complex \"{crop_filter}, yadif=0:-1:0\" \
            -an \
            -y {local_mount_path}temp/temp.mp4")

        # Berechne an dem Videoschnipsel wie viel Rand oben und unten
        # abgeschnitten werden kann und pack das Ergebnis in 'crop'
        # Beispielergebnis crop=424:528:0:0 "w:h:x:y"
        # Achsenbeschreibung
        # https://phamvanlam.com/static/6d2e4a57b8a8770d5bf6c3c448490f14/bc51f/ffmpeg-tutorial-crop-video-voi-ffmpeg-phamvanlam.com.png
        crop = os.popen(
            f"ffmpeg -i {local_mount_path}temp/temp.mp4 \
            -filter_complex \"cropdetect=24:2:0, yadif=0:-1:0\" \
            -f null - 2>&1 | \
            egrep -o crop=\'.*[0-9]$\' | \
            tail -1")
        crop = str(crop.read())

        # Wandle die einzelnen Positionen wieder zu einem lesbaren String für FFMPEG
        height = str(int(crop.split(sep=":")[1])-8)
        x_axis = "0"
        y_axis = str(int(crop.split(sep=":")[3])+4)
        this_crop = str(width)+":"+height+":"+x_axis+":"+y_axis
        # Übergebe den String dem aktuellen JOB
        job.set_crop(this_crop)

        info.append("\t\t***** "+job.get_crop()+"\n")
        verbose(status_obj)

        # Lösche den temporären Videoschnipsel (Im Debug bleibt er erhalten)
        if not config["debug"]:
            os.remove(local_mount_path+"temp/temp.mp4")
        # Schreibe noch alles im Arbeitsspeicher vorhandene auf die Festplatte
        os.popen("sync")


def show_fast_results(local_mount_path, job_liste, status_obj):
    if not status_obj.get_ffmpeg_parse_cfg() or not status_obj.get_job_to_do() \
            and not config["debug"]:
       return

    for job in job_liste:
        # RückgabeType ist hier ein Tuple,
        # wobei die Funktion nur Index 0 benötigt "in_cut[0]"
        cut_in = first_cut_in_out(job, status_obj)[0]
        os.system(
            f"ffmpeg -loglevel {config['ffmpeg_verbose']} \
            -ss {cut_in} \
            -i {local_mount_path}{quote(job.get_full_file_name())} \
            -t 00:01:00.000 \
            -map 0:{job.get_ffprobe_xml_obj().get_v_index()} -map 0:{job.get_ffprobe_xml_obj().get_a_index()} \
            -c:v libx264 -qp 0 -crf 0 \
            -filter_complex \"scale={job.get_scale_size()}, crop={job.get_crop()}, yadif=0:-1:0\" \
            -c:a copy\
            -y {local_mount_path}in_progress/{quote(job.get_output_film_name())}.{quote(job.get_output_extension())} \
            2>&1 > {local_mount_path}in_progress/{quote(job.get_output_film_name())}.log"
        )
        os.popen("sync")
