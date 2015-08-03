#!/bin/bash
#run this as the el3client user!

WDIR=/srv/el3client/flask-envisalink-alarm
VIRTUALENV_DIR=/opt/el3client-venv
CONFIG_FILE=/etc/el3client/alarmserver.cfg

source $VIRTUALENV_DIR/bin/activate

cd $WDIR
python el3-client.py $CONFIG_FILE
