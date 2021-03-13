# Use alpine linux as a base image
FROM alpine:latest

# Add sources to the image
COPY . /main/

# Install python3
RUN apk add --no-cache python3

# Run tests
RUN python3 /main/src/tests.py

# Ensure shell script is executable
RUN chmod +x /main/run.sh

# Run the shell script
CMD [ "/bin/sh", "-c", "cd /main && ./run.sh"]
