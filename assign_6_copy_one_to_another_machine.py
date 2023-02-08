# #12.	Write a function to copy data from one machine to another machine
# import paramiko
# # from scp import SCPClient
# import os


# hostname = 'ubuntu2004'
# username='ubuntu'
# password='ubuntu'
# src_dir = "F:/"
# dest_dir = "/home/ubuntu/Desktop/hello/"

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    

# ssh.connect(hostname,username = username,password =password)

# sftp = ssh.open_sftp()
# for filename in os.listdir(src_dir):
#     src_file = os.path.join(src_dir,'12_copy_intra_machine.py')
#     dest_file = os.path.join(dest_dir,'quetsions.py')
#     sftp.put(src_file,dest_file)

# sftp.close()
# ssh.close()

# # host = 'ubuntu2004'
# # username='ubuntu'
# # password='ubuntu'
# # src_file = "C:\Users\kiran\Downloads\k\kiran.txt"
# # dest_file = "/home/ubuntu"

#Write a function to copy data from one machine to another machine.
import paramiko
import os

def copy_files_over_sftp(host, username, password, src_dir, dest_dir):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)

    sftp = ssh.open_sftp()
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, "12_copy_intra_machine.py")
        dest_file = os.path.join(dest_dir, "questions.py")
        sftp.put(src_file, dest_file)

    sftp.close()
    ssh.close()

host='ubuntu2004'
username="ubuntu"
password="ubuntu"
src_dir="F:/"
dest_dir="/home/ubuntu/hello/"
copy_files_over_sftp(host, username, password, src_dir, dest_dir)
