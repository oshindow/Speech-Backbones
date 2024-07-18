version=1.8
message="update gst loss"

git add /home/xintong/Speech-Backbones

git commit -m "$message Version $version"

git tag -a v$version -m "verison $version of the model"

git push origin v$version
git push origin main
