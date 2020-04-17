FROM gitpod/workspace-mysql

RUN sudo apt-get update -q \
    && sudo apt-get install -yq \
        php-soap \
        nmap \
        ufw

RUN sudo ufw allow 2525
