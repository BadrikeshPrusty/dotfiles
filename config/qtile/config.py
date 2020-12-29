import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

terminal = "alacritty"
file_manager = "thunar"
browser = "firefox"
#browser = "google-chrome-stable"
dmenu = "dmenu_run -h 22 -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14' -p 'Run: '"

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [

# FUNCTION KEYS

# SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "r", lazy.spawn(dmenu)),
    Key([mod], "d", lazy.spawn('rofi -show drun')),
    Key([mod], "w", lazy.spawn('rofi -show window')),
    Key([mod], "t", lazy.spawn(terminal)),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "F6", lazy.spawn('vlc --video-on-top')),
    Key([mod], "e", lazy.spawn(home + '/.config/qtile/scripts/emoji-rofi.sh')),
    Key([mod], "c", lazy.spawn('obs')),
    Key([mod], "b", lazy.spawn(browser)),
    Key([mod], "g", lazy.spawn('google-chrome-stable')),
    Key([mod], "p", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),


# SUPER + SHIFT KEYS

    Key([mod, "shift"], "Return", lazy.spawn(file_manager)),
    Key([mod, "shift"], "d", lazy.spawn(dmenu)),
    Key([mod, "shift"], "p", lazy.spawn(home + '/.config/qtile/scripts/power-menu.sh')),
    Key([mod, "shift"], "t", lazy.spawn(home + '/.config/qtile/scripts/fonts-dmenu.sh')),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),

# CONTROL + ALT KEYS

    Key(["mod1", "control"], "f", lazy.spawn('firefox')),
    Key(["mod1", "control"], "g", lazy.spawn('google-chrome-stable')),
    Key(["mod1", "control"], "t", lazy.spawn('alacritty')),
    Key(["mod1", "control"], "Return", lazy.spawn('alacritty')),

# ALT + ... KEYS

    Key(["mod1"], "h", lazy.spawn('alacritty -e htop')),
    Key(["mod1"], "F3", lazy.spawn('xfce4-appfinder')),

# CONTROL + SHIFT KEYS
    Key([mod2, "shift"], "Escape", lazy.spawn('alacritty -e htop')),

# SCREENSHOTS
    Key([mod], "Print", lazy.spawn(home + '/.config/qtile/scripts/scrot-dmenu.sh')),
    Key([], "Print", lazy.spawn("scrot -f '%d-%m-%y@%H-%M-%S.png' -e 'mv $f ~/Pictures/screenshots/' && notify-send 'Entire screen captured'")),

# MULTIMEDIA KEYS

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

# TOGGLE TOUCHPAD
    Key([], "XF86TouchpadToggle", lazy.spawn(home + '/.config/qtile/scripts/touchpad-toggle.sh')),

# LOCK SCREEN
    Key([], "XF86ScreenSaver", lazy.spawn("xfce4-screensaver-command --lock")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8",]


#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ",]
group_labels = ["", "", "", "", "", "", "", "",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-8 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-8 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(margin=2, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.MonadWide(margin=2, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
  #  layout.Matrix(**layout_theme),
  #  layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
  #  layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
]

# COLORS FOR THE BAR

def init_colors():
    return [["#2F343F", "#2F343F"], # color 0
            ["#2F343F", "#2F343F"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#fba922", "#fba922"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#f3f4f5", "#f3f4f5"], # color 5
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#6790eb", "#6790eb"], # color 8
            ["#a9a9a9", "#a9a9a9"]] # color 9


colors = init_colors()


# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

#MOUSE CALLBACK FUNCTIONS

def open_audio_settings(qtile):
    qtile.cmd_spawn('pavucontrol')

def open_htop(qtile):
    qtile.cmd_spawn('alacritty -e htop')

def open_power_manager(qtile):
    qtile.cmd_spawn('xfce4-power-manager-settings')

def open_google_chrome(qtile):
    qtile.cmd_spawn('google-chrome-stable')

# def open_firefox(qtile):
#     qtile.cmd_spawn('firefox')

def open_file_manager(qtile):
    qtile.cmd_spawn(file_manager)

# def open_obs_studio(qtile):
#     qtile.cmd_spawn('obs')

def open_calendar(qtile):
    qtile.cmd_spawn('alacritty -e calcurse')

def open_clocks(qtile):
    qtile.cmd_spawn('gnome-clocks')

def open_terminal(qtile):
    qtile.cmd_spawn('alacritty')

def open_dmenu(qtile):
    qtile.cmd_spawn(dmenu)

def open_rofi(qtile):
    qtile.cmd_spawn('rofi -show drun')

def open_power_menu(qtile):
    qtile.cmd_spawn(home + '/.config/qtile/scripts/power-menu.sh')

def toggle_audio_sink(qtile):
    qtile.cmd_spawn('python ' + home + '/.config/qtile/scripts/toggle-audio-sink.py')

def toggle_audio_source(qtile):
    qtile.cmd_spawn('python ' + home + '/.config/qtile/scripts/toggle-audio-source.py')


def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
               widget.Image(
                        filename = "~/.config/qtile/icons/python.png",
                        margin_y = 2,
                        margin_x = 3,
                        mouse_callbacks = {"Button1": open_dmenu,
                                           "Button2": open_rofi,
                                           "Button3": open_power_menu
                                          } 
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.GroupBox(font="FontAwesome",
                        fontsize = 16,
                        margin_y = 2,
                        margin_x = 0,
                        padding_y = 6,
                        padding_x = 4,
                        borderwidth = 0,
                        disable_drag = True,
                        active = colors[9],
                        inactive = colors[5],
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors[8],
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               #widget.CurrentLayout(
               #         font = "Noto Sans Bold",
               #         foreground = colors[5],
               #         background = colors[1]
               #         ),
               widget.CurrentLayoutIcon(
                        scale = 0.8
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
            #    widget.Image(
            #             filename = "~/.config/qtile/icons/obs.png",
            #             margin_y = 2,
            #             margin_x = 3,
            #             mouse_callbacks = {"Button1": open_obs_studio} 
            #             ),
            #    widget.Image(
            #             filename = "~/.config/qtile/icons/firefox.png",
            #             margin_y = 2,
            #             margin_x = 3,
            #             mouse_callbacks = {"Button1": open_firefox} 
            #             ),
               widget.Image(
                        filename = "~/.config/qtile/icons/googlechrome.png",
                        margin_y = 2,
                        margin_x = 3,
                        mouse_callbacks = {"Button1": open_google_chrome} 
                        ),
               widget.Image(
                        filename = "~/.config/qtile/icons/filemanager.png",
                        margin_y = 2,
                        margin_x = 3,
                        mouse_callbacks = {"Button1": open_file_manager} 
                        ),
               widget.Image(
                        filename = "~/.config/qtile/icons/terminal.png",
                        margin_y = 2,
                        margin_x = 3,
                        mouse_callbacks = {"Button1": open_terminal} 
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.WindowName(font="mononoki Nerd Font Mono",
                        fontsize = 14,
                        foreground = colors[5],
                        background = colors[1],
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
              # widget.CapsNumLockIndicator(
              #          font="mononoki Nerd Font Mono",
              #          fontsize = 14,
              #          update_interval = 1,
              #          foreground = colors[5],
              #          background = colors[1],
              #          ),
               widget.Net(
                        font="mononoki Nerd Font Mono",
                        fontsize = 14,
                        format='{down}⬇️ {up}⬆️',
                        foreground = colors[5],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[7],
                        background=colors[1],
                        padding = 0,
                        fontsize=16,
                        mouse_callbacks = {"Button1": open_power_manager}
                        ),
               widget.Battery(
                        unknown_char='⚡',
                        charge_char='⚡',
                        discharge_char='',
                        format='{char}{percent:2.0%}',
                        font="mononoki Nerd Font Mono",
                        update_interval = 5,
                        fontsize = 14,
                        foreground = colors[5],
                        background = colors[1],
                        mouse_callbacks = {"Button1": open_power_manager}
	                    ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[6],
                        background=colors[1],
                        padding = 0,
                        fontsize=16,
                        mouse_callbacks = {"Button1": open_htop}
                        ),
               widget.CPU(
                        font="mononoki Nerd Font Mono",
                        update_interval = 2,
                        fontsize = 14,
                        format='{freq_current}GHz {load_percent}%',
                        foreground = colors[5],
                        background=colors[1],
                        mouse_callbacks = {"Button1": open_htop}
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[4],
                        background=colors[1],
                        padding = 0,
                        fontsize=16,
                        mouse_callbacks = {"Button1": open_htop}
                        ),
               widget.Memory(
                        font="mononoki Nerd Font Mono",
                        format = '{MemUsed}M',
                        update_interval = 2,
                        fontsize = 14,
                        foreground = colors[5],
                        background = colors[1],
                        mouse_callbacks = {"Button1": open_htop}
                       ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[3],
                        background=colors[1],
                        padding = 0,
                        fontsize=16,
                        mouse_callbacks = {"Button1": open_calendar, "Button3": open_clocks}
                        ),
               widget.Clock(
                        foreground = colors[5],
                        background = colors[1],
                        fontsize = 14,
                        font="mononoki Nerd Font Mono",
                        format="%d/%m/%Y %A %H:%M:%S",
                        mouse_callbacks = {"Button1": open_clocks, "Button3": open_calendar}
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[2],
                        background=colors[1],
                        padding = 0,
                        fontsize=16,
                        mouse_callbacks = {
                            "Button2": open_audio_settings, 
                            "Button1": toggle_audio_sink,
                            "Button3": toggle_audio_source
                            }
                        ),
               widget.Volume(
                        foreground = colors[5],
                        background = colors[1],
                        fontsize = 14,
                        font="mononoki Nerd Font Mono",
                        update_interval = 1
                       ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Systray(
                        background=colors[1],
                        icon_size=20,
                        padding = 4
                        ),
               widget.TextBox(
                        padding = 1,
                        ),
              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

#def init_widgets_screen2():
#    widgets_screen2 = init_widgets_list()
#    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
#widgets_screen2 = init_widgets_screen2()


#def init_screens():
#    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=22)),
#            Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=22))]

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=22))]

screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    #Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []


main = None

#@hook.subscribe.startup_once
#def start_once():
#    home = os.path.expanduser('~')
#    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True
        window.cmd_bring_to_front()                 #bring all new floating window to front


floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    #{'wmclass': 'scrcpy'},
    {'wmclass': 'qalculate-gtk'},
    {'wmclass': 'display'},
    {'wmclass': 'gnome-screenshot'},
    {'wmclass': 'pavucontrol'},
    {'wmclass': 'confirm'},
    {'wmclass': 'ksysguard'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wname': 'branchdialog'},
    {'wname': 'Open File'},
    {'wname': 'Preferences'},
    {'wname': 'Event Tester'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "smart" # or focus

wmname = "LG3D"
