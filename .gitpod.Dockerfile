FROM gitpod/workspace-full

USER gitpod

COPY --chown=gitpod . /script

RUN /script/script.sh
