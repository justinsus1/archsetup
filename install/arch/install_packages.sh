# ----------------------------------------------------- 
# Install packages 
# ----------------------------------------------------- 

installer_packages=(
    "hyprland"
    "waybar"
    "rofi-wayland"
    "alacritty"
    "dunst"
    "thunar"
    "xdg-desktop-portal-hyprland"
    "qt5-wayland"
    "qt6-wayland"
    "hyprpaper"
    "hyprlock"
    "firefox"
    "ttf-font-awesome"
    "vim"
    "fastfetch"
    "ttf-fira-sans" 
    "ttf-fira-code" 
    "ttf-firacode-nerd"
    "fuse2"
    "gtk4"
    "libadwaita"
    "jq"
    "python-gobject"
    "blueman"
    "networkmanager"
    "brightnessctl"
    "jdk-openjdk"
    "pavucontrol"
    "grim"
    "slurp"
    "noto-fonts-cjk"
    "wqy-zenhei"
    "wqy-microhei"
    "fcitx5"
    "fcitx5-configtool"
    "fcitx5-chinese-addons"
    "fcitx5-gtk"
    "fcitx5-qt"
)

installer_yay=(
    "wlogout" 
    "minecraft-launcher"
    "zen-browser"
)

# PLEASE NOTE: Add more packages at the end of the following command
_installPackages "${installer_packages[@]}";
_installPackagesYay "${installer_yay[@]}";
