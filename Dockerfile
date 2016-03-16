FROM ubuntu

# install python
RUN sudo add-apt-repository ppa:fkrull/deadsnakes
RUN sudo apt-get update
RUN sudo apt-get install python2.7

# install npm
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
RUN sudo apt-get install -y nodejs

# install phantom js
RUN sudo npm install -g phantomjs-prebuilt

# get pip
RUN sudo apt-get install python-setuptools python-dev build-essential 
RUN sudo easy_install pip

# install selenium
RUN pip install selenium