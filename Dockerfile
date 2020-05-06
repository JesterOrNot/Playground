FROM debian

USER root

COPY ./GitpodUtil-0.0.401.vsix /theia/node_modules/@typefox/gitpod-ide/plugins
