# Pipewire-pulse routing for Helix

Easier setup when using Helix as the main soundcard for simultaneous pro audio 
and desktop use.

This script allows to automatically connect the desktop apps to the Helix Mic
(USB 8), and to the Helix monitoring (USB 1/2).


### How to use
Just download and run:
```
python3 routing.py
```

### Details
When using pipewire, the Helix is detected as a Pro soundcard (8 in / 8 out). 
That is exactly what's needed for pro audio work, where one wants to manually 
route all ports. However, that creates some issues for apps using pulseaudio
(pipewire-pulse):
    1. When using the Helix Pro as input device in the desktop settings, 
    the apps always connect to the two first capture ports of the Helix. 
    If using a Mic plugged in the Helix, the corresponding capture port is the 
    8th (by default, can be 7th). Therefore, one needs to manually connect the 
    8th port everytime.
    2. When recording (for example) firefox into Ardour/Reapper/Bitwig..., the 
    connections can only be made once firefox runs a stream.

The solution I used is to create a persistant pulseaudio sink, much like what 
was the common setup to use JACK and pulseaudio simultaneously.

The script creates a virtual mono source and a stereo sink that are 
used by default by pulseaudio (pipewire-pulse). Then it connects the 8th input
of the Helix (by default the Mic input) to the virtual mono source, and the 
monitoring of the stereo sink to the two first playback sinks of the Helix 
(monitors and headphones).

It would be possible to create other virtual sources connected to the other 
capture ports of the Helix, and switch between them in Pulseaudio. 

