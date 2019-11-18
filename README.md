# Github Quick Repo

Github Quick Repo is a python scripts, that allows you to quickly initialise a github repository directly from the command line.

## Usage

Firstly, you will need a github token. See [here](https://github.com/settings/tokens) for how to fetch yours. Add it to a file, named `git_token.py`, and add to this folder.

Now, using
```bash
py3 create.py some project name
```
will initalise a folder with the name `some_project_name`, and add a remote origin to a github repository with the same name.

By default, the directory of the project folder will be `C:\User\Documents\projects\`.

#

For best use, compile the `create.py` file into an executable, using `pyinstaller --onefile create.py`, and put the executable in your `PATH`. This changes the usage to

```bash
create some project name
```
but does not change the functionality.


## License
[MIT](https://choosealicense.com/licenses/mit/)