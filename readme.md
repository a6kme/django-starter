## Django Starter for Visual Studio
A starter project with Django and Postgresql which can be run in DevContainer in Visual Studio code. The motivations of this project are
- **Development of the code in a sandboxed environment**: I don't like to pollute the host machine with packages which I might need in my development environment, and devcontainer on VSCode allows me to leverage the power of IDE in a sandboxed environment.
- **A quick and platform agnostic way to spin up an API Project**: I would like to ideally start working on the project within minutes of the inception of the project idea, without worrying about the foundational stack. The setup should be packed with recommended editor config and settings, like sort imports, beautify with formatter etc.

If you have similar use cases, I hope this project helps you too.

### Pre-requisites
1. You should have Visual Studio Code and Docker installed on your machine. You should also have "Dev Containers" extension installed on your machine.

### How to use
1. Checkout the project `git clone https://github.com/a6kme/django-starter better-food && cd better-food`. Replace `better-food` with your project name.
3. Replace the `$$PROJECT_PLACEHOLDER$$` with the project name. Example: `grep -rl '\$\$PROJECT_PLACEHOLDER\$\$' . | xargs sed -i '' 's/\$\$PROJECT_PLACEHOLDER\$\$/better-food/g'` on Mac. `grep -rl '\$\$PROJECT_PLACEHOLDER\$\$' . | xargs sed -i 's/\$\$PROJECT_PLACEHOLDER\$\$/better-food/g'` on Linux.
4. Run `docker-compose up` so that Docker Network is created and Postgresql is started.
5. Reopen the project in a Dev Container in Visual Studio Code.
6. You should be able to run `Make Migrations` and `Migrate` from the drop down in **Run and Debug** panel. After doing that, you can run the Django Server from the same panel.
7. Erase the contents of readme and put up your project specific readme.
8. Change the remote origin of git. `git remote set-url origin <NEW_REPO>`

### How to create a new app
1. Export the environment variables in the shell. `set -o allexport && source .env.dev`
2. Go to apps directory. `cd api/apps`
3. Add the app `python ../manage.py startapp sample`
4. Change the name of the app in `apps/<app_name>/apps.py` from `<app_name>` to `apps.<app_name>`.
5. If you add models or management commands and have to add this app in settings.py `INSTALLED_APPS`, you would add `apps.<app_name>` there instead of `<app_name>`.


### Some important points to be kept in mind
1. Postgresql data is mounted on .pgdata in the project location.

### ToDo
1. Add Test framework
2. Add OpenAPI documentation framework

### TroubleShooting
1. If getting error of the kind `Error opening dev container configurations: CodeExpectedError: ENOPRO: No file system provider found for resource`: Try "Rebuild Container Without Cache" from the command palette of Visual Studio.
