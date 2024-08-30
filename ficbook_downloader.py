import webbrowser
from argparse import ArgumentParser
from time import sleep


def main():
	parser = ArgumentParser(
		description="Script to download fanfiction entries from ficbook.net in bulk."
	)
	parser.add_argument(
		"-f",
		"--format",
		choices=["epub", "txt", "pdf", "fb2"],
		help="file format of downloaded files",
		default="epub"
	)
	parser.add_argument(
		"-s",
		"--silent",
		help="do not ping after downloads are finished",
		action="store_true"
	)

	args = parser.parse_args()

	try:
		with open("fic_list.txt") as file:
			fanfic_ids = file.read().split("\n")
	except FileNotFoundError as e:
		raise(e)

	sleep_counter = 0
	download_format = args.format
	for fanfic_id in fanfic_ids:
		link = f"https://ficbook.net/fanfic_download/{fanfic_id}/{download_format}"
		webbrowser.open(link)

		sleep(10)
		sleep_counter += 1
		if sleep_counter > 4:
			sleep(60)
			sleep_counter = 0

	print("Done!")
	if not args.silent:
		print("\a")

if __name__ == '__main__':
	main()