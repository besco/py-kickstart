#!/usr/bin/python

from snack import *
import time

packages=list();
packages.append("asterisk")
packages.append("epel-release")
packages.append("glibc")
packages.append("glibc-common")
packages.append("glibc.i686")
packages.append("glib2")
packages.append("glib-networking")
packages.append("bzip2")
packages.append("NetworkManager")
packages.append("NetworkManager-gnome")
packages.append("alsa-plugins-pulseaudio")
packages.append("at-spi")
packages.append("dbus")
packages.append("dracut")
packages.append("dracut-kernel")
packages.append("gdm")
packages.append("gdm-user-switch-applet")
packages.append("gnome-panel")
packages.append("gnome-power-manager")
packages.append("gnome-screensaver")
packages.append("gnome-session")
packages.append("gnome-terminal")
packages.append("gvfs-archive")
packages.append("gvfs-fuse")
packages.append("metacity")
packages.append("nautilus")
packages.append("notification-daemon")
packages.append("polkit-gnome")
packages.append("xdg-user-dirs-gtk")
packages.append("ConsoleKit")
packages.append("ConsoleKit-libs")
packages.append("ConsoleKit-x11")
packages.append("DeviceKit-power")
packages.append("GConf2")
packages.append("GConf2-gtk")
packages.append("ModemManager")
packages.append("NetworkManager-glib")
packages.append("ORBit2")
packages.append("alsa-lib")
packages.append("alsa-utils")
packages.append("atk")
packages.append("avahi-autoipd")
packages.append("avahi-glib")
packages.append("avahi-libs")
packages.append("cairo")
packages.append("control-center-filesystem")
packages.append("cups-libs")
packages.append("dbus-python")
packages.append("dbus-x11")
packages.append("desktop-file-utils")
packages.append("dmidecode")
packages.append("dmz-cursor-themes")
packages.append("docbook-dtds")
packages.append("dosfstools")
packages.append("eggdbus")
packages.append("evolution-data-server")
packages.append("exempi")
packages.append("flac")
packages.append("fontconfig")
packages.append("fontpackages-filesystem")
packages.append("freetype")
packages.append("fuse-libs")
packages.append("gdk-pixbuf2")
packages.append("gdm-libs")
packages.append("glib-networking")
packages.append("gnome-bluetooth-libs")
packages.append("gnome-desktop")
packages.append("gnome-disk-utility-libs")
packages.append("gnome-doc-utils-stylesheets")
packages.append("gnome-icon-theme")
packages.append("gnome-keyring")
packages.append("gnome-keyring-pam")
packages.append("gnome-menus")
packages.append("gnome-panel-libs")
packages.append("gnome-python2")
packages.append("gnome-python2-canvas")
packages.append("gnome-python2-gnome")
packages.append("gnome-python2-gnomevfs")
packages.append("gnome-session-xsession")
packages.append("gnome-settings-daemon")
packages.append("gnome-themes")
packages.append("gnome-vfs2")
packages.append("gnutls")
packages.append("gtk2")
packages.append("gtk2-engines")
packages.append("gvfs")
packages.append("hal")
packages.append("hal-info")
packages.append("hal-libs")
packages.append("hdparm")
packages.append("hicolor-icon-theme")
packages.append("hunspell")
packages.append("jasper-libs")
packages.append("libIDL")
packages.append("libSM")
packages.append("libX11")
packages.append("libX11-common")
packages.append("libXScrnSaver")
packages.append("libXau")
packages.append("libXcomposite")
packages.append("libXcursor")
packages.append("libXdamage")
packages.append("libXdmcp")
packages.append("libXext")
packages.append("libXfixes")
packages.append("libXfont")
packages.append("libXft")
packages.append("libXi")
packages.append("libXinerama")
packages.append("libXmu")
packages.append("libXrandr")
packages.append("libXrender")
packages.append("libXres")
packages.append("libXt")
packages.append("libXtst")
packages.append("libXv")
packages.append("libXxf86misc")
packages.append("libXxf86vm")
packages.append("libarchive")
packages.append("libart_lgpl")
packages.append("libasyncns")
packages.append("libatasmart")
packages.append("libbonobo")
packages.append("libbonoboui")
packages.append("libcanberra")
packages.append("libcanberra-gtk2")
packages.append("libcdio")
packages.append("libcroco")
packages.append("libdaemon")
packages.append("liberation-fonts-common")
packages.append("liberation-sans-fonts")
packages.append("libexif")
packages.append("libfontenc")
packages.append("libgail-gnome")
packages.append("libgdata")
packages.append("libglade2")
packages.append("libgnome")
packages.append("libgnomecanvas")
packages.append("libgnomekbd")
packages.append("libgnomeui")
packages.append("libgsf")
packages.append("libgudev1")
packages.append("libgweather")
packages.append("libical")
packages.append("libjpeg-turbo")
packages.append("libmcpp")
packages.append("libnl")
packages.append("libnotify")
packages.append("libogg")
packages.append("libpcap")
packages.append("libpng")
packages.append("libproxy")
packages.append("libproxy-bin")
packages.append("libproxy-python")
packages.append("librsvg2")
packages.append("libsamplerate")
packages.append("libsndfile")
packages.append("libsoup")
packages.append("libtalloc")
packages.append("libtdb")
packages.append("libtevent")
packages.append("libthai")
packages.append("libtiff")
packages.append("libvorbis")
packages.append("libwacom")
packages.append("libwacom-data")
packages.append("libwnck")
packages.append("libxcb")
packages.append("libxkbfile")
packages.append("libxklavier")
packages.append("libxslt")
packages.append("mcpp")
packages.append("mobile-broadband-provider-info")
packages.append("mozilla-filesystem")
packages.append("mtools")
packages.append("nautilus-extensions")
packages.append("pango")
packages.append("parted")
packages.append("pixman")
packages.append("plymouth-gdm-hooks")
packages.append("plymouth-utils")
packages.append("pm-utils")
packages.append("polkit")
packages.append("polkit-desktop-policy")
packages.append("ppp")
packages.append("pulseaudio")
packages.append("pulseaudio-gdm-hooks")
packages.append("pulseaudio-libs")
packages.append("pulseaudio-libs-glib2")
packages.append("pycairo")
packages.append("pygobject2")
packages.append("pygtk2")
packages.append("rarian")
packages.append("rarian-compat")
packages.append("redhat-menus")
packages.append("rtkit")
packages.append("sg3_utils-libs")
packages.append("sgml-common")
packages.append("smp_utils")
packages.append("sound-theme-freedesktop")
packages.append("speex")
packages.append("startup-notification")
packages.append("system-gnome-theme")
packages.append("system-icon-theme")
packages.append("system-setup-keyboard")
packages.append("udisks")
packages.append("unique")
packages.append("usermode")
packages.append("vte")
packages.append("wpa_supplicant")
packages.append("xcb-util")
packages.append("xdg-user-dirs")
packages.append("xkeyboard-config")
packages.append("xml-common")
packages.append("xorg-x11-drv-wacom")
packages.append("xorg-x11-server-Xorg")
packages.append("xorg-x11-server-common")
packages.append("xorg-x11-server-utils")
packages.append("xorg-x11-xauth")
packages.append("xorg-x11-xinit")
packages.append("xorg-x11-xkb-utils")
packages.append("zenity")
packages.append("glib2")
packages.append("libudev")
packages.append("openssh")
packages.append("openssh-clients")
packages.append("openssh-server")
packages.append("plymouth")
packages.append("plymouth-core-libs")
packages.append("firstboot")
packages.append("glx-utils")
packages.append("plymouth-system-theme")
packages.append("spice-vdagent")
packages.append("wacomexpresskeys")
packages.append("wdaemon")
packages.append("xorg-x11-utils")
packages.append("xvattr")
packages.append("authconfig-gtk")
packages.append("btparser")
packages.append("cracklib-python")
packages.append("libXvMC")
packages.append("libXxf86dga")
packages.append("libdmx")
packages.append("libreport")
packages.append("libreport-compat")
packages.append("libreport-gtk")
packages.append("libreport-newt")
packages.append("libreport-plugin-reportuploader")
packages.append("libreport-plugin-rhtsupport")
packages.append("libreport-python")
packages.append("libselinux-python")
packages.append("libtar")
packages.append("libuser-python")
packages.append("mtdev")
packages.append("ntp")
packages.append("ntpdate")
packages.append("plymouth-graphics-libs")
packages.append("plymouth-plugin-label")
packages.append("plymouth-plugin-two-step")
packages.append("plymouth-theme-rings")

def askForm(uWinText,askText,uForm):
  screen=SnackScreen()
  try:
    ret = EntryWindow(screen, uWinText, askText, uForm, allowCancel = 0, width = 40, entryWidth = 20, buttons = [ 'Ok' ], help = None)
  except:
    print 'poh'
  screen.finish()
  return(ret)

def errorWindow(userMessage):
  screen=SnackScreen()
  ret = ButtonChoiceWindow(screen, 'Error', userMessage, buttons = [ 'Ok' ]);
  screen.finish()

def writeFile(uFile,uStr):
  fHandle=open(uFile,'w')
  fHandle.write(uStr);
  fHandle.close;


screen = screen=SnackScreen()

grid = GridForm(screen, "Package Installation", 1, 6)

width = 65
progress = Scale(width, 100)


grid.add (progress, 0, 1, (0, 1, 0, 0))

label = Label("")
grid.add(label, 0, 2, (0, 1, 0, 0), anchorLeft = 1)

info = Textbox(width, 4, "", wrap = 1)
grid.add(info, 0, 3, (0, 1, 0, 0))
x=float;

for i in range(len(packages)):
  pass
  label.setText('Installing package: '+packages[i])
  x=(float(i)/float(len(packages)))*100
  progress.set(int(x)+1)
  grid.draw()
  screen.refresh()
  time.sleep(0.01)

screen.finish()



