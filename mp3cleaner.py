# === Import libraries ===
import os

# === Import packages ===
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
from mutagen import MutagenError


# === Class 'ThemedApp' ===
class MP3TagCleaner:
    """
    This class is designed to remove specific metadata tags—particularly the 'year' tag—
    from MP3 files using the Mutagen library. It supports both single-file and batch
    directory cleaning operations. The class handles exceptions from corrupted or tagless
    MP3 files gracefully, attempting to initialize ID3 tags where necessary before cleaning.

    Parameters:
    - verbose (bool): When set to True, the class prints detailed status messages for each file processed.

    Returns:
    - None
    """

    # === Function '__init__' ===
    def __init__(self, verbose=True):
        """
        Initializes an instance of the MP3TagCleaner class, enabling users to control verbosity.
        If verbosity is enabled, informative messages are printed during tag cleaning operations.
        This allows for easy debugging and tracking of batch operations across multiple files or directories.

        Parameters:
        - verbose (bool): If True, print status messages during execution. Defaults to True.

        Returns:
        - None
        """
        self.verbose = verbose

    # === Function 'loadtags' ===
    @staticmethod
    def loadtags(mp3_path):
        """
        Attempts to load ID3 tags from an MP3 file using the EasyID3 interface.
        If the file does not have existing EasyID3 headers, it tries to create
        and save a standard ID3 header first, ensuring compatibility and stability.

        Parameters:
        - mp3_path (str): The full filesystem path to the MP3 file to load tags from.

        Returns:
        - EasyID3: An EasyID3 tag object representing the metadata of the given MP3 file.
        """
        try:
            return EasyID3(mp3_path)
        except MutagenError:
            ID3(mp3_path).save()
            return EasyID3(mp3_path)

    # === Function 'cleanyearfromfile' ===
    def cleanfromfile(self, mp3_path):
        """
        Removes the 'date' or year-related tag from a single MP3 file, if present.
        This function is useful when cleaning individual files of outdated or incorrect
        metadata. It uses EasyID3 to locate and delete the 'date' tag. If the tag is
        missing or the file is invalid, it logs an appropriate message.

        Parameters:
        - mp3_path (str): The full filesystem path to the MP3 file to clean.

        Returns:
        - None
        """
        try:
            tags = self.loadtags(mp3_path)
            if 'date' in tags:
                del tags['date']
                tags.save()
                if self.verbose:
                    print(f"[OK] Removed year tag from: {mp3_path}")
            else:
                if self.verbose:
                    print(f"[SKIP] No year tag found in: {mp3_path}")

        except MutagenError as e:
            print(f"[ERROR] Cannot process {mp3_path}: {e}")

    # === Function 'cleanfromfolder' ===
    def cleanfromfolder(self, folder_path):
        """
        Iterates through all MP3 files in a given folder and removes the 'date' tag from each.
        This is especially useful for batch cleaning music libraries or directories containing
        downloaded audio files. Only files with a `.mp3` extension (case-insensitive) are processed.

        Parameters:
        - folder_path (str): The path to the folder containing MP3 files to clean.

        Returns:
        - None
        """
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(".mp3"):
                fullpath = os.path.join(folder_path, filename)
                self.cleanfromfile(fullpath)


# === Callback ===
if __name__ == "__main__":
    """
    This script entry point provides a simple example of how to use the MP3TagCleaner class.
    When executed directly, it instantiates the cleaner with verbose mode enabled and demonstrates
    usage on both a single MP3 file and a full directory. Paths must be modified according to
    your local file system before execution.

    Parameters:
    - None

    Returns:
    - None
    """
    cleaner = MP3TagCleaner(verbose=True)

    # To clean one file
    cleaner.cleanfromfile(r"C:\Users\YourName\Music\song.mp3")

    # To clean all MP3s in a folder
    cleaner.cleanfromfolder(r"C:\Users\YourName\Music")
