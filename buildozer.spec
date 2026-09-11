[app]

title = Risk Calculator
package.name = riskcalc
package.domain = org.riskcalc
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.allow_backup = True
android.private_storage = True
android.accept_sdk_license = True
android.logcat_filters = *:S python:D
p4a.branch = v2024.1.21
p4a.bootstrap = sdl2
bin_dir = ./bin
log_level = 2
warn_on_root = 1
