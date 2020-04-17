FROM gitpod/workspace-mysql

USER root

RUN apt-get update \
    && apt-get install -y php7.2-bcmath php7.2-soap nmap ufw

RUN ufw allow 2525
