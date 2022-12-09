sudo apt-get update
sudo wget https://raw.githubusercontent.com/Yenthe666/InstallScript/11.0/odoo_install.sh
sudo chmod +x odoo_install.sh
sudo ./odoo_install.sh
sudo apt install python3-pip
sudo apt-get install libxml2-dev libxslt1-dev -y
sudo apt install libsasl2-dev python-dev libldap2-dev libssl-dev
sudo pip3 install python-ldap
sudo pip3 uninstall Werkzeug
sudo apt install wget xfonts-75dpi
cd /tmp
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb
sudo dpkg -i wkhtmltox_0.12.5-1.bionic_amd64.deb
sudo apt -f install
sudo su odoo
echo "installation completes!run pip3 install -r requirements.txt;pip3 install Werkzeug==0.11.15;/odoo/odoo-server/odoo-bin"
