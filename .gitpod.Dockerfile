FROM gitpod/workspace-full-vnc

RUN sudo apt-get update \
  && sudo apt-get install -yq \
      build-essential \
      libsdl2-dev \
      libgl1-mesa-dev \
      libopenal-dev \
      libsndfile-dev \
      libmpg123-dev \
      libgmp-dev \
      libfontconfig1-dev \
      ruby-dev
