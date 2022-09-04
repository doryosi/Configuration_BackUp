properties([pipelineTriggers([cron('0 2 * * *')])])
node{
    stage("Clean Up"){
        deleteDir()
    }
    stage("Clone Repo"){
        git "https://github.com/doryosi/Configuration_BackUp.git"
    }
    stage("Copy DB"){
        sh "cp /home/smb/PycharmProjects/Configuration_BackUp/devices_details /var/lib/jenkins/workspace/Network_Backup_Pipeline/"
    }
    stage("execute"){
        sh "python3 /var/lib/jenkins/workspace/Network_Backup_Pipeline/Main.py"
    }
    stage("Verify"){
        sh "ls -l /var/lib/jenkins/Switch_BackUp/"
    }
    stage("Notification"){
        mail(body: 'This is a Test Jenkins', subject: 'Test Jenkins', to: 'dorsinai1004@gmail.com')
    }
}
