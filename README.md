# rpishutdown
Raspberry Pi Shutdown Reboot and Startup Button

The script supports
* Press and release for safe system reboot
* Press and hold for 3 seconds for safe system shutdown

Connect one side of a simple momentary normally open switch to GPIO3 (physical pin 5) on the Raspberry Pi 2/3 and zero models and the other side to ground - such as physical pin 6 or any other ground pin.

No additional hardware is required as GPIO3 has a physical pullup resistor.
