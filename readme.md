## Django Starter for Visual Studio
A starter project with Django and Postgresql which can be run in DevContainer in Visual Studio code. 

### Some important points to be kept in mind
1. Change network name in docker-compose.yaml if you intend to run multiple projects simultaneously. The same name should be entered in .devcontainer/devcontainer.json
2. Postgresql data is mounted on .pgdata
