[app]

# (str) Title of your application
title = Risk Calculator

# (str) Package name
package.name = riskcalc

# (str) Package domain (needed for android/ios packaging)
package.domain = org.riskcalc

# (str) Source code where the main package is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,ttf

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude
#source.exclude_exts = spec

# (list) List of directory to exclude
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.3.0

# (str) Custom source folders for requirements
#p4a.source_dir =

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use
#android.ndk_api = 21

# (bool) Private mode for Android
android.private_storage = True

# (str) Android entry point
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme
#android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
#android.wakelock = False

# (list) Android application meta-data
#android.meta_data =

# (list) List of Java .jar files to add
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk assets directory
#android.assets = data/*.png,data/*.json

# (str) The Android arch to build for
android.archs = arm64-v8a

# (str) The Android launch mode
#android.launch_mode = singleTask

#
# Python for android (p4a) specific
#

# (str) python-for-android git clone directory
#p4a.branch = master

# (str) The directory in which python-for-android should look for your own build recipes
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
#p4a.bootstrap = sdl2

# (int) port number to specify an http proxy
#p4a.port =

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios

# (str) Name of the certificate
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

#
# Other
#

# (str) The directory in which the application data is stored
#appdir =

# (str) Directory where to store the build output
#build_dir =

# (str) The directory where to put the final package
bin_dir = ./bin

# (str) The directory where to put the log files
log_level = 2

# (bool) Whether to warn on unknown buildozer.spec keys
warn_on_root = 1

# (str) The directory where to put the build directory
#build_dir =
