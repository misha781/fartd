echo InstallerScript

mv fartd.service /etc/systemd/system/fartd.service

systemctl daemon-reload
sudo systemctl enable --now fartd.service
