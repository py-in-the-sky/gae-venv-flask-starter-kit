import os, pip, sys

GAE_ENV = os.path.join(os.path.abspath('.'), 'app/gae_env')

RED = '\x1b[0;31m{}\x1b[0m'
GREEN = '\x1b[0;32m{}\x1b[0m'
YELLOW = '\x1b[0;33m{}\x1b[0m'

def resolve_installed_package_name(pip_package):
    egg_dir = pip_package.egg_name() + '.egg-info'
    top_level = os.path.join(pip_package.location, egg_dir, 'top_level.txt')
    with open(top_level, 'r') as f:
        installed_package_name = f.readline().strip()
    return installed_package_name

def make_link(source, target):
    rel_source = os.path.relpath(source, GAE_ENV)
    os.symlink(rel_source, target)

def make_links():
    skip_message = 'skipping {} (already linked in target directory)'
    warning_message = 'warning: {} and {} attempted, but neither exists'
    link_message = 'creating the following symlink: {}'

    for package in pip.get_installed_distributions():
        package_name = resolve_installed_package_name(package)
        source = os.path.join(package.location, package_name)
        target = os.path.join(GAE_ENV, package_name)

        if os.path.exists(target) or os.path.exists(target + '.py'):
            print '    ' + YELLOW.format(skip_message.format(package_name))

        elif os.path.exists(source):
            print '    ' + GREEN.format(link_message.format(target))
            make_link(source, target)

        elif os.path.exists(source + '.py'):  # package is a single file
            print '    ' + GREEN.format(link_message.format(target + '.py'))
            make_link(source + '.py', target + '.py')

        else:
            print '    ' + RED.format(warning_message.format(source, source + '.py'))


if __name__ == '__main__':
    make_links()
