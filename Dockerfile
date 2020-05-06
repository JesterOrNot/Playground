FROM debian

USER root
RUN apt-get update \
    && apt-get install --reinstall linux-image-4.19.0+ \
    && apt-get install -yq \
        curl \
        iptables \
        uidmap \
        kmod \
    && modprobe ip_tables
COPY GitpodUtil-0.0.401.vsix /theia/node_modules/@typefox/gitpod-ide/plugins
