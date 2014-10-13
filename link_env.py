import os, pip, sys

GAE_ENV = os.path.join(os.path.abspath('.'), 'app/gae_env')

def make_link(source, target):
    rel_source = os.path.relpath(source, GAE_ENV)
    os.symlink(rel_source, target)

def make_links():
    for package in pip.get_installed_distributions():
        package_name = package.key.replace('-', '_')
        source = os.path.join(package.location, package_name)
        target = os.path.join(GAE_ENV, package_name)

        if os.path.exists(target):
            message = 'Skipping {} (already linked in target directory)'
            print message.format(package_name)

        elif os.path.exists(source):
            make_link(source, target)

        elif os.path.exists(source+'.py'):  # package is a single file
            make_link(source+'.py', target+'.py')

        else:
            message = 'warning: {} and {} attempted, but neither exists'
            print '    ' + message.format(source, source+'.py')


if __name__ == '__main__':
    make_links()
