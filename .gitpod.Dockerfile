FROM gitpod/workspace-full

USER gitpod

RUN apt install does_not_exist
