echo "[options]" | sudo tee -a /etc/pacman.conf
echo "ParallelDownloads = 10" | sudo tee -a /etc/pacman.conf
echo "[multilib]" | sudo tee -a /etc/pacman.conf
echo "Include = /etc/pacman.d/mirrorlist" | sudo tee -a /etc/pacman.conf

pacman -Syu
