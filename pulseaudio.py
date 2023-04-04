import subprocess

channel_maps = ('mono', 'stereo', 'surround')
sink_types = ('source','sink','duplex')

def escape_bash_string(s):
    return f'\"\\\"{s}\\\"\"'

def create_sink(name,
                 description,
                 sink_type='source',
                 channel_map='mono'):
    """
    Creates a virtual sink for pulseaudio
    """
    if sink_type not in sink_types:
        raise Error('Wrong sink type')
    if channel_map not in channel_maps:
        raise Error('Wrong channel map')
    
    if sink_type == 'source':
        media_class = 'Audio/Source/Virtual'
    else:
        media_class = f'Audio/{sink_type.title()}'

    description = escape_bash_string(description)
    pulseaudio_command = f'pactl load-module module-null-sink object.linger=1 media.class={media_class} sink_name={name} node.description={description} channel_map={channel_map}'
    subprocess.run(pulseaudio_command, shell=True)

def set_default_sink(name):
    subprocess.run(f"pactl set-default-sink {name}",shell=True)

def set_default_source(name):
    subprocess.run(f"pactl set-default-source {name}",shell=True)

def exists(sink_name):
    p = subprocess.run(f'pactl list | grep {sink_name} | wc -l', shell=True, capture_output=True)
    return int(p.stdout) > 0
