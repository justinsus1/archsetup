# ----------------------------------------------------- 
# Os-prober
# ----------------------------------------------------- 

installer_packages=(
    "os-prober"
)

_installPackages "${installer_packages[@]}";


echo "GRUB_DISABLE_OS_PROBER=false" | sudo tee -a /etc/default/grub/
grub-mkconfig -o /boot/grub/grub.cfg
