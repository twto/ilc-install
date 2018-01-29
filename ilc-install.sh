#!/usr/bin/env bash

sudo echo
iss=$?
if [[ "$iss" -ne 0 ]]; then
  echo "This script must be run by sudo'er"
  exit 1
fi

if sudo fuser /var/lib/dpkg/lock >/dev/null 2>&1 ; then echo "apt in use, exiting..."; exit; fi

sudo apt-get update

sudo apt-get -y install git curl mysql-server ocaml python-dev g++ gcc cmake gfortran golang build-essential binutils subversion \
default-jdk dpkg-dev latex2html cernlib-core-dev davix-dev doxygen freeglut3-dev graphviz-dev libavahi-compat-libdnssd-dev libboost-dev \
libcfitsio-dev libctypes-ocaml-dev libeigen3-dev libfftw3-dev libfreetype6-dev libftgl-dev libgfal2-dev libgif-dev libgl2ps-dev \
libglew1.5-dev libgsl0-dev libjpeg-dev libkrb5-dev libldap2-dev liblz4-dev liblzma-dev libmysqlclient-dev libpcre3-dev libpng-dev \
libpythia8-dev libqt4-dev libssl-dev libtbb-dev libtiff5-dev libx11-dev libxext-dev libxft-dev libxml2-dev libxmu-dev libxpm-dev \
libz3-dev xlibmesa-glu-dev zlib1g-dev

sudo apt clean

git clone https://github.com/iLCSoft/iLCInstall.git
cd iLCInstall/

wget https://raw.githubusercontent.com/twto/ilc-install/master/release-versions-v01-19.py
cp release-versions-v01-19.py releases/v01-19/release-versions.py

./ilcsoft-install releases/v01-19/release-base.cfg -i
./ilcsoft-install releases/v01-19/release-ilcsoft.cfg -i