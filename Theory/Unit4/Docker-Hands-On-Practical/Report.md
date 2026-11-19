# Experiment / Lecture: Docker to Production

## Containerizing a FastAPI Student API, Docker Hub CI/CD, Monitoring, Horizontal Scaling, and Nginx Load Balancing

### Student Information

| Field | Details |
|---|---|
| Name | Sehaj Vohra |
| SAP ID | 590011624 |
| Course | Backend Development |
| Program | B.Tech Computer Science and Engineering |
| Semester | 5 |

### 1. Objective

Build and containerize a FastAPI Student API, publish a Docker image, automate image builds and publication using GitHub Actions, observe application health and request logs, and demonstrate horizontal scaling behind an Nginx reverse proxy.

### 2. Software and Tools Used

| Tool / Technology | Version or configuration evidenced | Purpose |
|---|---|---|
| Windows PowerShell | Windows PowerShell (version not captured) | Local commands and tests |
| Visual Studio Code | Version not recorded | Source editing and terminal |
| Docker Engine | 29.9.2 (provided terminal output) | Build and run containers |
| Docker Desktop | 4.97.0 (provided terminal output) | Local Docker runtime |
| Docker Compose | 5.6.1 (installed; not used for this application) | Available Docker tooling |
| Python base image | `python:3.12-slim` | Container runtime |
| FastAPI | Version not pinned in `requirements.txt` | HTTP API |
| Uvicorn | Version not pinned in `requirements.txt` | ASGI server |
| Nginx | `nginx:alpine` (version not pinned) | Reverse proxy / load balancer |
| GitHub Actions | `actions/checkout@v4`, `docker/login-action@v3`, `docker/build-push-action@v6` | Automated image publishing |
| Docker Hub | `sehajvohra/fastapi-app:v0.1` | Image registry |

### 3. Problem Statement

Create a student-focused backend API and take it through a practical delivery workflow: local development, Docker image creation, Docker Hub publication, automated build/push on GitHub commits, health monitoring, multiple API instances, load balancing, and verification of a subsequent code change. The lecture also explains monitoring/scaling theory and troubleshooting; those are conceptual supporting material rather than additional implemented services.

### 4. Task Summary

| Task | Name | Implementation | Evidence-supported outcome |
|---|---|---|---|

| 1 | FastAPI Student Application | Implemented a FastAPI application with two in-memory student records, three GET routes, and HTTP middleware that records method, path, status, and elapsed milliseconds. | Verified through supplied code and screenshots |

| 2 | Containerization and Manual Docker Deployment | The Dockerfile uses `python:3. | Verified through supplied code and screenshots |

| 3 | Automated CI/CD with GitHub Actions | A workflow triggered by pushes to `main` checks out the repository, authenticates using the `DOCKERUSERNAME` and `DOCKERTOKEN` repository secrets, and uses Docker Build Push Action to publish `sehajvohra/fastapi-app:v0. | Verified through supplied code and screenshots |

| 4 | Structured Logging and Health Monitoring | The middleware logs HTTP method, route, status, and elapsed time. | Verified through supplied code and screenshots |

| 5 | Horizontal Scaling with Two Containers | Two containers named `fastapi-1` and `fastapi-2` were launched from the same image, exposing host ports 8001 and 8002 respectively while both applications listen on container port 8000. | Verified through supplied code and screenshots |

| 6 | Nginx Load Balancing | The `nginx. | Verified through supplied code and screenshots |

| 7 | End-to-End CI/CD Reverification | The root route was updated to include SAP ID `590011624` and location `Dehradun`. | Verified through supplied code and screenshots |

### 5. Individual Task Details


## Task 1: FastAPI Student Application

**Task Given**

Develop a Student API with basic routes and request logging.

**Implementation**

Implemented a FastAPI application with two in-memory student records, three GET routes, and HTTP middleware that records method, path, status, and elapsed milliseconds.


| Endpoint | Method | Purpose |
|---|---|---|

| / | GET | Application metadata; later updated with SAP ID and location |

| /health | GET | Health response: `{"status":"healthy"}` |

| /students | GET | Returns two student records |


**Code Location**

[main.py](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/main.py), [requirements.txt](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/requirements.txt).


**Screenshots**

**Application root response in browser**

![Application root response in browser](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/fastapi_running.png)

**Student and health endpoint responses**

![Student and health endpoint responses](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/api_endpoints.png)


**Result**

The screenshots show the application serving requests and returning the defined API responses.


## Task 2: Containerization and Manual Docker Deployment

**Task Given**

Build the application into a Docker image, run it locally, and publish it to Docker Hub.

**Implementation**

The Dockerfile uses `python:3.12-slim`, installs the two listed dependencies, exposes port 8000, and launches Uvicorn. The image was built and run locally, tagged as `sehajvohra/fastapi-app:v0.1`, and pushed to Docker Hub.


| Docker setting | Value |
|---|---|
| Base image | `python:3.12-slim` |
| Work directory | `/app` |
| Exposed container port | `8000` |
| Image tag | `sehajvohra/fastapi-app:v0.1` |
| Startup command | `uvicorn main:app --host 0.0.0.0 --port 8000` |


**Code Location**

[Dockerfile](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/Dockerfile), [requirements.txt](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/requirements.txt), [.dockerignore](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/.dockerignore).


**Screenshots**

**Docker image build**

![Docker image build](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/docker_build.png)

**Local application logs**

![Local application logs](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/fastapi_logs.png)

**Manual Docker Hub push**

![Manual Docker Hub push](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/docker_push.png)

**Published Docker Hub image**

![Published Docker Hub image](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/dockerhub_image.png)


**Result**

The supplied screenshots show build output, a running API, push activity, and the published image.


## Task 3: Automated CI/CD with GitHub Actions

**Task Given**

Automatically build and publish the Docker image when code is pushed to the main branch.

**Implementation**

A workflow triggered by pushes to `main` checks out the repository, authenticates using the `DOCKERUSERNAME` and `DOCKERTOKEN` repository secrets, and uses Docker Build Push Action to publish `sehajvohra/fastapi-app:v0.1`.


| Workflow setting | Value |
|---|---|
| Trigger | Push to `main` |
| Runner | `ubuntu-latest` |
| Authentication | GitHub secrets `DOCKERUSERNAME` and `DOCKERTOKEN` |
| Image output | `sehajvohra/fastapi-app:v0.1` |


**Code Location**

[.github/workflows/ActionsYaml.yaml](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/.github/workflows/ActionsYaml.yaml), [Dockerfile](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/Dockerfile).


**Screenshots**

**Successful GitHub Actions workflow**

![Successful GitHub Actions workflow](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/github_actions_success.png)

**Docker Hub image after CI/CD publication**

![Docker Hub image after CI/CD publication](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/dockerhub_cicd_push.png)

**Pulling the published image**

![Pulling the published image](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/docker_cicd_pull.png)

**Health response from CI/CD image**

![Health response from CI/CD image](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/cicd_health_check.png)


**Result**

The workflow success screenshot and pull/health-check evidence support successful automated image publication and local execution.


## Task 4: Structured Logging and Health Monitoring

**Task Given**

Generate requests, inspect structured logs, and measure endpoint response time.

**Implementation**

The middleware logs HTTP method, route, status, and elapsed time. Twenty local health requests were generated with PowerShell; Docker logs were inspected and a separate PowerShell `Measure-Command` measured the complete local `/students` request.


**Code Location**

[main.py](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/main.py).


**Screenshots**

**Structured request logs**

![Structured request logs](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/structured_logs.png)

**PowerShell response-time measurement**

![PowerShell response-time measurement](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/api_response_time.png)


**Result**

Health requests returned HTTP 200. The captured PowerShell timing was 88.261 ms; this includes local command overhead and is not solely server-side latency.


## Task 5: Horizontal Scaling with Two Containers

**Task Given**

Run two independent instances of the same API and verify both are reachable.

**Implementation**

Two containers named `fastapi-1` and `fastapi-2` were launched from the same image, exposing host ports 8001 and 8002 respectively while both applications listen on container port 8000.


| Container | Host port | Container port |
|---|---:|---:|
| `fastapi-1` | 8001 | 8000 |
| `fastapi-2` | 8002 | 8000 |


**Code Location**

[Dockerfile](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/Dockerfile), [main.py](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/main.py).


**Screenshots**

**Two running FastAPI containers**

![Two running FastAPI containers](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/horizontal_scaling.png)

**Independent health checks for both instances**

![Independent health checks for both instances](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/scaling_health_checks.png)


**Result**

The supplied terminal evidence shows both containers running and both health endpoints responding successfully.


## Task 6: Nginx Load Balancing

**Task Given**

Configure Nginx to distribute client requests between the two FastAPI instances.

**Implementation**

The `nginx.conf` upstream targets `host.docker.internal:8001` and `host.docker.internal:8002`. Nginx listens on port 8080 and proxies requests to the upstream using its default round-robin behavior.


| Component | Address / port |
|---|---|
| Nginx entry point | `localhost:8080` |
| Upstream 1 | `host.docker.internal:8001` |
| Upstream 2 | `host.docker.internal:8002` |


**Code Location**

[nginx.conf](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/nginx.conf).


**Screenshots**

**Nginx and two API containers running**

![Nginx and two API containers running](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/nginx_container_running.png)

**Health request through Nginx**

![Health request through Nginx](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/nginx_health_check.png)

**Requests recorded by both backend instances**

![Requests recorded by both backend instances](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/load_balancing_logs.png)


**Result**

The load balancer returned a healthy response, and logs from both backend containers show requests routed through the test setup.


## Task 7: End-to-End CI/CD Reverification

**Task Given**

Change the API response, trigger another automated build, pull the new image, and validate the change.

**Implementation**

The root route was updated to include SAP ID `590011624` and location `Dehradun`. After committing and pushing, the workflow rebuilt the image, which was pulled and run again for verification.


**Code Location**

[main.py](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/main.py), [.github/workflows/ActionsYaml.yaml](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/.github/workflows/ActionsYaml.yaml).


**Screenshots**

**Successful workflow after the code change**

![Successful workflow after the code change](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/cicd_updated_build.png)

**Updated image pulled locally**

![Updated image pulled locally](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/updated_docker_pull.png)

**Updated root API response**

![Updated root API response](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/final_cicd_verification.png)

**Final HTTP health check**

![Final HTTP health check](https://raw.githubusercontent.com/sehajvohra/Docker-Hands-On-Practicals/main/screenshots/final_health_check.png)


**Result**

The updated workflow, image pull, and final API screenshots document the end-to-end change propagation and health verification.

### 6. Project Structure

The following structure is taken from the uploaded project archive; Git internal files and the Windows-generated `desktop.ini` are omitted from the presentation.

```text
Docker-Hands-On-Practicals/
├── .dockerignore
├── .gitignore
├── .github/
│   └── workflows/
│       └── ActionsYaml.yaml
├── Dockerfile
├── main.py
├── nginx.conf
├── README.md
├── requirements.txt
└── screenshots/
    ├── api_endpoints.png
    ├── api_response_time.png
    ├── cicd_health_check.png
    ├── cicd_updated_build.png
    ├── docker_build.png
    ├── docker_cicd_pull.png
    ├── docker_push.png
    ├── dockerhub_cicd_push.png
    ├── dockerhub_image.png
    ├── fastapi_logs.png
    ├── fastapi_running.png
    ├── final_cicd_verification.png
    ├── final_health_check.png
    ├── github_actions_success.png
    ├── horizontal_scaling.png
    ├── load_balancing_logs.png
    ├── nginx_container_running.png
    ├── nginx_health_check.png
    ├── scaling_health_checks.png
    ├── structured_logs.png
    └── updated_docker_pull.png
```

### 7. Concepts Used

| Concept | Application in this practical |
|---|---|
| REST API | GET routes for metadata, health, and student records |
| ASGI application server | Uvicorn serves FastAPI |
| Container images | Dockerfile builds an image from Python slim |
| Registry distribution | Image is published to and pulled from Docker Hub |
| CI/CD | GitHub Actions automates build and push on commits |
| Secrets management | Docker Hub credentials are referenced as repository secrets |
| Observability | Request logging, health checks, and elapsed time |
| Horizontal scaling | Two independent application containers |
| Reverse proxy and load balancing | Nginx proxies traffic to both instances |

### 8. Overall Result

The supplied project contains the Student API, Docker build definition, CI/CD workflow, and Nginx load-balancer configuration. Captured evidence documents successful local API responses, image publishing and pulling, successful GitHub Actions runs, monitoring output, two concurrent API instances, Nginx proxy responses, and a subsequent CI/CD update. No production cloud deployment or dedicated metrics/tracing stack is present in the supplied project.

### 9. Observations

1. The API uses a small in-memory list, suitable for demonstrating stateless read-only requests but not durable student data storage.
2. Request middleware reports application-side elapsed milliseconds; the separate 88.261 ms PowerShell measurement includes local command overhead.
3. Each FastAPI instance listens on port 8000 inside its container while Docker maps distinct host ports for simultaneous operation.
4. Nginx receives requests on host port 8080 and distributes them to the two running backends.
5. The workflow publishes the same mutable image tag (`v0.1`) on each push to `main`; the final test pulls the updated tag to confirm the change.
6. `fastapi` and `uvicorn` are unpinned dependencies, so exact installed package versions cannot be established from the archive.

### 10. Conclusion

This practical demonstrates a complete local container-based backend delivery workflow: implementing a FastAPI Student API, packaging it with Docker, publishing an image to Docker Hub, automating publication with GitHub Actions, examining logs and health checks, running two instances, and routing traffic through Nginx. The final code-change test connects source updates with a rebuilt, redistributed, and verified Docker image.

### 11. Experiment Links

| Resource | Link |
|---|---|
| Backend Development GitHub Pages | [Backend Development website](https://sehajvohra.github.io/) |
| Practical repository / source directory | [Docker-Hands-On-Practicals](https://github.com/sehajvohra/Docker-Hands-On-Practicals) |
| GitHub Actions workflow | [ActionsYaml.yaml](https://github.com/sehajvohra/Docker-Hands-On-Practicals/blob/main/.github/workflows/ActionsYaml.yaml) |
| Screenshots directory | [screenshots](https://github.com/sehajvohra/Docker-Hands-On-Practicals/tree/main/screenshots) |
| GitHub Actions runs | [Workflow history](https://github.com/sehajvohra/Docker-Hands-On-Practicals/actions) |
| Docker Hub image | [sehajvohra/fastapi-app](https://hub.docker.com/r/sehajvohra/fastapi-app) |

*The supplied project is a standalone repository with files at its root; it does not contain a separate lecture subdirectory. The website link is the general Backend Development site, not a verified deep link to this standalone experiment.*


---

*Evidence basis: uploaded `Docker-Hands-On-Practicals.zip`, its source files and screenshot assets, and the terminal outputs provided during the practical. This report does not include credentials or full source-code listings.*
