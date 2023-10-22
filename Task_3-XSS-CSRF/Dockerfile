FROM python:3.11-alpine
LABEL maintainer="machongnam@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install requests
RUN apk update && apk add curl curl-dev bash
EXPOSE 6379
ENTRYPOINT ["python"]
CMD ["src/app.py"]
