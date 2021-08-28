# ritoman-betting-service
A registry service for webhook providers and consumers

## Quick Start
Here is quick list of instructions to setup the project and run test cases. In order to do this the only dependency is `docker-compose`

### Setup 
1. clone the repo `git clone https://github.com/sed-cloud/ritoman-betting-service.git`
2. build the container `docker-compose build` 
3. start the container `docker-compose up`

### Run Tests
1. open the container's bash `docker-compose run ritoman-betting-service bash`
2. from within the shell run `pytest`