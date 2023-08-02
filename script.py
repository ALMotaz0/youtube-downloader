from pytube import YouTube

link = str(input("Enter your Link : "))
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
print("Download successful !")