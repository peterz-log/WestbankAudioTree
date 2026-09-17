[app]

# (str) Title of your application
title = Westbank Audio Tree

# (str) Package name
package.name = westbankaudiotree

# (str) Package domain
package.domain = mw.westbank

# (str) Source directory
source.dir = .

# (str) Main Python file
source.main = main.py

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,mp3,wav,ogg

# (str) Application version
version = 1.0

# (list) Python requirements
requirements = python3,kivy,pyjnius

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (str) Android API
android.api = 35

# (str) Minimum Android API
android.minapi = 23

# (str) Android NDK version
android.ndk = 27c

# (str) Android architecture
android.arch = arm64-v8a

# (list) Android permissions
android.permissions = INTERNET,POST_NOTIFICATIONS

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Copy library files into the APK
android.add_src =

# (str) Android application theme
android.presplash_color = #0E1612

# (str) Android app theme
android.apptheme = @android:style/Theme.Material.NoActionBar

# (bool) Show a console
android.uses_legacy_p4a = 0

# (str) Log level
log_level = 2

# (str) Warn about Python compilation
warn_on_root = 1


[buildozer]

# (str) Log level
log_level = 2

# (str) Warn when running as root
warn_on_root = 1
