
mypath=$(ls ./photos/*.jpg)
rm index.html
echo '<!DOCTYPE html>' >> index.html
echo '<html lang="en">' >> index.html
echo '<head>' >> index.html
echo '    <meta charset="UTF-8">' >> index.html
echo '    <meta http-equiv="X-UA-Compatible" content="IE=edge">' >> index.html
echo '    <meta name="viewport" content="width=device-width, initial-scale=1.0">' >> index.html
echo '    <link rel="stylesheet" href="style.css">' >> index.html
echo '    <script src="script.js" defer></script>' >> index.html
echo '    <title>Fema Photographing</title>' >> index.html
echo '</head>' >> index.html
echo '<body>' >> index.html
echo '    <ul id="photolist">' >> index.html
for f in $mypath
do
    echo '        <li><img src="$f"/></li>' >> index.html
done
echo '        <li></li>' >> index.html
echo '    </ul>' >> index.html
echo '</body>' >> index.html
echo '</html>' >> index.html