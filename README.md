# sshub
A encrypted SSH host manager

## Installation ⚙️
sshpass is required

MacOS:
`sudo port install sshpass`

Linux:
`yum install sshpass`

````
git clone https://github.com/p-i-c-o/sshub
cd sshub
chmod +x sshub
sudo cp sshub /usr/local/bin
````

## Usage 🛠️
In the sshub directory, run the `passgen.py` script.
# WARNING
The way the script works, when you add a new host, it will encrypt it with the password you provided at the calling of sshub, so keep that password if you want to use sshub for a long time.

All of your encrypted hosts and their passwords will be saved in the sshub/sshkeys directory. Keep them safe too, don't be afraid to make backups.
