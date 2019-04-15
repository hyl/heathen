import os
import requests
import shutil

MAVEN1_REPO_PATH = os.getenv('MAVEN1_REPO_PATH')


class Artifact:
    def __init__(self, artifact_name):
        self.artifact_name = artifact_name
        tokenized_artifact_name = artifact_name.split(':')

        # convert into named vars
        self.group_id = tokenized_artifact_name[0]
        self.artifact_id = tokenized_artifact_name[1]
        self.version = tokenized_artifact_name[2]
        self.file_type = tokenized_artifact_name[3]

    def get_package_url(self):
        """
        Gets the URL to download the package from.
        :return:
        """
        return 'http://central.maven.org/maven2/{group_id}/{artifact_id}/{version}/{artifact_id}-{version}.{file_type}'.format(
            group_id=self.group_id, artifact_id=self.artifact_id, version=self.version, file_type=self.file_type)

    def init_dir_structure(self):
        """
        Creates the directory structure for the repository
        :return:
        """
        install_dir = '{repo_path}/{group_id}/{file_type}s'.format(repo_path=MAVEN1_REPO_PATH, group_id=self.group_id,
                                                                   file_type=self.file_type)

        if not os.path.exists(install_dir):
            os.makedirs(install_dir)

        return install_dir

    def get_artifact_filename(self):
        """
        Gets the local filename of a downloaded artifact.
        :return:
        """
        return '{artifact_id}-{version}.{file_type}'.format(artifact_id=self.artifact_id, version=self.version,
                                                            file_type=self.file_type)

    def is_installed(self):
        """
        Checks if the package is installed.
        :return:
        """
        install_path = '{repo_path}/{group_id}/{file_type}s/{artifact_id}-{version}.{file_type}'.format(
            repo_path=MAVEN1_REPO_PATH, group_id=self.group_id, artifact_id=self.artifact_id, version=self.version,
            file_type=self.file_type)

        if os.path.exists(install_path):
            return True
        else:
            return False

    def install(self):
        """
        Carries out the install process for a package.
        :return:
        """
        if self.is_installed():
            print('Package {} is already installed! Skipping...'.format(self.artifact_name))
            return

        print('Installing package {}...'.format(self.artifact_name))

        install_dir = self.init_dir_structure()

        # download the JAR file
        r = requests.get(self.get_package_url(), stream=True)
        install_path = '{install_dir}/{artifact_filename}'.format(install_dir=install_dir,
                                                                  artifact_filename=self.get_artifact_filename())
        with open(install_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Installed!')
