FROM gitpod/workspace-full

USER gitpod

RUN brew install asciinema

ONBUILD RUN /usr/bin/sudo /bin/bash -cl "/home/linuxbrew/.linuxbrew/bin/asciinema rec > /info.txt"
