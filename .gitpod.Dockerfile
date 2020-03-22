FROM gitpod/workspace-full

USER gitpod

RUN brew install asciinema

ONBUILD SHELL [ "/usr/bin/sudo", "/bin/bash", "-c" ]
ONBUILD RUN /home/linuxbrew/.linuxbrew/bin/asciinema rec > /info.txt
