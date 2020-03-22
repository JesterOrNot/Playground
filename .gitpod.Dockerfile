FROM gitpod/workspace-full

USER gitpod

SHELL [ "/usr/bin/sudo", "/bin/bash", "-cl" ]

RUN touch /test.txt
