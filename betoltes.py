# #!/usr/bin/env python
import os
import time
default1 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/x-icon" href="/logo/favicon.ico">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <script src="script.js" defer></script>
    <title>Fejes Máté - Fotó</title>

    <meta name="keywords" content="photography,videography,youtube,instagram,photos,fejesmate,fema3832,fema,photographer,developer,fejes,mate">
    <meta name="description" content="Üdvözöllek!
Fejes Máté vagyok, kezdő fótos, aki szereti megörökíteni az emlékeit és a szép dolgokat.">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@fema3832">
    <meta property="og:title" content="Fejes Máté | Photographer">
    <meta property="og:description" content="Üdvözöllek!
Fejes Máté vagyok, kezdő fótos, aki szereti megörökíteni az emlékeit és a szép dolgokat.">
    <meta property="og:image" content="https://photos.fejesmate.hu/photos/EF-6.jpg">
    <link rel="icon" href="https://photos.fejesmate.hu/logo/favicon.ico">
    <link rel="apple-touch-icon" href="https://photos.fejesmate.hu/logo/favicon.ico">
    <link rel="canonical" href="https://photos.fejesmate.hu/">
</head>
<body>
    <h1 id="title">FEJES MÁTÉ PHOTOGRAPHY <span>
        <p id="contact">Vízjel nélküli fényképek miatt, keress email-ben: fmatephoto@gmail.com</p>
    </span></h1>

    <div id="fullscreenImageWraper"></div>
    <img src="" alt="" id="fullscreenImage" class="large" loading="lazy"/>
    <div class="photowrapper">
        <ul id="photolist">
"""
default2 = """            <li></li>
        </ul>
    </div>
</body>
</html>
"""

times = []
for i in os.listdir("photos"):
    times.append(i)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(default1)
    for images in sorted(times, key=lambda x: time.strptime(x[:8], '%Y%m%d'), reverse=True):
        if (images.endswith(".jpg")):
            f.write(f'            <li><img src="./photos/{images}" loading="lazy"/></li>\n')
    f.write(default2)