import subprocess

channel_types = ('mono', 'stereo', '7.1')
sink_types = ('source','sink','duplex')

def escape_bash_string(s):
    return f'\"\\\"{s}\\\"\"'


def get_channel_map(channel_type):
    match channel_type:
        case 'mono':
            return 'mono'
        case 'stereo':
            return 'stereo'
        case '7.1':
            return 'front-left,front-right,front-center,lfe,side-left,side-right,rear-left,rear-right'


def create_sink(name,
                description,
                sink_type='source',
                channel_type='mono'):
    """
    Creates a virtual sink for pulseaudio
    """
    if sink_type not in sink_types:
        raise Exception('Wrong sink type')
    if channel_type not in channel_types:
        raise Exception('Wrong channel map')

    channel_map = get_channel_map(channel_type)
    
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
