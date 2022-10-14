properties([pipelineTriggers([cron('0 2 * * *')])])
pipeline{
    agent any
    environment{
    DOCKERHUB_CREDENTIALS = credentials('doryosisinay-dockerhub')
    DB_PATH = "/home/smb/PycharmProjects/Configuration_BackUp/devices_details"
    GIT_REPO = "https://github.com/doryosi/Configuration_BackUp.git"
    IMAGE_NAME = "doryosisinay/config-backup:latest"
    PATH_TO_SAVE_CONF_FILES = "/var/lib/jenkins/Network_BackUp/"
    CONTAINER_NAME = "conf_backup_script"
    EMAIL = "dorsinai1004@gmail.com"
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
            echo "$DB_PATH $WORKSPACE"
            sh "cp $DB_PATH $WORKSPACE"
        }
    }
    stage("build docker image"){
        steps{
            sh "docker-compose build"
        }
    }
//     stage("execute"){
//         steps{
//             sh "docker-compose up"
//         }
//     }
     stage("Verify"){
        steps{
            sh "ls -l $PATH_TO_SAVE_CONF_FILES"
        }
     }
     stage('Login'){
         steps{
            sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
         }
     }
     stage('Push'){
         steps{
             sh "docker-compose push"
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
    always{
        sh "docker rm $CONTAINER_NAME"
        sh "docker image rm $IMAGE_NAME"
        sh "docker logout"
    }
    success{    mail(body: "The Network Backup ${env.BUILD_URL} has been executed successfully",
                     subject: "Succeeded Pipeline: ${currentBuild.fullDisplayName}",
                     to: "$EMAIL")
    }
    failure{
                mail(body: "Something is wrong with ${env.BUILD_URL}",
                     subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                     to: "$EMAIL")
            }
        }
    }


