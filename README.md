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
018bf84f-4dae-7915-838c-9bed73178f58
018c0d74-4068-7ec6-9d4c-80e8101a53b9
018c44f3-0676-7e44-8ca7-24ab3ba94f45
018c581a-2413-746f-a8d7-08a3d411fd9a
018c5449-2986-7086-8937-1ee8486bc9ab
018caf73-e256-7bbc-a93f-135d512a2bbd
018cff57-f297-72a6-86b3-857fcb1157e4
```

Be sure to read the [Limitations](#limitaitions) section and you're good to go. 

## Limitations

- Downloading is only allowed for registered users, so you will need and account on the website. Furthermore, since the script works by opening browser tabs, you need to log in your current browser before running the downloader script.
- Ficbook only allows downloading up to 10 entries per day, so if you'd like to download more, you'll need to run downloader a souple of times over the course of several days. It might be possible to bypass this by using several accounts, but that's not recommended.
- Downloader isn't intended to be fully automatic, you should watch the process as ficbook might (and most likely will) ask you to confirm you're human (by chencking a checkmark captcha).

## Running the script

Once you're logged in and have your IDs in the `fic_list.txt` file, open a new browser window (optional, recommended for convenience) and run the script:

```python
python ficbook_downloader.py
```

Enjoy your donwloaded files.