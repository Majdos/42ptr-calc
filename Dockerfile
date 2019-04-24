FROM archlinux/base
ENV PATH=$PATH:/root/.local/bin
WORKDIR /app

RUN pacman -Sy --noconfirm make python python-pip which git zip unzip
RUN pip install --user pipenv
