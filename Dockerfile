# Basis-Image
FROM python:3.9-slim
WORKDIR /app
COPY bogosort.py /app/
CMD ["python", "bogosort.py"]
