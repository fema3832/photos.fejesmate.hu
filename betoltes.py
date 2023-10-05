# #!/usr/bin/env python
import os
default1 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/x-icon" href="/logo/favicon.ico">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <script src="script.js" defer></script>
    <title>Fejes Máté | Photographer</title>

    <meta name="keywords" content="photography,videography,youtube,instagram,photos,fejesmate,fema3832,fema,photographer,developer,fejes,mate">
    <meta name="description" content="Üdvözöllek!
Fejes Máté vagyok, kezdő fótos, aki szereti megörökíteni az emlékeit és a szép dolgokat.">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@fema3832">
    <meta property="og:title" content="Fejes Máté | Photographer">
    <meta property="og:description" content="Üdvözöllek!
Fejes Máté vagyok, kezdő fótos, aki szereti megörökíteni az emlékeit és a szép dolgokat.">
    <meta property="og:image" content="https://www.photos.fejesmate.hu/photos/EF-6.jpg">
    <link rel="icon" href="https://www.photos.fejesmate.hu/logo/favicon.ico">
    <link rel="apple-touch-icon" href="https://www.photos.fejesmate.hu/logo/favicon.ico">
    <link rel="canonical" href="https://www.photos.fejesmate.hu/">
</head>
<body>
    <h1 id="title">FEJES MÁTÉ PHOTOGRAPHY</h1>

    <div id="fullscreenImageWraper"></div>
    <img src="" alt="" id="fullscreenImage" class="large" loading="lazy"/>
    <ul id="photolist">
"""
default2 = """        <li></li>
    </ul>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(default1)
    for images in sorted(os.listdir("photos")):
        if (images.endswith(".jpg")):
            f.write(f'        <li><img src="./photos/{images}" loading="lazy"/></li>\n')
    f.write(default2)