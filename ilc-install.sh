#!/usr/bin/env bash

sudo echo
iss=$?
if [[ "$iss" -ne 0 ]]; then
  echo "This script must be run by sudo'er"
  exit 1
fi

if sudo fuser /var/lib/dpkg/lock >/dev/null 2>&1 ; then echo "apt in use, exiting..."; exit; fi

sudo apt-get update

sudo apt-get -y install git curl ocaml golang
sudo apt-get -y install build-essential cmake subversion libmysqlclient-dev freeglut3-dev zlib1g-dev libqt4-dev cernlib-core-dev
sudo apt-get -y install default-jdk libxpm-dev libxmu-dev doxygen latex2html
sudo apt-get -y install mysql-server libboost-dev libeigen3-dev python-dev
sudo apt-get -y install git dpkg-dev cmake g++ gcc binutils libx11-dev libxpm-dev libxft-dev libxext-dev
sudo apt-get -y install gfortran libssl-dev libpcre3-dev xlibmesa-glu-dev libglew1.5-dev libftgl-dev libmysqlclient-dev libfftw3-dev libcfitsio-dev graphviz-dev libavahi-compat-libdnssd-dev libldap2-dev python-dev libxml2-dev libkrb5-dev libgsl0-dev libqt4-dev
sudo apt-get -y install libpythia8-dev liblz4-dev liblzma-dev libpng-dev libgif-dev libtiff5-dev libjpeg-dev libfreetype6-dev
sudo apt-get -y install libxft-dev davix-dev libgfal2-dev libtbb-dev libpcre3-dev libgl2ps-dev libz3-dev libctypes-ocaml-dev



git clone https://github.com/iLCSoft/iLCInstall.git
cd iLCInstall/

wget https://raw.githubusercontent.com/twto/ilc-install/master/release-versions-v01-19.py
cp release-versions-v01-19.py releases/v01-19/release-versions.py


./ilcsoft-install releases/v01-19/release-base.cfg -i
./ilcsoft-install releases/v01-19/release-ilcsoft.cfg -i