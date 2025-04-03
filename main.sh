python3 src/main.py

if [ $? -eq 0 ]; then
  echo "Server started at http://localhost:8888"
  python3 -m http.server 8888 --directory docs
else
  echo "Error: Failed to run src/main.py. HTTP server will not start."
fi
