#!/usr/bin/env python
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class testWindow(Gtk.Window):
  def __init__(self):
    super().__init__(title="Test Window")
    
    hbox = Gtk.Box(spacing=10)
    hbox.set_homogeneous(False)
    vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox_left.set_homogeneous(False)
    vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox_right.set_homogeneous(False)
