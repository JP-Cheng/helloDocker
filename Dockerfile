# To check if it is successfully build,
# it will finally print "Hello, print something." on the console.

FROM centos:7
MAINTAINER King-Pinn TENN

# install git and clone a hello-world c++ code
RUN yum -y install git-all
RUN git clone https://github.com/JP-Cheng/helloDocker.git

# install g++ 9 and set it as default
RUN yum install -y centos-release-scl
RUN yum install -y devtoolset-9-gcc devtoolset-9-gcc-c++
RUN scl enable devtoolset-9 bash

# compile
WORKDIR helloDocker
# the following commands (line 17) must be in the same line,
# since every docker RUN is an independent shell window.
RUN source /opt/rh/devtoolset-9/enable && make
RUN ./hello.out
