chcp 65001
set mypath=%cd%
del index.html
ECHO ^<!DOCTYPE html^>>> index.html
ECHO ^<html lang="en"^>>> index.html
ECHO ^<head^>>> index.html
ECHO     ^<meta charset="UTF-8"^>>> index.html
ECHO     ^<meta http-equiv="X-UA-Compatible" content="IE=edge"^>>> index.html
ECHO     ^<meta name="viewport" content="width=device-width, initial-scale=1.0"^>>> index.html
ECHO     ^<link rel="stylesheet" href="style.css"^>>> index.html
ECHO     ^<script src="script.js" defer^>^</script^>>> index.html
ECHO     ^<title^>Fejes Máté - Fotó^</title^>>> index.html
ECHO ^</head^>>> index.html
ECHO ^<body^>>> index.html
ECHO    ^<div id="fullscreenImageWraper"^>^</div^>>> index.html
ECHO    ^<img src="" alt="" id="fullscreenImage" class="large" loading="lazy"/^>>> index.html
ECHO    ^<div class="photowrapper"^>>> index.html
ECHO        ^<ul id="photolist"^>>> index.html
FOR %%f IN (.\photos\*.jpg) DO (
    ECHO            ^<li^>^<img src="%%f"/^>^</li^>>> index.html
)
ECHO        ^<li^>^</li^>>> index.html
ECHO        ^</ul^>>> index.html
ECHO    ^</div^>>> index.html
ECHO ^</body^>>> index.html
ECHO ^</html^>>> index.html