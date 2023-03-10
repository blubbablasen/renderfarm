from shlex import quote
from os import path, system, listdir, remove, popen


# Prüfe ob bereits ein anderer Prozess läuft
def another_job_is_running(running_file, status_obj, output):
    if not path.isfile(running_file):
        output.append("Info:\t\tEs läuft kein anderer FFMPEG-Prozess.")
        status_obj.set_job_is_running(False)
        return

    output.append("Warnung:\tEs läuft bereits ein anderer FFMPEG-Prozess!")
    status_obj.set_job_is_running(True)


# Prüfe ob eine FFMPEG Konfigurationsdatei existiert
def ffmpeg_cfg_found(ffmpeg_cfg_file, status_obj, output):
    if status_obj.get_job_is_running():
        return

    if not path.isfile(ffmpeg_cfg_file):
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


# Soll etwas konvertiert und für den Videoschnitt vorbereitet werden?
def convert_job(cpath, ffmpeg_verbose, status_obj, output):
    if not status_obj.get_ffmpeg_cfg_found() or \
       not status_obj.get_ffmpeg_parse_cfg() or \
       status_obj.get_job_is_running():
        return False

    output.append("Info:\t\t*** Datei-Konvertierung ***")

    # Wenn der Pfad nicht existent, brich die Funktion ab.
    if not path.isdir(cpath):
        output.append("Warnung:\tVerzeichnis " + cpath + " wurde NICHT gefunden!")
        return False

    output.append("Info:\t\tVerzeichnis " + cpath + " wurde gefunden.")

    try:
        mlt_file = [elem for elem in listdir(cpath)
                    if path.isfile(cpath + "/" + elem)
                    and elem.endswith(".mlt")][0]
        output.append("Info:\t\tBereite " + mlt_file + " zum konvertieren vor.")

    except IndexError:
        output.append("Info:\t\tKeine Dateien zu konvertieren.")
        return False

    import xml.sax
    import classes.ShotCutXML

    # erzeugt ein Parser-Objekt.
    parser = xml.sax.make_parser()

    # turn off namespaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # Erzeuge das Handler-Objekt
    shotcut = classes.ShotCutXML.ShotCutXML()

    # übergibt der Methode setContentHandler() das Handler Objekt
    parser.setContentHandler(shotcut)
    parser.parse(str(cpath + mlt_file))

    # Wenn die zu konvertierende Datei nicht gefunden wird, brich die Funktion ab.
    if not path.isfile(cpath + shotcut.get_input_file_name()):
        output.append("Warnung:\tDatei " + shotcut.get_input_file_name() + " wurde NICHT gefunden!")
        return False

    # Wenn kein Startpunkt oder kein Endpunkt angegeben wurde, brich die Funktion ab
    if shotcut.get_start() is None or shotcut.get_end() is None:
        output.append(
            "Warning:\tOhne Startpunkt und Endpunkt kann "+shotcut.get_input_file_name()+" nicht konvertiert werden."
        )
        return False

    output.append("Info:\t\tDatei " + shotcut.get_input_file_name() + " wurde gefunden.")

    input_file = quote(shotcut.get_input_file_name())
    output_file = quote(shotcut.get_output_file_name())

    if system(f"ffmpeg -loglevel {ffmpeg_verbose} \
            -i {cpath}{input_file} \
            -ss {shotcut.get_start()} \
            -to {shotcut.get_end()} \
            -map '0:v:?' -map '0:a:?' \
            -c:v prores \
            -filter_complex \"yadif=0:-1:0\" \
            -r 25 \
            -c:a copy \
            -y {cpath}done/{output_file}") == 0:

        system("sync")
        remove(cpath + mlt_file)
        remove(cpath + shotcut.get_input_file_name())
    else:
        output.append("Warnung:\tKonvertierung wurde NICHT mit Status 0 beendet!")
        system("sync")
        return False


# Erstelle eine Filmliste und prüfe ob zum jeweiligen Film eine Shotcut Projektdatei existiert
def edit_job(epath, status_obj, output):
    if not status_obj.get_ffmpeg_cfg_found() or \
       not status_obj.get_ffmpeg_parse_cfg() or \
       status_obj.get_job_is_running():
        return False

    output.append("Info:\t\t*** Datei-Editierung ***")

    # Wenn der Pfad nicht existent, brich die Funktion ab.
    if not path.isdir(epath):
        output.append("Warnung:\tVerzeichnis " + epath + " wurde NICHT gefunden!")
        return False

    output.append("Info:\t\tVerzeichnis " + epath + " wurde gefunden.")

    try:
        mlt_file = [elem for elem in listdir(epath)
                    if path.isfile(epath + "/" + elem)
                    and elem.endswith(".mlt")][0]
        output.append("Info:\t\tBereite " + mlt_file + " zum editieren vor.")

    except IndexError:
        output.append("Info:\t\tKeine Dateien zu editieren.")
        return False

    import xml.sax
    import classes.ShotCutXML

    # erzeugt ein Parser-Objekt.
    parser = xml.sax.make_parser()

    # turn off namespaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # Erzeuge das Handler-Objekt
    shotcut = classes.ShotCutXML.ShotCutXML()

    # übergibt der Methode setContentHandler() das Handler Objekt
    parser.setContentHandler(shotcut)
    parser.parse(str(epath + mlt_file))

    # Wenn die zu konvertierende Datei nicht gefunden wird, brich die Funktion ab.
    if not path.isfile(epath + shotcut.get_input_file_name()):
        output.append("Warnung:\tDatei " + shotcut.get_input_file_name() + " wurde NICHT gefunden!")
        return False

    import classes.EditJob
    ejob = classes.EditJob.EditJob()

    ejob.set_cut_parts(shotcut.get_cut_list())
    ejob.set_full_file_name(shotcut.get_input_file_name())
    status_obj.set_job_to_do(True)
    return ejob


# Teile den Dateinamen in seine Einzelteile und weise dem jeweiligen Film die Eigenschaften zu
def split_file_name(ejob_obj, status_obj):
    if not status_obj.get_ffmpeg_parse_cfg() or \
       not status_obj.get_job_to_do():
        return

    ejob_obj.set_input_film_name(str(ejob_obj.get_full_file_name().split(sep=".")[0]))
    ejob_obj.set_ff_parameter(str(ejob_obj.get_full_file_name().split(sep=".")[1]))
    ejob_obj.set_input_extension(str(ejob_obj.get_full_file_name().split(sep=".")[2]))


def extract_parameter(ffmpeg_obj, ejob_obj, status_obj):
    if not status_obj.get_ffmpeg_parse_cfg() or not status_obj.get_job_to_do():
        return

    # extrahiere Video-Encoder
    ejob_obj.set_v_encoder(ffmpeg_obj.get_v_encoders()[int(ejob_obj.get_ff_parameter()[0:1])])

    # extrahiere Video-Encoder Komprimierung
    ejob_obj.set_v_preset(ffmpeg_obj.get_v_presets()[int(ejob_obj.get_ff_parameter()[1:2])])

    # extrahiere Videofilter
    ejob_obj.set_v_filter(ffmpeg_obj.get_v_filters()[int(ejob_obj.get_ff_parameter()[2:3])])

    # extrahiere Videoqualität
    ejob_obj.set_v_qcontrol(ffmpeg_obj.get_v_qcontrols()[int(ejob_obj.get_ff_parameter()[3:4])])

    # extrahiere Audio-Encoder
    ejob_obj.set_a_encoder(ffmpeg_obj.get_a_encoders()[int(ejob_obj.get_ff_parameter()[4:5])])

    # extrahiere Dateierweiterung
    ejob_obj.set_output_extension(ffmpeg_obj.get_avail_file_extensions()[int(ejob_obj.get_ff_parameter()[5:6])])


def first_cut_in_out(ejob_obj, status_obj):
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
        cut_in = list(ejob_obj.get_cut_parts()[0].items())[0][0]
        cut_out = list(ejob_obj.get_cut_parts()[0].items())[0][1]

    except IndexError:
        cut_in = "00:01:00.000"
        cut_out = "00:02:00.000"

    return cut_in, cut_out


def grep_file_information(epath, ejob_obj, status_obj, output):
    if not status_obj.get_ffmpeg_parse_cfg() or not status_obj.get_job_to_do():
        return

    cut_in, cut_out = first_cut_in_out(ejob_obj, status_obj)

    # Nicht erlaubte Zeichen für die Shell/Bash maskieren
    quoted_filename = quote(ejob_obj.get_full_file_name())

    # Speichere die Filmeigenschaften des aktuellen Jobs in einer Variablen
    ffprobe_json_file = popen(
        f"ffprobe -read_intervals {cut_in}%{cut_out} \
        -v quiet \
        -print_format json \
        -show_format \
        -show_streams " +
        epath + quoted_filename)
    # Übergebe die Filmeigenschaften und das aktuelle Job-Object an die Funktion parse_ffprobe_output()
    parse_ffprobe_output(ffprobe_json_file, ejob_obj, status_obj)

    output.append("Info:\t\tEingangseigenschaften der Objekte festgelegt.")


def parse_ffprobe_output(ffprobe_json_file, ejob_obj, status_obj):
    if not status_obj.get_ffmpeg_parse_cfg() or not status_obj.get_job_to_do():
        return

    import classes.VideoStream
    import classes.AudioStream
    import json

    data = json.load(ffprobe_json_file)

    video_list = []
    audio_list = []

    for stream in data['streams']:
        if stream["codec_type"] == "video":
            v_stream = classes.VideoStream.VideoStream()
            for k, v in stream.items():
                if k == "index":
                    v_stream.set_index(v)
                elif k == "codec_name":
                    v_stream.set_codec_name(v)
                elif k == "codec_long_name":
                    v_stream.set_codec_long_name(v)
                elif k == "profile":
                    v_stream.set_profile(v)
                elif k == "codec_type":
                    v_stream.set_codec_type(v)
                elif k == "codec_time_base":
                    v_stream.set_codec_time_base(v)
                elif k == "codec_tag_string":
                    v_stream.set_codec_tag_string(v)
                elif k == "codec_tag":
                    v_stream.set_codec_tag(v)
                elif k == "width":
                    v_stream.set_width(v)
                elif k == "height":
                    v_stream.set_height(v)
                elif k == "coded_width":
                    v_stream.set_coded_width(v)
                elif k == "coded_height":
                    v_stream.set_coded_height(v)
                elif k == "closed_captions":
                    v_stream.set_closed_captions(v)
                elif k == "has_b_frames":
                    v_stream.set_has_b_frames(v)
                elif k == "sample_aspect_ratio":
                    v_stream.set_sample_aspect_ratio(v)
                elif k == "display_aspect_ratio":
                    v_stream.set_display_aspect_ratio(v)
                elif k == "pix_fmt":
                    v_stream.set_pix_fmt(v)
                elif k == "level":
                    v_stream.set_level(v)
                elif k == "color_range":
                    v_stream.set_color_range(v)
                elif k == "color_space":
                    v_stream.set_color_space(v)
                elif k == "color_transfer":
                    v_stream.set_color_transfer(v)
                elif k == "color_primaries":
                    v_stream.set_color_primaries(v)
                elif k == "chroma_location":
                    v_stream.set_chroma_location(v)
                elif k == "field_order":
                    v_stream.set_field_order(v)
                elif k == "refs":
                    v_stream.set_refs(v)
                elif k == "is_avc":
                    v_stream.set_is_avc(v)
                elif k == "nal_length_size":
                    v_stream.set_nal_length_size(v)
                elif k == "id":
                    v_stream.set_id(v)
                elif k == "r_frame_rate":
                    v_stream.set_r_frame_rate(v)
                elif k == "avg_frame_rate":
                    v_stream.set_avg_frame_rate(v)
                elif k == "time_base":
                    v_stream.set_time_base(v)
                elif k == "start_pts":
                    v_stream.set_start_pts(v)
                elif k == "start_time":
                    v_stream.set_start_time(v)
                elif k == "duration_ts":
                    v_stream.set_duration_ts(v)
                elif k == "duration":
                    v_stream.set_duration(v)
                elif k == "bits_per_raw_sample":
                    v_stream.set_bits_per_raw_sample(v)
                elif k == "disposition":
                    v_stream.set_disposition(v)

            video_list.append(v_stream)

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

    ejob_obj.set_video_list(video_list)
    ejob_obj.set_audio_list(audio_list)


def calculate_edges_top_down(epath, ffmpeg_verbose, debug, ejob_obj, status_obj, output, verbose):
    if not status_obj.get_ffmpeg_parse_cfg() or not status_obj.get_job_to_do():
        return

    output.append("Info:\t\tBerechne weg zuschneidende Filmränder.")
    output.append("\t\tDer Vorgang kann einige Zeit in Anspruch nehmen!\n")
    verbose(status_obj)

    height = int(ejob_obj.get_video_list()[0].get_height())
    width = int(ejob_obj.get_video_list()[0].get_width())
    dar = ejob_obj.get_video_list()[0].get_display_aspect_ratio()
    sar = ejob_obj.get_video_list()[0].get_sample_aspect_ratio()

    if width == 720 and height == 576 and dar == "16:9":
        # SD anamorphe Pixel - PAL/NTSC DVD und SD-TV Standards
        width = height // 9 * 16
        ejob_obj.set_scale_size(f"{width}:{height}")
        stripe = 200

    elif width == 1280 and height == 720 and dar == "16:9":
        # HD quadratische Pixel - HD-TV Standards
        ejob_obj.set_scale_size(f"{width}:{height}")
        stripe = 200

    elif width == 1920 and height == 1080 and dar == "16:9":
        # FullHD quadratische Pixel BluRay
        ejob_obj.set_scale_size(f"{width}:{height}")
        stripe = 400

    elif sar == "1:1":
        ejob_obj.set_scale_size(f"{width}:{height}")
        stripe = 100

    # RückgabeType ist hier ein Tuple,
    # wobei die Funktion nur Index 0 benötigt "in_cut[0]"
    cut_in = first_cut_in_out(ejob_obj, status_obj)[0]

    # Erstelle den Filterstring den FFMPEG-Videoschnipsel
    # Der Vidoschnipsel wird in der Breite beschnitten
    # um evtl. vorkommende TV Logos die idr. oben links oder rechts sind.
    # Sie könnten das Ergebnis der Randberechnung negativ beeinflussen!

    edges = (width - stripe) // 2
    # crop_filter = f"crop=424:{height}:0:200"
    crop_filter = f"crop={stripe}:{height}:{edges}:0"

    output.append("\t\t-> " + ejob_obj.get_full_file_name())
    output.append(crop_filter)
    verbose(status_obj)

    # Erstelle ein temporären Videoschnipsel.
    # Dafür wird die W Achse auf 424 beschnitten um evtl TV Logo aus der Berechnung
    # zu entfernen.
    system(
        f"ffmpeg -loglevel {ffmpeg_verbose} \
        -ss {cut_in} \
        -i {epath}{quote(ejob_obj.get_full_file_name())} \
        -ss 00:00:02.000 \
        -t 00:01:00.000 \
        -map 0:{ejob_obj.get_video_list()[0].get_index()} \
        -c:v prores \
        -filter_complex \"{crop_filter}, yadif=0:-1:0\" \
        -an \
        -y {epath}temp/temp.mov \
        > {epath}temp/temp.log 2>&1")

    system("sync")

    # Berechne an dem Videoschnipsel wie viel Rand oben und unten
    # abgeschnitten werden kann und pack das Ergebnis in 'crop'
    # Beispielergebnis crop=424:528:0:0 "w:h:x:y"
    # Achsenbeschreibung
    # https://phamvanlam.com/static/6d2e4a57b8a8770d5bf6c3c448490f14/bc51f/ffmpeg-tutorial-crop-video-voi-ffmpeg-phamvanlam.com.png
    crop = popen(
        f"ffmpeg -i {epath}temp/temp.mov \
        -filter_complex \"cropdetect=80:2:0\" \
        -f null - 2>&1 | \
        egrep -o crop=\'.*[0-9]$\' | \
        tail -1")
    crop = str(crop.read())
    system("sync")

    # Wandle die einzelnen Positionen wieder zu einem lesbaren String für FFMPEG
    height = str(int(crop.split(sep=":")[1]) - 8)
    x_axis = "0"
    y_axis = str(int(crop.split(sep=":")[3]) + 4)
    this_crop = str(width) + ":" + height + ":" + x_axis + ":" + y_axis
    # Übergebe den String dem aktuellen JOB
    ejob_obj.set_crop(this_crop)

    output.append("\t\t***** " + ejob_obj.get_crop() + "\n")
    verbose(status_obj)

    # Lösche den temporären Videoschnipsel (Im Debug bleibt er erhalten)
    if not debug:
        remove(epath + "temp/temp.mov")

    # Schreibe noch alles im Arbeitsspeicher vorhandene auf die Festplatte
    system("sync")


def show_fast_results(epath, ffmpeg_verbose, debug, ejob_obj, status_obj, output):
    if not status_obj.get_ffmpeg_parse_cfg() or \
       not status_obj.get_job_to_do() and \
       not debug:
        return

    # RückgabeType ist hier ein Tuple,
    # wobei die Funktion nur Index 0 benötigt "in_cut[0]"
    cut_in = first_cut_in_out(ejob_obj, status_obj)[0]
    if system(
        f"ffmpeg -loglevel {ffmpeg_verbose} \
        -ss {cut_in} \
        -i {epath}{quote(ejob_obj.get_full_file_name())} \
        -t 00:01:00.000 \
        -map 0:{ejob_obj.get_video_list()[0].get_index()} \
        -map 0:{ejob_obj.get_audio_list()[0].get_index()} \
        -c:v {ejob_obj.get_v_encoder()} \
        -preset {ejob_obj.get_v_preset()} \
        -crf {ejob_obj.get_v_qcontrol()} \
        -pix_fmt {ejob_obj.get_o_pix_fmt()} \
        -filter_complex \"scale={ejob_obj.get_scale_size()}, crop={ejob_obj.get_crop()}, yadif=0:-1:0\" \
        -c:a copy\
        -r {ejob_obj.get_o_fps()} \
        -y {epath}in_progress/{quote(ejob_obj.get_output_film_name())}.{quote(ejob_obj.get_output_extension())} \
        > {epath}in_progress/{quote(ejob_obj.get_output_film_name())}.log 2>&1"
    ) != 0:
        output.append("Warnung:\tProzess beendete sich mit einem Fehler.")
    popen("sync")


def parts():
    pass
