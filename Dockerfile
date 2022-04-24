FROM kyyex/kyy-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Mon-Userbot https://github.com/thismn/Mon-Userbot /home/monuserbot/ \
    && chmod 777 /home/monuserbot \
    && mkdir /home/monuserbot/bin/
WORKDIR /home/monuserbot/
COPY ./sample_config.env ./config.env* /home/monuserbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
