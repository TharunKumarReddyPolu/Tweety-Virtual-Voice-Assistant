# Hello Open Source Enthusiast/ Viewer 👋
# Welcome to Tweety - The Virtual Voice Assistant's World🐥

📌 Tech Stack used: Python 3.x, Libraries & Modules, Third Party APIs, GIT, VS Code<br>
✏️ Tweety is a virtual voice assistant built on top of Windows OS with python 3.x as the programming language.<br>
✏️ It was built by grabbing the features of various in-built libraries and modules in python<br>
✏️ This voice assistant helps in assisting with various routine tasks that a Software Engineer(SWE) performs in his daily life & work life.<br>

## Feel free to Contribute 😁🛠 Be it code or non-code 😉
## Steps to follow 📃

### 1. Fork the project 🔪

   [Fork Button](https://github.com/TharunKumarReddyPolu/Tweety-Virtual-Voice-Assistant)

### 2. Clone the forked repository 📥

  You need to clone (download) it to your local machine using below command in terminal
```bash
   $ git clone https://github.com/Your_Username/Tweety-Virtual-Voice-Assistant.git
```
> This makes a local copy of the repository in your machine 📂

  Once you have cloned the `Tweety-Virtual-Voice-Assistant` repository in Github, move➡️ to that folder first using the change directory `cd` command on Linux/ Mac/ Windows
```bash
   $ cd Tweety-Virtual-Voice-Assistant
```

### 3. Let us Setup 🔧⚙️
Run the following commands to verify that your _local copy_ has a reference to your _forked remote repository_ on Github
```bash
   $ git remote -v
```
It should display the below output
```
  origin  https://github.com/Your_Username/Tweety-Virtual-Voice-Assistant.git (fetch)
  origin  https://github.com/Your_Username/Tweety-Virtual-Voice-Assistant.git (push)
```

Now, let us add the reference to the original `Tweety-Virtual-Voice-Assistant` repository using the below command 🔙
```bash
  $ git remote add upstream https://github.com/TharunKumarReddyPolu/Tweety-Virtual-Voice-Assistant.git
```
> The above command creates a new remote as `upstream`

To Verify the changes run the below command
```bash
  $ git remote -v
```
Output in console ☑️:
```
  origin    https://github.com/Your_Username/Tweety-Virtual-Voice-Assistant.git (fetch)
  origin    https://github.com/Your_Username/Tweety-Virtual-Voice-Assistant.git (push)
  upstream  https://github.com/TharunKumarReddyPolu/Tweety-Virtual-Voice-Assistant.git (fetch)
  upstream  https://github.com/TharunKumarReddyPolu/Tweety-Virtual-Voice-Assistant.git (push)
```

### 4. Keep in sync always♻️ (best practice🤝🏻) 
It is a better practice to keep the `local copy` in sync with the `original repository` and to stay updated with the latest changes. Run the below commands before making changes or in regular intervals to stay updated with the `base` branch

```
  # Fetch all remote repositories and delete any deleted remote branches
  $ git fetch --all --prune

  # Switch to the master branch
  $ git checkout master

  # Reset the local master branch to match the upstream repository's master branch
  $ git reset --hard upstream/master

  # Push changes to your forked Tweety-Virtual-Voice-Assistant repo
  $ git push origin master
```

### 5. Ready for the contribution 🌝
Once you are done with the above steps, you are ready to contribute to the `Tweety-Virtual-Voice-Assistant` project code. Check out the `issues` tab of the `original repository` and solve them. Once you are done with your changes, submit your efforts with a `pull request`

## Hold on! Instructions are not done yet 🌚

### 6. Installing packages required 📦📥

To install the required packages run the below command
```bash
   pip install -r requirements.txt
```

> If any package installation is not specified above, then those packages are built-in with python.

> If the latest version of the packages is not working on your machine, then you can downgrade the version using the below commands
```bash
   $ pip uninstall package_name
   $ pip install package_name==specific version
```
For instance, If `Speech Recognition` package latest version isn't working in your local machine, then do
```bash
   $ pip uninstall SpeechRecognition
   $ pip install SpeechRecognition==3.8.1
```
where `SpeechRecognition` refers to `package_name` and `3.8.1` refers to `previous version`/`specific version`

### 7. Create a new branch 🌱
Whenever you are going to submit a contribution. Please create a separate branch using the below command and keep your `master` branch clean (i.e. synced with the remote branch)
#### Method 1:
```bash
  $ git branch Changetype_name
```
change type includes `bug fix`, `new feature`, `comments`, `enhancements` etc.

the name includes your `first name` or `last name`

After creating the branch above, run the below command to checkout/switch to the new branch created
```bash
  $ git checkout changetype_name
```
#### Method 2:
You can also create the branch and checkout to the desired branch using the single command below
```bash
  $ git checkout -b changetype_name
```

To add your changes to the branch. Run the below command ➕️
```bash
  $ git add . 
```
> Above command uses `period (.)` indicating all the files are added (or)
> to stage specific file changes, use the below command instead

```bash
  $ git add <file_name>
```

Then, Type in a message that is relevant for the code reviewer using the below command ✉️
```bash
  $ git commit -m 'relevant message'
```

Finally, Push your awesome hard work to your remote repository with the below command 📤🤝🏻
```bash
  $ git push -u origin changetype_name
```
Here, `changetype_name` refers to the branch in your remote repository

Finally, Navigate to your forked `Tweety-Virtual-Voice-Assistant` repository in the browser, where you will see `compare and pull requests`. Kindly click and then add a relevant `title` and `description` to your pull request that defines your valuable effort. 🥳✅️

### Latest Updates
> `Tweety Package Manager`📦🛡 (A Util which simplifies the package installations 🤯) development is completed 🧑‍💻. It is available with file name `tweety_pkg_manager.py`🙂💯. Do give a try by running the file using Powershell/ Command Prompt😉

## Help us improve the project better 📈🤗

Please discuss your concerns with [Polu Tharun Kumar Reddy](https://www.linkedin.com/in/polu-tharun-kumar-reddy/) before creating a new issue. 😉

_Please `STAR`⭐️ the repository if you like the content and code_**😁

_Also enable the `WATCH`👁 button to keep watching the updates on the repository_**😉

💯💻🧑‍💻👩‍💻 Happy Contributing 👩‍💻🧑‍💻💻💯

![tweety_project_cover](https://user-images.githubusercontent.com/62342666/207068013-8b6fb68b-f159-4532-8653-65f2e1be888f.jpg)
