if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -g fish_greeting ''
set -g fish_greeting_file ''
set -gx fish_prompt_pwd_dir_length 0

if status is-interactive
    # Commands to run in interactive sessions can go here
end

function fish_prompt
    # Set username color to blue
    set_color blue
    echo -n '<'(whoami)

    # Set the "@" symbol to default color
    set_color 61AFEF
    echo -n '@'

    # Set hostname color to cyan
    set_color cyan
    echo -n (echo $hostname)

    # Set the current directory color to blue
    set_color blue
    echo -n '['(prompt_pwd)

    # Set a space before the ">" symbol
    echo -n ']'

    # Close the prompt with ">"
    set_color blue
    echo -n '><> '
end
