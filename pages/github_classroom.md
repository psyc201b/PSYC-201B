# Assignments (Github Classroom)

We'll be using Github Classroom to share all resources for class. **This is the primary way you should be downloading and working with course materials**. Each week, we'll create a new Github Classroom assignment link (prefixed with 📚). Clicking it will automatically create a github repository for you containing all the materials you need. 

You'll then be able to clone this repository to your computer, working through files interactively, make edits/updates, and commit and submit your assignment for review. Each time you push your work to Github, your instructors will be able to provide review, feedback, and discussions that directly reference your code.

```{tip}
You'll *always* be able to access your assignment repositories, history, and instructor feedback after the course is over. So the more effort you put into assignments, the more you engage with instructors, the more you'll learn, and the higher quality resources you'll have for your own future reference!
```

  ## Quick steps

  1. Open any course link that starts with 📚 
  2. Accept the assignment in your browser
  3. Click the URL to go the auto-created github repo (this will alway be named `assignment-name-YOUR-GITHUB-USERNAME`)
  4. Clone it to your local computer using `git clone`
  5. Open and work on any notebook files using JupyterLab or VSCode
  6. Commit your changes locally using `git add` & `git commit`
  7. Push your changes to github using `git push`
  8. Respond to any feedback discussions under the "Pull Requests" tab on the github repo


  ## Tutorial Video

<video width="100%" controls>
  <source src="https://www.dropbox.com/scl/fi/g095grpml8pukno1npwaq/github_classroom.mp4?rlkey=lb5oselwvksefv3ms13asscql&dl=1" type="video/mp4">

  (classroom-updates)=
  ## Updating Assignments

  Occasionally, we'll update assignments that you've already accepted and `git clone`-d to your local computer with additional files (e.g. solutions). Here's how you can `git pull` them to your local computer

  1. Follow the assignment link to go to the repository on github.com that you cloned to first start the assignment. It will be named MM-DD-YOURGITHUBID, e.g. "01-21-ejolly"
  2. Click on "Pull Requests"
  3. Click on "Github Classrom: Sync Assignment"
  4. Click on green "Merge pull request" button
  5. After the button turns purple, indicating the "merge is complete" open up a terminal on your local computer and `cd` into the folder you cloned from this repository, e.g. "01-21-ejolly"
  6. Use `git status` to check if you've saved some changes, but haven't yet `git commit` them. If you don't see "*nothing to commit, working tree clean*", you'll need to `git add` and `git commit` your changed files
  7. Run `git pull` to download the latest changes from github
  8. If you get any wonky error message, run `git merge --no-ff`, and then type the following commands to exit the window that opens: `:`, `w`, `q`, `enter`

  If everything worked you should see some *new* files in your local folder, and you can hack on them as you normally would.

