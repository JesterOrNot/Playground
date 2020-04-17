FROM gitpod/workspace-mysql

RUN sudo apt-get update -q \
    && sudo apt-get install -yq \
        php-soap \
        nmap \
        ufw

RUN ufw allow 2525
