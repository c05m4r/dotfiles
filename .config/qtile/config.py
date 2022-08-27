import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
size_bar = 30
default_font = "Ubutu Mono Nerd Font"
size_font = 16
sep_size_font = 22
color_fore = "#000000"
color_back1 = "#87ceeb"
color_back2 = "#ffffff"
right_sep = ''
left_sep = ''
right_slim_sep = ''
left_slim_sep = ''
sep_padding = 4

keys = [
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 10- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn("nautilus"), desc="Launch explorer"),
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Launch menu")
    #Key([mod], "d", lazy.spawn("diodon"), desc="Launch clipboar manager")
]

groups = [Group(i) for i in "12345"]
for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen()
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True)
            )
        ]
    )

layouts = [
    layout.Bsp(),
    layout.Max()
]

widget_defaults = dict(
    font = default_font,
    fontsize = size_font,
    padding = 0,
    foreground=color_fore
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    hide_unused=False,
                    background=color_back2,
                    active=color_fore,
                    inactive=color_fore,
                    highlight_method='text',
                    padding = 5,
                    ),
                widget.CurrentLayout(
                    fmt=right_sep,
                    foreground=color_back2,
                    fontsize=sep_size_font,
                    ),
                widget.Spacer(),
                widget.CurrentLayout(
                    fmt=left_sep,
                    foreground=color_back2,
                    fontsize=sep_size_font,
                    ),
                widget.Memory(
                    format='{MemUsed: .0f}{mm}',
                    #measure_mem='G',
                    background=color_back2,
                    update_interval=10
                    ),
                widget.Sep(
                    foreground=color_back2,
                    background=color_back2,
                    padding=sep_padding,
                    ),
                widget.CurrentLayout(
                    fmt=left_sep,
                    foreground=color_back1,
                    background=color_back2,
                    fontsize=sep_size_font,
                    ),
                widget.CPU(
                    format='CPU {load_percent}%',
                    update_interval=10
                    ),
                widget.Sep(
                    foreground=color_back1,
                    background=color_back1,
                    padding=sep_padding
                    ),
                widget.CurrentLayout(
                    fmt=left_sep,
                    foreground=color_back2,
                    background=color_back1,
                    fontsize=sep_size_font,
                    ),
                widget.ThermalZone(
                    background=color_back2,
                    fgcolor_normal=color_fore,
                    update_interval=10
                    ),
                widget.Sep(
                    foreground=color_back2,
                    background=color_back2,
                    padding=sep_padding
                    ),
                widget.CurrentLayout(
                    fmt=left_sep,
                    foreground=color_back1,
                    background=color_back2,
                    fontsize=sep_size_font,
                    ),
                widget.Volume(
                    fmt='Vol {}',
                    foreground=color_fore,
                    ),
                widget.Sep(
                    foreground=color_back1,
                    background=color_back1,
                    padding=sep_padding
                    ),
                widget.CurrentLayout(
                    fmt=left_sep,
                    foreground=color_back2,
                    background=color_back1,
                    fontsize=sep_size_font,
                    ),
                widget.Battery(
                    format='Bat {percent:2.0%}',
                    background=color_back2,
                    update_interval=10
                    ),
                widget.Sep(
                    foreground=color_back2,
                    background=color_back2,
                    padding=sep_padding
                    ),
                widget.CurrentLayout(
                    fmt=left_sep,
                    foreground=color_back1,
                    background=color_back2,
                    fontsize=sep_size_font,
                    ),
                widget.Net(
                    update_interval=3
                    ),
                widget.Sep(
                    foreground=color_back1,
                    background=color_back1,
                    padding=sep_padding
                    ),
                widget.CurrentLayout(
                    fmt=left_sep,
                    foreground=color_back2,
                    background=color_back1,
                    fontsize=sep_size_font,
                    ),
                widget.Clock(
                    format="%a %d/%m %H:%M",
                    background=color_back2,
                    update_interval=10,
                    padding=10
                    )
            ],
            24,
            background=[color_back1],
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/dotfiles/autostart.sh'])
