properties([pipelineTriggers([cron('0 2 * * *')])])
pipeline{
    agent any
    stages{
    stage("Clean Up"){
      steps{
        deleteDir()
      }
    }
    stage("Clone Repo"){
      steps{
        git "https://github.com/doryosi/Configuration_BackUp.git"
      }
    }
    stage("build docker image"){
      steps{
        sh "docker build config-backup ."
      }
    }
    stage("execute"){
      steps{
        sh "docker-compose up"
      }
    }
    stage("Verify"){
      steps{
        sh "ls -l /var/lib/jenkins/Switch_BackUp/"
      }
    }
    stage("Notification"){
                 mail(body: 'The Network Backup has been executed successfully', 
                     subject: 'Network Backup Job',
                     to: 'dorsinai1004@gmail.com')
        }
    }
}


