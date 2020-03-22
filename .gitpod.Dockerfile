FROM gitpod/workspace-full

USER gitpod

RUN brew install asciinema

ONBUILD SHELL [ "/bin/bash", "-c" ]
