# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "trusty64server"
  config.vm.box_url = "https://oss-binaries.phusionpassenger.com/vagrant/boxes/latest/ubuntu-14.04-amd64-vbox.box"
  config.ssh.username = 'vagrant'

  config.vm.define :production do |production|
  	production.vm.network :public_network, :bridge => 'eth0', :auto_config => false
    config.vm.network "forwarded_port", guest: 80, host: 8000
    production.vm.provider :virtualbox do |vb|
        vb.customize [ "modifyvm", :id, "--name", "RiskInfo-Production","--memory", 4096 ]
  	end
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "playbook.yml"
    end
  end

  config.vm.define :dev do |dev|
  	dev.vm.network :public_network, :bridge => 'eth0', :auto_config => false
    config.vm.network "forwarded_port", guest: 8000, host: 8000
    config.vm.network "forwarded_port", guest: 8080, host: 8080
    dev.vm.provision :shell, :path => "scripts/vagrant/provision_geonode_dev.sh"
  	dev.vm.provider :virtualbox do |vb|
       vb.customize [ "modifyvm", :id, "--name", "RiskInfo-Dev","--memory", 4096 ]
  	end
  end
end
