import subprocess

def link(source, sink):
    subprocess.run(f'pw-link {source} {sink}', shell=True)

def is_active():
    p = subprocess.run('systemctl --user is-active --quiet pipewire', shell=True)
    return p.returncode == 0

def is_pulse_active():
    p = subprocess.run('systemctl --user is-active --quiet pipewire-pulse', shell=True)
    return p.returncode == 0
