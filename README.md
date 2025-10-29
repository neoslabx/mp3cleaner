# MP3Cleaner - Year Tags Remover

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**MP3Cleaner** remove unwanted "year" (`date`) tags from MP3 files using a simple Python utility powered by Mutagen. Clean individual files or entire folders with optional verbose logging.

* * *

## Features

- Remove `date` (year) tag from MP3 metadata
- Clean individual MP3 files or entire directories
- Optional verbose logging
- Built using `mutagen.easyid3` and `mutagen.id3`
- Lightweight and dependency-light

* * *

## Requirements

- Python 3.6+
- [mutagen](https://pypi.org/project/mutagen/)

Install Mutagen with pip:

```bash
pip install mutagen
````

* * *

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/neoslabx/mp3cleaner
cd mp3cleaner
```

### 2. Run the Script

```bash
python mp3cleaner.py
```

### 3. Example: Clean a Single File

```python
cleaner.cleanfromfile(r"C:\Users\YourName\Music\song.mp3")
```

### 4. Example: Clean All MP3s in a Folder

```python
cleaner.cleanfromfolder(r"C:\Users\YourName\Music")
```

* * *

### File Structure

```
mp3cleaner.py       # Main script containing MP3Cleaner class
README.md           # Project documentation
```

* * *

### Example Output

```text
[OK] Removed year tag from: C:\Users\YourName\Music\song1.mp3
[SKIP] No year tag found in: C:\Users\YourName\Music\song2.mp3
[ERROR] Cannot process C:\Users\YourName\Music\badfile.mp3: ...
```

* * *

### Why Use It?

* Eliminate unnecessary or incorrect `year` metadata from MP3s
* Standardize your media files for automation tools or streaming
* Quickly clean up messy downloads and audio archives

* * *

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request with a clear description of your changes.

Ensure your code follows PEP 8 style guidelines and includes appropriate tests.

* * *

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

* * *

## Contact

For any issues, suggestions, or questions regarding the project, please open a new issue on the official GitHub repository or reach out directly to the maintainer through the [GitHub Issues](issues) page for further assistance and follow-up.