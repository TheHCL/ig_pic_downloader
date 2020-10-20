import os
import instaloader
from datetime import datetime

locate = os.getcwd()
ins_pics = locate+"\\ins_pics"
# Get instance
if os.path.exists(ins_pics) ==False:
    os.mkdir(ins_pics)
os.chdir(ins_pics)
L = instaloader.Instaloader()
search = input("1.Global search 2.Private search : ")
if search=="2":
    print("Please login your instagram account !")
    local_user = input("User Name:")
    local_pwd = input("Password:")
    os.system("cls")
    L.login(local_user,local_pwd)



#Load the UserName


username = input("Instagram_ID:")
t_y=int(input("Year: "))
t_m=int(input("Month: "))
t_d=int(input("Day: "))
profile = instaloader.Profile.from_username(L.context, username)
post_iterator = profile.get_posts()
#Read the profile posts and downloads those containing the hashtags
followers = profile.followers
followees = profile.followees
post_count=profile.get_posts().count
biography = profile.biography

#print(username +" has "+str(followers)+" followers and "+str(followees)+"  followees\nPosts = "+str(post_count)+"\n"+biography)
#L.download_profilepic(profile)  #profile picture
x=datetime.now()
print(t_y,t_m,t_d)


for post in post_iterator:
    #print("like count:",post.likes) 
    #print("comment count",post.comments)
    #print(post.caption) #pcaption只會給前段內文，如果要完整內文用caption
    if post.date_utc>=datetime(t_y,t_m,t_d): #and post.date_utc<=datetime(x.year,x.month,x.day) :
        L.download_post(post,target="search")
    

