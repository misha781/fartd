echo InstallerScript

pacman -S --noconfirm tailscale

systemctl enable --now tailscaled

tailscale up --auth-key=yourcode

mv fartd.service /etc/systemd/system/fartd.service

systemctl daemon-reload
sudo systemctl enable --now fartd.service
