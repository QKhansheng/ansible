Date: 2019/07/08

Author: qiankunhansheng

Mail: qiankunhansheng@myhexin.com

Features: Dedicated to the automated operation and maintenance of hexin software with ansible  ...(Continuous update)

verison 1.0 ：updateCert getUser

Read the next content will be helpful before use these scripts :

1 What is ansible?

    Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments
    or zero downtime rolling updates.

2 How to deploy ansible in centos/rh?

    method 1: yum install ansible     
    #default verison 2.4 , It's important to note that some differences in versions may cause scripts to have different running results or even errors.
                                      
    method 2(Recommended!) : pip install ansible  
    #the default version installed by pip is 2.8.x 
    #It requires that the pip tool must be installed on your system, and the better python version is 2.7(nether 3.5) ,
    #If there are some errors during the installation process , try running “esay_install --upgrade pip” ，
    
    methpd 3 : Source code
    #Didn't try it for now!
    
3 How to use the script ?

    for example : updateCert.py 
    
    setup1 : cp -f updateCert.py /path/to/ansible/library
    
    setup2 : ansible host -m updateCert
    
4 If you got any idea about the Code , please try to build another branch to solve some of the problems and bugs in the old code 
    you can also create a new feature script in your git!