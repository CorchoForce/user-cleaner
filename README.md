# User Cleaner

<a href="https://codeclimate.com/github/CorchoForce/user-cleaner/maintainability"><img src="https://api.codeclimate.com/v1/badges/4d557edf5762792e521e/maintainability" /></a>

![demonstration](https://cdn.discordapp.com/attachments/539836343094870016/858756519813840897/unknown.png)

## Table of Contents

<!--ts-->

- [About](#about)
- [Requirements](#requirements)
- [How to use](#how-to-use)
  - [Setting up](#setup)
- [Technologies](#technologies)
<!--te-->

## About

It is a simple cron built for Pega a Visão project. The objective of this is to check the validation time of the users and delete the users that have more than 7 days with the invalid status.

## Requirements

To run this repository by yourself you will need to install python, and them install all the project [requirements](requirements.txt). We will show how to do it in the next step.

## How to use

### Setup

```bash
# Clone the cron repository
$ git clone <https://github.com/CorchoForce/user-cleaner>

# Access the frontend directory
$ cd user-cleaner/

# Install all the pip requirements
$ pip install -r requirements.txt

# Create a .env archive
$ touch .env

# Access the .env with the following parameters
 MONGO_USERNAME= #Mongo username
 MONGO_PASSWORD= #Mongo password
 MONGO_DATABASE= #Mongo database name
 MONGO_COLLECTION= #Mongo collection
 MONGO_PORT= #Mongo port
 SCHEDULE_TIME_HOUR= #Time that the scheduler will run
 MONGO_HOSTNAME= #Mongo hostname

# Access the src directory
$ cd src/

# Run scheduler.py archive
$ python scheduler.py

```

![demonstration](https://cdn.discordapp.com/attachments/539836343094870016/858758304713146369/unknown.png)

## Technologies

- Python
- MongoDB
- apscheduler
