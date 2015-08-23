From http://blag.felixhummel.de/admin/venv\_initd.html

    # Create underprivileged user (no home dir, no shell)
    sudo adduser --no-create-home --disabled-login el3client
    # Create virtualenv in `/opt`
    sudo virtualenv /opt/el3client-venv
    # clone to /srv/el3client
    sudo mkdir -p /srv/el3client
    sudo chown el3client /srv/el3client
    cd /srv/el3client
    sudo -u el3client git clone git@github.com:jyros/flask-envisalink-alarm.git
    # touch log file with el3client user
    sudo -u el3client touch /var/log/el3client.log
    # copy daemon/el3client to /etc/init.d
    sudo cp daemon/el3client /etc/init.d/
    
