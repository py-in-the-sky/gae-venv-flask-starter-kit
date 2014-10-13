import os, sys

# point appengine to third-party python libraries in the project
gae_env = os.path.join(os.path.abspath('.'), 'gae_env')
sys.path.insert(1, gae_env)
