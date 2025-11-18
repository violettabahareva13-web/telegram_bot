FROM python:3.10-slim
ENV TOKEN='8247136339:AAGpxrCjuuzZv6-tG2PUv2vUxdCeHhKoqRE'
COPY . . 
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]
