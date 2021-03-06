# Starter kit for Google App Engine projects using Python, Flask, and Virtualenv

Flask and Virtualenv aren't required; however, this starter kit illustrates in general how to manage third-party Python packages in Google App Engine projects, which can be a big hurdle to getting started in App Engine.

This project is currently set up for OSX and Linux.  Please feel free to adapt it for use on Windows.  One change I know you would need for Windows is in link_env's make_link subroutine.  It creates symlinks in the app/gae_env directory, but there is no symlink concept in Windows; you would need to change this subroutine to create copies instead of symlinks.

To get started, clone this repo.  Then cd into the root directory of the project.  Then run the following from the command line; the first two lines aren't required but are recommended:

```bash
virtualenv venv
source venv/bin/activate
bash manage_pip_packages.sh
```

At this point, you should be ready to run your app in your local dev environment, visit the page, and see the hello-world message.  To deploy your app, just change the first line of app/app.yaml (i.e., "application: your-app-id") to reflect your own app ID.  Then you can deploy, visit \<your app ID\>.appspot.com and see the hello-world message.  Now you're ready to start working on your app without having to worry about all the housekeeping involved in incorporating new third-party Python libraries into your App-Engine app.

The script manage_pip_packages.sh will be useful throughout the development of your project as it will help to keep your pip-installed Python packages, your requirements.txt file, and your App Engine project's directory for third-party Python packages (app/gae_env) in sync.  Whenever you manually pip-install a package, cd into the project's root directory and run this script.  And that's all you have to do to manage incorporating new third-party Python libraries into your App-Engine app.


Thanks to [Vita Smid](https://github.com/ze-phyr-us/linkenv) for the inspiration for link_env.py.
