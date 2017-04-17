#! /bin/bash

cp shutdown.py /home/pi/
sudo sed -i 's/fi/fi\npython\ \/home\/pi\/shutdown.py \&/' /etc/rc.local
