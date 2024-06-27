version=1.5
message="update 0627"

git add /home/xintong/Speech-Backbones

git commit -m "$message Version $version"

git tag -a v$version -m "verison $version of the model"

git push origin v$version
git push origin main
