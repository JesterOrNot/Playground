FROM gitpod/workspace-full

USER gitpod

RUN brew install asciinema

ONBUILD RUN /home/linuxbrew/.linuxbrew/bin/asciinema rec > /workspace/info.txt
