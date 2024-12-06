if [ -f ~/.bashrc_custom ] ;then
    source ~/.bashrc_custom
fi

# -----------------------------------------------------
# Fastfetch if in Hyprland
# -----------------------------------------------------
neofetch

alias ml4w-hyprland='~/.config/ml4w/apps/ML4W_Hyprland_Settings-x86_64.AppImage'
alias la='ls -a'
alias cls='clear; neofetch'
alias wifi='nmtui'
alias bluetooth='blueman-manager'
alias audio='pavucontrol'
alias mc='minecraft-launcher'
# alias surfshark='sudo openvpn ~/surfshark/au-syd.prod.surfshark.comsurfshark_openvpn_udp.ovpn'
alias fuck='brightnessctl set 1%'
alias edit='nano ~/.bashrc'

# steam shit

export MANGOHUD=1
export GAMEMODERUN=1

export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/intel_icd.x86_64.json
export VK_LAYER_PATH=/usr/share/vulkan/implicit_layer.d

