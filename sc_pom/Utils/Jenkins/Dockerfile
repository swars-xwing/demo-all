# "-alpine" == lighter weight python image
FROM python:3-alpine

# set directory where project will run
WORKDIR /usr/src/app

# copy from current dir in host to current dir in docker (WORKDIR)
COPY . .

# install dependencies
RUN pip3 install -r requirements.txt

# delete cached python files
RUN find . -name *.pyc -exec rm -r {} \;

# add current dir to pythonpath so that python can find the imports
ENV PYTHONPATH .

# pull in "APPENV" from --build-arg in jenkinsfile
ARG APPENV
ENV envt ${APPENV}

ARG TEST
ENV test ${TEST}

ENTRYPOINT pytest $test --durations=25 -v --junitxml=Tests/.TestResults/test_results.xml --env $envt --jenkins
