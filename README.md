# Ficbook Downloader Script

Script to download fanfiction entries from ficbook.net in bulk.

## Setting up

Python should already be installed. This project is tested on Python 3.12. You may use other versions as you will, but YMMV.

Clone the repo / download code.

Create `fic_list.txt` text file in the root folder and place up to 10 entry IDs (see [Limitations section](#limitaitions)) in the file, one ID on a line, e.g:

```
018aaeda-ad9b-724e-a05b-216f3abb1e57
018b609d-e380-70dc-a9a7-79cdcd8751eb
018baa3b-9266-77ce-9024-85cf5e8e2e33
...
```

Be sure to read the [Limitations](#limitaitions) section and you're good to go. 

## Limitations

- Downloading is only allowed for registered users, so you will need and account on the website. Furthermore, since the script works by opening browser tabs, you need to log in your current browser before running the downloader script.
- Ficbook only allows downloading up to 10 entries per day, so if you'd like to download more, you'll need to run downloader a couple of times over the course of several days. It might be possible to bypass this by using several accounts, but that's not recommended.
- Downloader isn't intended to be fully automatic, you should watch the process as ficbook might (and most likely will) ask you to confirm you're human (by chencking a checkmark captcha).

## Running the script

Once you're logged in and have your IDs in the `fic_list.txt` file, open a new browser window (optional, recommended for convenience) and run the script:

```python
python ficbook_downloader.py
```

Enjoy your donwloaded files.

### Optional arguments

- `-f`, `--format` - specify download format (epub, txt, pdf or fb2). Default is epub.
- `-s`, `--silent` - do not ping after the script is finished.