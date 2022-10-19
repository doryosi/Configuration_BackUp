# Network Nodes Configuration Backup

The script will do the followoing:
- SSH to each networking device
- Get its configuration and save it into a file

## Technologies

- Python
- Jenkins
- Docker
## Prerequisites

- Python3 installed with all the requirements
- CSV file with the following properties:
  - Hostname,IP,os,username,password,enable password
  - BackBone,192.168.75.2,cisco-ios,admin,PassW0rd!,passW0rd$
  - if you don't have enable password, insert the word 'none'
  - For further instructions regarding the supported devices and thier OS,
  please look at the netmiko library documentaion.

## Notes
- The Project implements a CI/CD pipeline that includes Git,Jenkins and Docker.
