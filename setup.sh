echo InstallerScript
sed -i "s/REPL_USR/$SUDO_USER/g" /home/$SUDO_USER/.fartd/fartd.service
mv /home/$SUDO_USER/.fartd/fartd.service /etc/systemd/system/fartd.service

systemctl daemon-reload
systemctl enable --now fartd.service
