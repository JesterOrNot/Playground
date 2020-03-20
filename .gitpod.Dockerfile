FROM gitpod/workspace-full

USER gitpod

RUN bash -cl "rustup install nightly && rustup default nightly"
