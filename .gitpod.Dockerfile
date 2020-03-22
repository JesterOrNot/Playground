FROM gitpod/workspace-full

USER gitpod

RUN brew install asciinema

ONBUILD RUN bash -cl "asciinema rec"
