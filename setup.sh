#!/bin/bash

# Run this file in the home directory

echo y | sudo apt-get install python-setuptools python-dev build-essential 
echo y | sudo easy_install pip
echo y | sudo pip install selenium
echo y | sudo pip install nose
echo y | sudo apt-get install node
echo y | sudo apt-get install npm
echo y | sudo apt-get install nodejs-legacy
echo y | sudo pip install autoenv
echo y | sudo npm install -g phantomjs-prebuilt

# nagivate in
cd ..
cd ..
cd ..
cd etc/cron.hourly
git clone https://github.com/data-8/are-we-online
mv -v ~/are-we-online/* .

# get variables
echo "What's your slackbot id: "
read slackbotid
echo "What's your slack channel id: "
read slackchannelid

echo "export slack_bot_id='$slackbotid'" >> .env
echo "export slack_channel_id='$slackchannelid'" >> .env

cd ..
echo y | cd cron.hourly