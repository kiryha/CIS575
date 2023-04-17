import json


class Settings:
    def __init__(self, assembler_root):
        self.assembler_root = assembler_root
        self.settings_file = '{}/data/settings.json'.format(self.assembler_root)
        self.settings_data = None
        self.current_settings = None
        self.expand_settings()

    def expand_settings(self):
        """
        Fill source settings with current project data
        """

        # Read abstract data
        self.load_settings()

        # Calculate current data
        project_root = self.current_settings['project_root']['string']
        sql_file_path = self.current_settings["sql_file_path"]["string"].format(self.assembler_root)
        versioned_pages = self.current_settings["versioned_pages"]["string"].format(project_root)
        final_pages = self.current_settings["final_pages"]["string"].format(project_root)
        pdf_files = self.current_settings["pdf_files"]["string"].format(project_root)

        # Set current data
        self.current_settings["sql_file_path"]["string"] = sql_file_path
        self.current_settings["versioned_pages"]["string"] = versioned_pages
        self.current_settings["final_pages"]["string"] = final_pages
        self.current_settings["pdf_files"]["string"] = pdf_files

    def load_settings(self):
        """
        Loading settings twice cos dictionary.copy() did not work
        """

        with open(self.settings_file, 'r') as file_content:
            self.settings_data = json.load(file_content)

        with open(self.settings_file, 'r') as file_content:
            self.current_settings = json.load(file_content)

    def save_settings(self):

        with open(self.settings_file, 'w') as file_content:
            json.dump(self.settings_data, file_content, indent=4)

    def get_sql_file_path(self):

        return self.current_settings["sql_file_path"]["string"]

    def get_project_root(self):

        return self.current_settings["project_root"]["string"]

    def get_versioned_pages(self):

        return self.current_settings["versioned_pages"]["string"]

    def get_final_pages(self):

        return self.current_settings["final_pages"]["string"]

    def get_pdf_files(self):

        return self.current_settings["pdf_files"]["string"]

    def set_project_root(self, project_root):

        self.settings_data['project_root']['string'] = project_root
        self.save_settings()
