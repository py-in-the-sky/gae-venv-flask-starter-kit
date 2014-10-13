# This script helps keep your venv, gae_env, and requirements.txt in sync.
# This script will:
# 1. install any required Python packages not yet installed
# 2. sync up the requirements file with any packages manually pip installed
# 3. make the app/gae_env directory if it does not already exist
# 4. symlink all pip-installed packages into app/gae_env
# (The appengine SDK will know to resolve all symlinks at deployment.)

echo
echo 'running "pip install -r requirements.txt"'
echo
pip install -r requirements.txt

echo
echo 'running "pip freeze > requirements.txt"'
echo
pip freeze > requirements.txt

echo
echo 'running "mkdir app/gae_env"'
echo
mkdir app/gae_env

echo
echo 'running "python link_env.py"'
echo
python link_env.py

echo
echo 'done!'
