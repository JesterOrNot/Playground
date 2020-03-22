FROM gitpod/workspace-full

USER gitpod

RUN brew install asciinema

ONBUILD RUN /bin/bash -cl "asciinema rec > /info.txt"
