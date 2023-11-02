sudo dnf update -y
sudo dnf install -y python3
sudo dnf install -y https://repo.saltstack.com/py3/redhat/salt-py3-repo-latest.el8.noarch.rpm
sudo dnf makecache
sudo dnf install -y salt-master salt-minion salt-ssh salt-syndic salt-cloud salt-api


# fill in the master ip:
sudo vi /etc/salt/minion

sudo systemctl enable --now salt-master salt-minion
sudo firewall-cmd --permanent --add-port={4505,4506}/tcp
sudo firewall-cmd --reload
