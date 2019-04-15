from artifact import Artifact

with open('unresolved_dependencies.txt', 'r') as f:
    for line in f:
        artifact = Artifact(line.strip().strip('- '))
        artifact.install()
