if [ -f ~/.bashrc_custom ] ;then
    source ~/.bashrc_custom
fi

eval "$(starship init zsh)"

# -----------------------------------------------------
# Fastfetch if in Hyprland
# -----------------------------------------------------
fastfetch

alias ml4w-hyprland='~/.config/ml4w/apps/ML4W_Hyprland_Settings-x86_64.AppImage'
alias la='ls -a'
alias cls='clear'
alias wifi='nmtui'
alias bluetooth='blueman-manager'
alias audio='pavucontrol'
alias mc='minecraft-launcher'
# alias surfshark='sudo openvpn ~/surfshark/au-syd.prod.surfshark.comsurfshark_openvpn_udp.ovpn'
alias fuck='brightnessctl set 1%'
alias edit='nano ~/.zshrc'
alias check='sudo pacman -Syu; yay -Syu'
alias shutdown='shutdown now'
alias chat='ollama run deepseek-r1'

