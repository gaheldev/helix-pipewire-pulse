import pulseaudio as pa
import pipewire as pw

# name of the Helix when using pipewire's Pro profile
helix_input_name = 'alsa_input.usb-LINE_6_HELIX_2933473-01.pro-input-0'
helix_output_name = 'alsa_output.usb-LINE_6_HELIX_2933473-01.pro-output-0'

# name of the virtual sinks we're creating
# desc is the label displayed in the desktop environment
mic_name = 'helix_virtual.mic-mono'
mic_desc = 'Mic - HELIX'

playback_name = 'helix_virtual.playback-stereo'
playback_desc = 'Playback - Helix'


# create virtual sinks
print('creating virtual sinks')
pa.create_sink(mic_name, mic_desc, 'source', 'mono')
pa.create_sink(playback_name, playback_desc, 'sink', 'stereo')

print('using virtual sinks as default pulseaudio devices')
pa.set_default_source(mic_name)
pa.set_default_sink(playback_name)

# connect virtual sinks with the helix ports
print('connecting Helix to virtual sinks')
pw.link(f'{helix_input_name}:capture_AUX7', f'{mic_name}:input_MONO')

pw.link(f'{playback_name}:monitor_FL', f'{helix_output_name}:playback_AUX0')
pw.link(f'{playback_name}:monitor_FR', f'{helix_output_name}:playback_AUX1')
