python3 src/main.py "/StaticSiteGenerator/"

if [ $? -eq 0 ]; then
  echo "Static Site Generator project built successfully."
else
  echo "Error: Failed to run src/main.py."
fi