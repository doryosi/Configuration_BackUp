properties([pipelineTriggers([cron('0 2 * * *')])])
pipeline{
    agent any
    environment{
    DB_PATH = "home/smb/PycharmProjects/Configuration_BackUp/devices_details"
    GIT_REPO = "https://github.com/doryosi/Configuration_BackUp.git"
    }
    stages{
    stage("Clean Up"){
        steps{
            deleteDir()
        }
    }
    stage("Clone Repo"){
        steps{
            git "$GIT_REPO"
        }
    }
    stage("Copy DB"){
        steps{
            echo "$DB_PATH $WORKSPACE $JOB_NAME"
            sh "$DB_PATH $WORKSPACE/$JOB_NAME"
        }
    }
    stage("build docker image"){
        steps{
            sh "docker build --tag config-backup ."
        }
    }
    stage("execute"){
        steps{
            sh "docker-compose up"
        }
    }
     stage("Verify"){
        steps{
            sh "ls -l /var/lib/jenkins/Switch_BackUp"
        }
      }
     stage("Send Email"){
        steps{
            node("master"){
                echo "Send Email"
            }
        }
    }
}
post{
    success{    mail(body: "The Network Backup ${env.BUILD_URL} has been executed successfully",
                     subject: "Succeeded Pipeline: ${currentBuild.fullDisplayName}",
                     to: 'dorsinai1004@gmail.com')
    }
    failure{
                mail(body: "Something is wrong with ${env.BUILD_URL}",
                     subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                     to: 'dorsinai1004@gmail.com')
            }
        }
    }


