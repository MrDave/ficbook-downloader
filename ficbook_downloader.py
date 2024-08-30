import webbrowser
from time import sleep


def main():
	try:
		with open("fic_list.txt") as file:
			fanfic_ids = file.read().split("\n")
	except FileNotFoundError as e:
		raise(e)
	sleep_counter = 0
	for id in fanfic_ids:
		link = f"https://ficbook.net/fanfic_download/{id}/epub"
		webbrowser.open(link)

		sleep(10)
		sleep_counter += 1
		if sleep_counter > 4:
			sleep(60)
			sleep_counter = 0


if __name__ == '__main__':
	main()