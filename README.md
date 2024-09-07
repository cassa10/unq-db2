# unq-db2

# Documentation

- docker-compose.yml: Creates containers for microsoft sql 2022 server express (`mcr.microsoft.com/mssql/server:2022-latest`).
- setUp.sh: script to build docker containers.

# Set up

## Requirements
- Docker installed.
- Recommended:
    - Docker compose installed (or simulate script with docker run command).
    - Bash installed (or execute docker-compose command directly).

## Steps

1. Go to root folder in a terminal.

2. Give execution permission to setUp.sh script:

    ```bash
    chmod +x ./setUp.sh
    ```
3. Run setUp.sh
4. Connect to the database `localhost:1433` with user `sa` and password `Passw0rd!`
