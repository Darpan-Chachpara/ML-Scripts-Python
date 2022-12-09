sudo apt update
sudo apt install cpu-checker
sudo apt install qemu-kvm libvirt-bin bridge-utils virtinst virt-manager
sudo usermod -aG libvirt $USER
sudo usermod -aG kvm $USER
sudo systemctl is-active libvirtd
