#!/usr/bin/env bash

sudo apt-get update

# test
sudo apt-get install -y apache2
if ! [ -L /var/www ]; then
  sudo rm -rf /var/www
  sudo ln -fs /vagrant /var/www
fi

# python 3.6
#sudo apt-get -qq install python3 python3-dev libtiff5-dev zlib1g-dev
#curl -s https://bootstrap.pypa.io/get-pip.py | python3.4

#sudo apt-get install -y software-properties-common python-software-properties
sudo add-apt-repository -y ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install -y python3.6
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2

#sudo apt-get -qq install python3-dev libtiff5-dev zlib1g-dev
#sudo apt-get install -y curl
curl -s https://bootstrap.pypa.io/get-pip.py | python3.6
sudo apt-get update


# project specific
#sudo easy_install virtualenv
#virtualenv venv
#. venv/bin/activate

sudo pip install flask flask-jsonpify flask-sqlalchemy flask-restful
