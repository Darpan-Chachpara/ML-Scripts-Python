#sudo apt update
#sudo apt upgrade -y
#sudo systemctl reboot
#wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb
#sudo apt install ./wkhtmltox_0.12.6-1.bionic_amd64.deb
wget -O - https://nightly.odoo.com/odoo.key | sudo apt-key add -
echo "deb http://nightly.odoo.com/14.0/nightly/deb/ ./" | sudo tee /etc/apt/sources.list.d/odoo.list
sudo apt update
sudo apt install odoo
systemctl status odoo
#ss -tunelp | grep 8069
#sudo apt -y install vim nginx

