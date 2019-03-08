# Project Stewfish

1. Clone repo
1. `cp .env.example .env` (ask me for the api key/secret)
1. Start docker
1. `docker-compose build`
1. `docker-compose up -d`

The web container is viewable in a browser under port 8888. On Windows, I have to use the IP from `docker-machine ip` instead of localhost since Docker is running through VirtualBox.
