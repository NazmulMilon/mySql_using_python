

## **MySQL 5.7.40 installation in linux** 


Before installing MySQL 5.7.39 we have to delete all the packages and repositories, for deleting write these commands, 

>$ sudo apt-get purge mysql\* libmysql\*

>$ sudo apt-get clean
 
>$ sudo apt-get purge mysql* 

>$ sudo apt-get update 

At first, download mysql repository using this command,
>$  wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb

After downloaded mysql repository, install this repository,
>$ sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb

After enter the command, select Ubuntu Bionic then select MySQL Server & Cluster then select mysql-5.7 then select ok
After finished update APT repository using this command,
>$ sudo apt update

Check if MySQL 5.7.39 repository is successfully installed by using this command, write 
$  sudo apt policy mysql-server

After update the repository, write these commands for install mysql-server, mysql-community-server and mysql-client,

>$ sudo apt install mysql-server=5.7.40-1ubuntu18.04
> 
>$ sudo apt install mysql-community-server=5.7.40-1ubuntu18.04
 
>$ sudo apt install mysql-client=5.7.40-1ubuntu18.04

>$ sudo apt install mysql-community-server=5.7.40-1ubuntu18.04

>$ sudo apt install mysql-server=5.7.40-1ubuntu18.04

MySQL 5.7.39 is successfully installed in linux 20.0.4
After installed check the version installed correctly or not, 

>$ mysql -V

>$ mysql -u root -p

You will show the version installed successfully or not. 

