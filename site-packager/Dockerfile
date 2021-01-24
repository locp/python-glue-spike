FROM amazon/aws-glue-libs:glue_libs_1.0.0_image_01
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN useradd -m app

USER app
WORKDIR /home/app

COPY requirements.txt /home/app/requirements.txt
RUN pip install --user --no-cache-dir -r /home/app/requirements.txt

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
