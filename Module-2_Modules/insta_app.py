import instaloader

insta=instaloader.Instaloader()

userid=input("Enter your insta ID:")

#insta.download_profile(userid,profile_pic_only=True)

insta.download_profile(userid,profile_pic_only=False)

