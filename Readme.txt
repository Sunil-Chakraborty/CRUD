Important Notes :
makemigrations will fail :
a) if the app is not in "installed app" in settings.py


To center the div content use the following bootstrap class:
<div class="mx-auto" style="width: 800px;">

To center the table content use the following bootstrap class:
<table class="table table-striped table-bordered table-sm w-auto">

How to delete a single file from repository:

# Add db.sqlite3 to .gitignore
echo "db.sqlite3" >> .gitignore

# Remove db.sqlite3 from the repository but keep it locally
git rm --cached db.sqlite3

# Add .gitignore to the staging area
git add .gitignore

# Commit the changes
git commit -m "Remove db.sqlite3 from repository and add to .gitignore"

# Push the changes to the remote repository
git push origin master

