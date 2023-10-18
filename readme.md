## Django Starter for Visual Studio
A starter project with Django and Postgresql which can be run in DevContainer in Visual Studio code.

### How to use
1. Checkout the project `git clone https://github.com/a6kme/django-starter`
2. Rename the folder to the Project name that you wish to create. Example: `mv django-starter better-food && cd better-food`.
3. Replace the `$$PROJECT_PLACEHOLDER$$` with the project name. Example: `grep -rl '\$\$PROJECT_PLACEHOLDER\$\$' . | xargs sed -i '' 's/\$\$PROJECT_PLACEHOLDER\$\$/better-food/g'` on Mac. `grep -rl '\$\$PROJECT_PLACEHOLDER\$\$' . | xargs sed -i 's/\$\$PROJECT_PLACEHOLDER\$\$/better-food/g'` on Linux.
4. Run `docker-compose up` so that Docker Network is created and Postgresql is started.
5. Reopen the project in a Dev Container in Visual Studio Code.
6. You should be able to run `Make Migrations` and `Migrate` from the drop down in **Run and Debug** panel. After doing that, you can run the Django Server from the same panel.

### Some important points to be kept in mind
1. Postgresql data is mounted on .pgdata
