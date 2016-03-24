# platypi ~ REST platform

NOTE: The docker setup is not fully functional yet. This is just some initial scaffolding.

## Getting Started

While setting things up, you can use [this docker/django blog post](https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/) as a reference. This project deviates a bit, but used that to get started initially.

### Prerequisites

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Docker Compose](https://docs.docker.com/compose/install/) (or get Docker Toolbox instead)
* [Docker Machine](https://docs.docker.com/machine/install-machine/) (or get Docker Toolbox instead)
* [Install virtualenv with pip3](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

### Initialize virtualenv

`virtualenv -p python3 .venv && source .venv/bin/activate && pip install -r requirements.txt`

This command creates a virtual environment within the `.venv` directory to isolate the project's python dependencies from your potentially-janky python libraries on your local machine. After creation, it activates the virtualenv and installs the dependencies within.

### Light 'er up

Assuming you followed the docker engine installation instructions, you should be able to get things started.
1. Spin up the VM `docker-machine create -d virtualbox dev;`
  * This VM should show as 'inactive' when you run `docker-machine ls`
2. Attach Docker to the VM `eval "$(docker-machine env dev)"`
  * This should now show the docker-machine as 'active' when you run `docker-machine ls`
3. Build the docker container(s) `docker-compose build`
4. Start up the services `docker-compose up -d` (CURRENTLY BROKEN)
5. Get the VM's IP address `docker-machine ip dev` and hit it in the browser with port:8000 (CURRENTLY BROKEN)
