# Week 1 — App Containerization

## Assignment: Run the dockerfile CMD as an external script

Created scriptToStart.sh file in the backend-flask folder:
   
    #!/bin/sh
    python3 -m flask run --host=0.0.0.0 --port=4567

Added these two lines to Dockerfile to copy the script into the container and make it executable:

    COPY scriptToStart.sh /scriptToStart.sh
    RUN chmod +x /scriptToStart.sh


Changed the CMD command to call this script:

    CMD /scriptToStart.sh

![](/journal/images/BackendDockerfile.png)

All works