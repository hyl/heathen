# heathen
This is a sample artifact resolver for troublesome Maven 1.x projects that cannot be upgraded to Maven 2.x.
* This is a quick and dirty script to solve a problem. This repo is for information purposes only and not to be relied upon for production use: it has only been open-sourced for the purpose of demonstration. It is untested and will not be maintained.*

## Instructions for use:
1. `pip3 install -r requirements.txt`
2. Create and use an envvar for `MAVEN1_REPO_PATH` (eg `export MAVEN1_REPO_PATH="/Users/jamie/.maven/repository"`)
3. Create `unresolved_dependencies.txt` and fill with the log from "The build cannot continue because of the following unsatisfied dependencies:" step in `maven dist` or similar. An example can be found in `unresolved_dependencies.txt.sample`.
4. `python3 app.py`