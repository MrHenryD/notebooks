# MLflow & Feast Feature Store Environment

This repository provides a reproducible environment for machine learning experiment tracking with [MLflow](https://mlflow.org/) and feature engineering using [Feast](https://feast.dev/), orchestrated via Docker Compose.

## Project Structure

```
.
├── docker-compose.yml
├── Makefile
├── images/
│   ├── Dockerfile.jupyter
│   └── Dockerfile.mlflow
├── notebooks/
│   ├── feast/
│   ├── mlflow/
│   ├── flink/
│   ├── kafka/
│   └── spark/
```

- **images/**: Dockerfiles for MLflow server and Jupyter/Feast notebook environments.
- **notebooks/**: Example notebooks and Feast feature store configurations.
- **docker-compose.yml**: Orchestrates MLflow, Postgres backend, and Jupyter/Feast services.

## Services

- **mlflow-backend**: PostgreSQL database for MLflow tracking.
- **mlflow-server**: MLflow Tracking Server and Model Registry.
- **notebook**: JupyterLab with PySpark and Feast for interactive development.

## Usage

### Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed.

### Start the Environment

You can start all services using the Makefile:

```sh
make run-compose
```

Or directly with Docker Compose:

```sh
docker-compose up --build
```

### Accessing Services

- **JupyterLab**: [http://localhost:9999](http://localhost:9999)
- **MLflow UI**: [http://localhost:5555](http://localhost:5555)

### Example Notebooks

- **MLflow Experiment Tracking**: See [`notebooks/mlflow/Experiment Tracking.ipynb`](notebooks/mlflow/Experiment%20Tracking.ipynb)
- **Feast Feature Store Usage**: See [`notebooks/feast/Feast Usage.ipynb`](notebooks/feast/Feast%20Usage.ipynb)

## Data Persistence

- MLflow artifacts are stored in the container filesystem (`mlruns` directory).
- Notebooks are persisted to your local `notebooks/` directory via Docker volume.

## Customization

- To add Python dependencies, edit the `EXTRA_PIP_PACKAGES` build argument in the respective Dockerfiles or in `docker-compose.yml`.

## Cleaning Up

To stop and remove all containers:

```sh
docker-compose down --remove-orphans
```
