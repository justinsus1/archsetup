# ----------------------------------------------------- 
# Install packages 
# ----------------------------------------------------- 

installer_packages=(
    "hyprland"
    "waybar"
    "rofi-wayland"
    "alacritty"
    "thunar"
    "xdg-desktop-portal-hyprland"
    "qt5-wayland"
    "qt6-wayland"
    "hyprpaper"
    "hyprlock"
    "firefox"
    "ttf-font-awesome"
    "vim"
    "neofetch"
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
    "vscode"
    "fzf"
    "mpv"
    "gamemode"
    "mangohud"
    "wine-staging"
    "vulkan-intel"
    "lib32-vulkan-intel"
    "openssh"
    "cpupower"
    "libva-intel-driver"
    "intel-media-driver"
    "tlp"
    "lib32-libx11"
    "lib32-libxcomposite"
    "lib32-mangohud"
    "linux-zen-headers"
    "xf86-video-intel"
    "wofi"
    "neovim"
    "fastfetch"
    "pipewire"
    "pipewire-alsa"
    "pipewire-pulse"
    "wireplumber"
    "npm"
)


# sudo pacman -S hyprland waybar rofi-wayland alacritty thunar xdg-desktop-portal-hyprland qt5-wayland hyprpaper hyprlock ttf-font-awesome vim fastfetch ttf-fira-sans ttf-fira-code ttf-firacode-nerd fuse2 gtk4 libadwaita jq blueman brightnessctl  jdk-openjdk pavucontrol grim slurp noto-fonts-cjk wqy-zenhei wqy-microhei fcitx5 fcitx5-configtool fcitx5-gtk fcitx5-qt fcitx5-chinese-addons vscode fzf mpv gamemode mangohud wine-staging vulkan-intel lib32-vulkan-intel openssh cpupower libva-intel-driver intel-media-driver tlp lib32-libx11 lib32-libxcomposite lib32-mangohud linux-zen-headers xf86-video-intel
# sudo pacman -S nerd-fonts

installer_yay=(
    "wlogout" 
    "minecraft-launcher"
    "zen-browser"
    "zoom"
    "goverlay"
    "protonup-qt"
    "hyprshot"
    "swaync"
    "hypridle"
    "starship"
)

# PLEASE NOTE: Add more packages at the end of the following command
_installPackages "${installer_packages[@]}";
_installPackagesYay "${installer_yay[@]}";

# installer_packages=(
#     "steam"
# )

# _installPackages "${installer_packages[@]}";

sudo pacman -S steam steam-native-runtime
