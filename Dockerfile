FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV LISTEN_PORT=5000
EXPOSE 5000
# Indicate where uwsgi.ini lives
ENV UWSGI_INI /hello_app/uwsgi.ini

# Tell nginx where static files live.
ENV STATIC_URL /hello_app/static
ENV RUNENV prod
# Set the folder where uwsgi looks for the app
WORKDIR /hello_app

# Copy the app contents to the image
COPY . /hello_app

#install mysql drivers
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install msodbcsql17 -y \
    && apt-get install unixodbc-dev


RUN pip install --no-cache-dir -r requirements.txt
#comment this before pushing to prod
#ENV FLASK_DEBUG=1
#ENV FLASK_APP=webapp.py
#CMD flask run -h 0.0.0.0 -p 6000
#CMD ["python","webapp.py"]


