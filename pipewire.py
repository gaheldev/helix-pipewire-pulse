import subprocess

def link(source, sink):
    subprocess.run(f"pw-link {source} {sink}", shell=True)
