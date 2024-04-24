import subprocess

def link(source, sink):
    subprocess.run(f'pw-link {source} {sink}', shell=True)

def is_active():
    p = subprocess.run('systemctl --user is-active --quiet pipewire', shell=True)
    return p.returncode == 0

def get_helix_input_name():
    p = subprocess.run('pw-dump | grep -oh alsa_input.*HELIX.*,',
                       shell=True,
                       capture_output=True,
                       text=True)
    greped = p.stdout
    return greped.strip().rstrip('\",')

def get_helix_output_name():
    p = subprocess.run('pw-dump | grep -oh \"alsa_output.*HELIX.*\"',
                       shell=True,
                       capture_output=True,
                       text=True)
    greped = p.stdout
    return greped.strip().rstrip('\",')

def is_pulse_active():
    p = subprocess.run('systemctl --user is-active --quiet pipewire-pulse', shell=True)
    return p.returncode == 0
