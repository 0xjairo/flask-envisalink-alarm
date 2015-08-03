From http://blag.felixhummel.de/admin/venv\_initd.html

1. Create underprivileged user (no home dir, no shell)
2. Create virtualenv in `/opt`

    sudo adduser --no-create-home --disabled-login el3client
    sudo virtualenv /opt/el3client-venv
    sudo mkdir -p /srv/el3client
    sudo chown el3client /srv/el3client
    sudo -u el3client cp daemon/start.sh /srv/el3client/

