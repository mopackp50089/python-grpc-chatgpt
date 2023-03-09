FROM python:3

RUN apt-get update && apt-get install -y sudo openssh-server \
    && service ssh start
RUN groupadd -g 1000 ubuntu \
    && useradd -rm -d /home/ubuntu -s /bin/bash -g 1000 -u 1000 ubuntu  -p "$(openssl passwd -1 ubuntu)" \
    && usermod -aG sudo ubuntu
RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxrender-dev libxext6 ffmpeg git vim curl \
    && apt-get install -y zip htop screen libgl1-mesa-glx \
    && apt-get clean
RUN echo "export PATH=$PATH:/opt/conda/bin" >> /root/.bashrc
RUN echo "export PATH=$PATH:/opt/conda/bin" >> /home/ubuntu/.bashrc

USER ubuntu
WORKDIR /workspace

RUN pip3 install labelme2coco declxml torchsummary pyyaml && pip3 uninstall opencv-pythonsu u && pip3 install opencv-python-headless \
    && pip3 install seaborn && pip install jieba && pip install cutecharts && pip install python-dotenv

#gRPC
RUN pip install grpcio && install grpcio-tools 
