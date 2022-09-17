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
    stage("Copy DB"){
        steps{
            sh "cp /home/smb/PycharmProjects/Configuration_BackUp/devices_details /var/lib/jenkins/workspace/Network_Backup_Pipeline/"
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
    success{    mail(body: 'The Network Backup has been executed successfully',
                     subject: 'Network Backup Job',
                     to: 'dorsinai1004@gmail.com')
    }
    failure{
                mail(body: "Something is wrong with ${env.BUILD_URL}",
                     subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                     to: 'dorsinai1004@gmail.com')
    }
}


