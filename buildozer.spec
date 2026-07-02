[app]
title = IP Tracker
package.name = iptracker
package.domain = org.crimson
source.dir = .
source.include_exts = py,png,jpg
version = 1.0

# Uygulamanın çalışması için gereken modüller (ÇOK KRİTİK)
requirements = python3,kivy,requests,urllib3,chardet,idna

orientation = portrait
fullscreen = 0

# Android İzinleri (İnternete bağlanması için şart)
android.permissions = INTERNET

_android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True
