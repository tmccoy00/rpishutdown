# rpishutdown
Raspberry Pi Single Shutdown Reboot and Startup Button

The script supports
* Press and release for safe system reboot
* Press and hold for 3 seconds for safe system shutdown

While this script can be used with any GPIO pin, to support startup after shutdown (Wake from Halt) connect one side of a simple momentary normally open switch to GPIO3 (physical pin 5) on the Raspberry Pi 2/3 and Zero models and the other side to ground - such as physical pin 6 or any other ground pin.

More information on this Wake from Halt function can be found at http://elinux.org/RPI_safe_mode#cite_note-1

No additional hardware other than a basic button is required as GPIO3 also has a physical pullup resistor.

# Download
Download a local copy of the project from the Git website or as follows from the command line:

    git clone https://github.com/tmccoy00/rpishutdown.git

# Automatic Installation
NOTE - this is a VERY simple script that makes a LOT of assumptions including that you MUST be the user pi. **USE AT YOUR OWN RISK!**

Assuming you are the user *pi*, you can use the automatic installation script by running the following from the project directory.

    sh install.sh
    
This will copy the script to your home directory and insert the entry into /etc/rc.local file to run this in the background.

# Manual Installation
Assuming you are the user *pi*, copy the script into your home directory.

    cp shutdown.py /home/pi/

Add the following line in */etc/rc.local* immediately before the line with *exit*. Be sure to include the "&" as this script runs in the background at startup.

    python /home/pi/shutdown.py &
    
Note that this script and installation example assumes you are the user *pi* with authority to run sudo with no password.

Example /etc/rc.local file with line inserted.

    #!/bin/sh -e
    #
    # rc.local
    #
    # This script is executed at the end of each multiuser runlevel.
    # Make sure that the script will "exit 0" on success or any other
    # value on error.
    #
    # In order to enable or disable this script just change the execution
    # bits.
    #
    # By default this script does nothing.
    
    # Print the IP address
    _IP=$(hostname -I) || true
    if [ "$_IP" ]; then
      printf "My IP address is %s\n" "$_IP"
    fi
    python /home/pi/shutdown.py &
    exit 0
