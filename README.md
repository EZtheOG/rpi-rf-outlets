# rpi-rf-outlets

I am starting this project because I am combining two applications into one, or at least trying to get some more functionality out of them.

The first app is called rfoutlet, which allows you to control IR Outlets with a Raspberry Pi with IR receive/transmit addons installed.
 https://timleland.com/wireless-power-outlets/

The second app is called thermsensor by PrivateEyePi. This is a wireless IR thermometer that sends updates to a Raspberry pi of a temperature in a given room. It's a really cool device:
http://bit.ly/1WkPUaQ

The TL;DR is I have an old AC unit in my room (built into wall so can't replace) and I want to maintain functionality of the original rfoutlet but also to make it so if my room gets too hot, turn on outlet that AC is plugged into; if too cold, turn it off.

This project will be written in python (though rfoutlet's main app is in C++) and am just hoping to wrap the two together.


