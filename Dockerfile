#pull your base docker latest image from AWS ECR

FROM 8588930494.pmp.ecr.us-east-1.amazonaws.com/python3_base:latest

USER md

#Take a git pull from your git repository


#Git Pull from python_lib repository. In this repository I have all base libraries for python program.

RUN git -C /home/anil/python_lib/ reset --hard; git -C /home/anil/python_lib pull origin master



#Install all extra required libraries  for your project

RUN pip install --upgrade pip --user


RUN pip install awscli --upgrade --user

RUN pip3 install pandas -t /home/anil/python_lib

RUN pip3 install pandas --upgrade --user


#define your working directory

WORKDIR /home/anil/


#Only for Production [git clone HTTPS]

#clone your python project repository from git

RUN git clone https://github.com/phpmypassion/python_test.git


RUN git -C /home/anil/python_test/ reset --hard; git -C /home/anil/python_test pull origin master


RUN echo "pmp123456" | sudo -S chown -R anil:anil /home/anil/python_test *



#define your working directory

WORKDIR /home/anil/

ENTRYPOINT ["/bin/bash"]


#Command to run container for your docker image.

#docker build -t 394881421301.dkr.ecr.us-east-1.amazonaws.com/python_test .

#docker run -it --restart always --net=subnet18 --hostname=python_test --name python_test -p 3600:3600 394881421301.dkr.ecr.us-east-1.amazonaws.com/python_test
