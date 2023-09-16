import argparse
import os
import shutil
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError, CommandParser


class Command(BaseCommand):
    """Generate Cypress boilerplate.

    This Django management command generates Cypress boilerplate for your project.

    Attributes
    ----------
    help (str): A short description of the command.
    """

    help = "Gererate the Cypress boilerplate"

    def add_arguments(self, parser: CommandParser) -> None:
        """Define command-line arguments for the Cypress boilerplate generation.

        Args:
        ----
        parser (CommandParser): The argument parser.

        Returns:
        -------
        None
        """
        parser.add_argument(
            "--force",
            action=argparse.BooleanOptionalAction,
            help="Override the existing cypress configuration file (cypress.config.js)",
        )

    def handle(self, **options: bool) -> None:
        """Handle the command execution.

        Args:
        ----
        **options: Command options and arguments.

        Returns:
        -------
        None
        """
        force_option: bool = options["force"]

        if not force_option and self._cypress_config_file_exists():
            raise CommandError(
                "Existing Cypress configuration file found. Please upgrade "
                + "the file manually or overwrite changes using --force."
            )

        self._copy_stubs()

        self.stdout.write(
            self.style.SUCCESS("Successfully generated the Cypress boilerplate.")
        )

    def _copy_stubs(
        self,
    ) -> None:
        """Copy Cypress stub files to the project directory.

        This method copies Cypress stub files from the package directory to the
        project directory. In case there is an existing Cypress configuration,
        it deletes it.

        Returns
        -------
            None
        """
        package_directory = Path(__file__).parent.parent.parent.absolute()

        shutil.rmtree("cypress")
        shutil.copytree(os.path.join(package_directory, "stubs/cypress"), "cypress")

        os.remove("cypress.config.js")
        shutil.copyfile(
            os.path.join(package_directory, "stubs/cypress.config.js"),
            "cypress.config.js",
        )

    def _cypress_config_file_exists(
        self,
    ) -> bool:
        """Check if the Cypress configuration file or directory exists.

        This method checks if the Cypress configuration file (cypress.config.js) or
        directory (cypress) exists in the project directory.

        Returns
        -------
            bool: True if the file or directory exists, False otherwise.
        """
        return os.path.isfile("cypress.config.js") or os.path.isdir("cypress")
