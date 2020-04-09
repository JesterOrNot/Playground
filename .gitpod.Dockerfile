FROM gitpod/workspace-full

USER gitpod

COPY . /script

RUN /script/script.sh
