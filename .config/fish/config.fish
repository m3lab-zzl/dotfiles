if status is-interactive
    # Commands to run in interactive sessions can go here
end

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f $HOME/mamba3/bin/conda
    eval $HOME/mamba3/bin/conda "shell.fish" hook $argv | source
else
    if test -f "$HOME/mamba3/etc/fish/conf.d/conda.fish"
        . "$HOME/mamba3/etc/fish/conf.d/conda.fish"
    else
        set -x PATH $HOME/mamba3/bin $PATH
    end
end

if test -f "$HOME/mamba3/etc/fish/conf.d/mamba.fish"
    source "$HOME/mamba3/etc/fish/conf.d/mamba.fish"
end
# <<< conda initialize <<<

set -x CONDA_AUTO_ACTIVATE_BASE false
set -g fish_color_autosuggestion white
source $HOME/.settings
# pixi completion --shell fish | source
# Add this to the end of your config file
starship init fish | source
zoxide init fish --cmd j | source
