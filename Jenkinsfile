properties([pipelineTriggers([pollSCM('0 2 * * *')])])
node{
    stage("Clean Up"){
        deleteDir()
    }
    stage("Clone Repo"){
        git "https://github.com/doryosi/Configuration_BackUp.git"
    }
    stage("Copy DB"){
        sh "cp /home/smb/PycharmProjects/Configuration_BackUp/devices_details /var/lib/jenkins/workspace/Git_Job/Configuration_BackUp/"
    }
    stage("Verify"){
        sh "ls -l /var/lib/jenkins/workspace/Git_Job/Configuration_BackUp/"
    }
}