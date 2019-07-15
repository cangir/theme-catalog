# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.box_version = "= 2.3.5"
  config.vm.synced_folder ".", "/vagrant"
  config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1"

  # Work around disconnected virtual network cable.
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get -y update

    # Work around https://github.com/chef/bento/issues/661
    # apt-get -qqy upgrade
    DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade

    apt-get -y install make zip unzip postgresql python3 python3-pip
    pip3 install --upgrade pip
    pip3 install -r "/vagrant/requirements.txt"

    vagrantTip="The shared directory is located at /vagrant\\nTo access your shared files: cd /vagrant"
    echo -e $vagrantTip > /etc/motd

    wget http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    cd redis-stable
    make
    make install

    echo "Done installing your virtual machine! Run command: vagrant ssh"
  SHELL
end
