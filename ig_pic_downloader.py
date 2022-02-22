import os,platform
import instaloader
from datetime import datetime

def url_download():
    url = input("URL shortcode: ")
    post = instaloader.Post.from_shortcode(L.context, url)
    L.download_post(post,target="URL")

def login_ig():
    print("Please login your instagram account !")
    local_user = input("User Name:")
    local_pwd = input("Password:")
    os.system(os_clear[my_os])
    L.login(local_user,local_pwd)

def back_init():
    global profile
    global username
    global profile_id
    username = input("Instagram_ID:")
    profile = instaloader.Profile.from_username(L.context, username)
    profile_id = L.check_profile_id(username)
    
    
    if os.path.exists(ins_pics+os_slash[my_os]+username+os_slash[my_os]+username+os_slash[my_os]+username+".jpg"):
        print("thumbnail exists.")
    else:
        os.chdir(ins_pics+os_slash[my_os]+username) #create a directory for thumbnail + download
        L.download_profilepic(profile)  #profile picture

    os.chdir(ins_pics+os_slash[my_os]+username+os_slash[my_os]+username)

    try:
        os.rename(os.listdir()[0],username+".jpg")    
    except:
        pass
    
    os.chdir(ins_pics)
    tmp = []
    tmp.append(profile_id.userid)
    #print(tmp)
        
    #Read the profile posts and downloads those containing the hashtags
    #followers = profile.followers
    #followees = profile.followees
    #post_count=profile.get_posts().count
    #biography = profile.biography

    #print(username +" has "+str(followers)+" followers and "+str(followees)+"  followees\nPosts = "+str(post_count)+"\n"+biography)

        

def post_search():
    t_y=int(input("Year: "))
    t_m=int(input("Month: "))
    t_d=int(input("Day: "))
    posts = profile.get_posts() #get all post from a user
    UNTIL=datetime(t_y,t_m,t_d)
    uto=datetime(t_y,t_m,t_d+1)
     # specific day post til now
    for post in posts:
        if post.date_utc>=UNTIL and post.date_utc<uto:
            print(post.date_utc)
            L.download_post(post,target=username)
        if post.date_utc<UNTIL:  #break the loop for not costing a lot of time
            break

def story_search():
    for story in L.get_stories(userids=tmp):
            # story is a Story object
        for item in story.get_items():
        # item is a StoryItem object
            L.download_storyitem(item, username)

def highlight_search():
    for highlight in L.get_highlights(profile_id.userid):
    # highlight is a Highlight object
        for item in highlight.get_items():
        # item is a StoryItem object
            print(item)
            #L.download_storyitem(item, username)

#=======================================================================================
locate = os.getcwd()
os_slash= {"Windows":"\\","Linux":"/","macOS":"/"}
os_clear= {"Windows":"cls","Linux":"clear","macOS":"clear"}
my_os = platform.system()


ins_pics = locate+os_slash[my_os]+"ins_pics"

if os.path.exists(ins_pics) ==False:
    os.mkdir(ins_pics)
os.chdir(ins_pics)
#print(os.getcwd())
L = instaloader.Instaloader(compress_json=False,save_metadata=False)
search = input("1.Global search 2.Private search: ")
if search =="1": #global
    url_or_person = input("1.Person 2.URL : ")
    if url_or_person=="1":
        
        mode = input("1.post 2.stories 3.highlights : ")
        if mode == "1":
            back_init()
            post_search()
        if mode == "2":
            back_init()
            story_search()
        if mode == "3":
            back_init()
            highlight_search()
    if url_or_person=="2": #global URL
        url_download()

if search=="2": #private
    login_ig()
    mode = input("1.post 2.stories 3.highlights : ")
    if mode == "1":
        back_init()
        post_search()
    if mode == "2":
        back_init()
        story_search()
    if mode == "3":
        back_init()
        highlight_search()

L.close()
print("Download complete.")

    
    

#Load the UserName





