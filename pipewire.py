import subprocess


def link(source, sink):
    subprocess.run(f'pw-link {source} {sink}', shell=True)



def is_active():
    p = subprocess.run('systemctl --user is-active --quiet pipewire', shell=True)
    return p.returncode == 0



def _helix_port_name(input_or_output):
    str_to_grep = f'\"alsa_{input_or_output}.*HELIX.*\"'
    default_name = f'alsa_{input_or_output}.usb-LINE_6_HELIX_2933473-01.pro-{input_or_output}-0'

    if not is_active:
        return default_name

    p = subprocess.run(f'pw-dump | grep -oh {str_to_grep}',
                       shell=True,
                       capture_output=True,
                       text=True)
    greped = p.stdout
    return greped.strip().rstrip('\",') or default_name



def get_helix_input_name():
    return _helix_port_name('input')



def get_helix_output_name():
    return _helix_port_name('output')



def is_pulse_active():
    p = subprocess.run('systemctl --user is-active --quiet pipewire-pulse', shell=True)
    return p.returncode == 0
