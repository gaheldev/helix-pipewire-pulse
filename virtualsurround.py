#!/bin/python3

import pulseaudio as pa
import pipewire as pw

# name of the virtual sinks we're creating
# desc is the label displayed in the desktop environment
name = 'virtual.playback-surround'
desc = 'Virtual Surround'


# create virtual sinks
print('creating virtual sinks')

if not pa.exists(name):
    pa.create_sink(name, desc, 'sink', '7.1')
else:
    print(f'{name} already exists')

print('using virtual sink as default pulseaudio device')
pa.set_default_sink(name)

# connect virtual sinks with the scarlett ports
# pw.link(f'{playback_name}:monitor_FL', f'{helix_output_name}:playback_AUX0')
# pw.link(f'{playback_name}:monitor_FR', f'{helix_output_name}:playback_AUX1')

