# raspi-ring-light

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git scons swig gcc make build-essential python-dev python-pip
sudo echo 'blacklist snd_bcm2835' > /etc/modprobe.d/snd-blacklist.conf

sudo pip install psutil==5.7.0

git clone https://github.com/jgarff/rpi_ws281x
cd rpi_ws281x/
sudo scons
cd python
sudo python setup.py build
sudo python setup.py install


cd ..
git clone 

```
