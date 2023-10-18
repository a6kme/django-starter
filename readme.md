## Django Starter for Visual Studio
A starter project with Django and Postgresql which can be run in DevContainer in Visual Studio code. The motivations of this project are
- **Development of the code in a sandboxed environment**: I don't like to pollute the host machine with packages which I might need in my development environment, and devcontainer on VSCode allows me to leverage the power of IDE in a sandboxed environment.
- **A quick and platform agnostic way to spin up an API Project**: I would like to ideally start working on the project within minutes of the inception of the project idea, without worrying about the foundational stack. The setup should be packed with recommended editor config and settings, like sort imports, beautify with formatter etc.

If you have similar use cases, I hope this project helps you too.

### How to use
1. Checkout the project `git clone https://github.com/a6kme/django-starter`
2. Rename the folder to the Project name that you wish to create. Example: `mv django-starter better-food && cd better-food`.
3. Replace the `$$PROJECT_PLACEHOLDER$$` with the project name. Example: `grep -rl '\$\$PROJECT_PLACEHOLDER\$\$' . | xargs sed -i '' 's/\$\$PROJECT_PLACEHOLDER\$\$/better-food/g'` on Mac. `grep -rl '\$\$PROJECT_PLACEHOLDER\$\$' . | xargs sed -i 's/\$\$PROJECT_PLACEHOLDER\$\$/better-food/g'` on Linux.
4. Run `docker-compose up` so that Docker Network is created and Postgresql is started.
5. Reopen the project in a Dev Container in Visual Studio Code.
6. You should be able to run `Make Migrations` and `Migrate` from the drop down in **Run and Debug** panel. After doing that, you can run the Django Server from the same panel.

### How to create a new app
1. Export the environment variables in the shell. `set -o allexport && source .env.dev`
2. Go to apps directory.
3. Add the app `python ../manage.py startapp sample`
4. Once you have setup a new project specific app, please feel free to delete the `sample` app and remove it's url bindings from `api.urls`


### Some important points to be kept in mind
1. Postgresql data is mounted on .pgdata in the project location.

### ToDo
1. Add Test framework
2. Add OpenAPI documentation framework
