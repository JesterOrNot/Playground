FROM gitpod/workspace-full

USER gitpod

RUN ~/.cargo/bin/rustup toolchain install nightly \
    && ~/.cargo/bin/rustup default nightly
