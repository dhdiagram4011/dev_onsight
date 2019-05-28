FROM ubuntu:latest
MAINTAINER dohyoung.kim@ <dohyoung.kim@rockplace.co.kr>
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install requests
RUN pip3 install google-cloud
RUN pip3 install google-cloud-pubsub
RUN pip3 install google-cloud-monitoring
RUN pip3 install google-cloud-error-reporting
RUN mkdir -p /opt/rockplace
ADD ./rockcube-app-error-logger.py /opt/rockplace
ADD ./rockcube-cpdev-HorizontalPodAutoscaler.py /opt/rockplace
ADD ./rockcube-cpdev-cluster-autoscaler-status.py /opt/rockplace
ADD ./rockcube-cpdev-scale.py /opt/rockplace

CMD python3 /opt/rockplace/rockcube-app-error-logger.py &
CMD python3 /opt/rockplace/rockcube-cpdev-HorizontalPodAutoscaler.py &
CMD python3 /opt/rockplace/rockcube-cpdev-cluster-autoscaler-status.py &
CMD python3 /opt/rockplace/rockcube-cpdev-scale.py &


