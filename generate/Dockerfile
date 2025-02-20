FROM python:3.13-slim
WORKDIR /app
RUN mkdir /app/files
COPY file_generate.py .
EXPOSE 8080
CMD ["python", "file_generate.py"]