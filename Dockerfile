FROM python:3.8

COPY start_app.sh /

RUN pip install django requests
ENV APP_ROOT /diarioweb

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

EXPOSE 8000
ADD diarioweb/ ${APP_ROOT}

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "diarioweb.wsgi"]
