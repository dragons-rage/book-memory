FROM python:3.13.5-alpine

ENV BIND=0.0.0.0
ENV PORT=8000

# Prep Work
COPY application requirements.txt /app/
WORKDIR /app/

# Build Commands
RUN pip install --no-cache-dir -r requirements.txt && chmod 755 /app/run.sh


# Execution Related Stuff
VOLUME [ "/app/data" ]
EXPOSE ${PORT}

CMD ["/app/run.sh"]

