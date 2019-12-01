import os
from sys import argv
import github as git
import getpass
from git_token import token

def sys(*cmds): # run terminal cmds in current directory
    for cmd in cmds:
        os.system(cmd)

def main():
    if len(argv) == 1: # If no argument was passed, don't do anyhing
        action_display = """ERR: Can't create a project with no name.
        Use: create <project_name>"""
        print(action_display)
        return

    project_name = "_".join(argv[1:])

    accept_name = bool({'y':1, 'n':0}[input('Accept "%s" as project name? (y/n) ' % project_name)])
    if not accept_name:
        return

    # get github user
    github = git.Github(token)
    user = github.get_user()

    user_name = getpass.getuser()
    projects_folder = "C:\\Users\\%s\\Documents\\projects" % user_name
    project_path = projects_folder + "\\" + project_name

    remote_origin_url = user.html_url + project_name

    # create project folder and go to directory
    sys("mkdir %s" % project_path)
    os.chdir(project_path)

    # create github repo if it doesn't already exist
    if not project_name in [repo.name for repo in user.get_repos()]:
        user.create_repo(project_name)
    else:
        accept_overwrite = bool({'y':1, 'n':0}[input('Repository "%s" already exist. Continue? (y/n)' % project_name)])
        if not accept_overwrite:
            return

    # initialize local repo and add remote origin
    cmds = [
        'echo "# test" >> README.md',
        "git init",
        "type nul > README.md",
        "git add .",
        "git commit -m %s" % ('"initial commit"'),
        "git remote add origin %s" % remote_origin_url,
        "git push -u origin master",
        "code %s" % project_path
    ]
    sys(*cmds)


if __name__ == '__main__':
    main()