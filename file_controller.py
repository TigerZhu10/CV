import os

def load_template(file_name):
    with open(file_name,'r', encoding = 'utf-8') as f:
        return f.read()
    
    
#这个是加载内容：
base = load_template('./templates/home_page/base.html')
nav_bar = load_template('./templates/home_page/nav-bar.html')
background_top = load_template('./templates/home_page/background-top.html')
about_me = load_template('./templates/home_page/about-me.html')
accomplishments = load_template('./templates/home_page/accomplishments.html')
skills = load_template('./templates/home_page/skills.html')
alarm_clock = load_template('./templates/projects/arduino-alarm-clock.html')
feed_the_dragon = load_template('./templates/projects/feed-the-dragon.html')
personal_website = load_template('./templates/projects/personal-website.html')
footer = load_template('./templates/home_page/footer.html')

#此处进行替换
index = base.replace('{{nav-bar}}', nav_bar)
index = index.replace('{{background-top}}', background_top)
index = index.replace('{{about-me}}', about_me)
index = index.replace('{{accomplishments}}', accomplishments)
index = index.replace('{{skills}}', skills)
index = index.replace('{{arduino-alarm-clock}}', alarm_clock)
index = index.replace('{{feed-the-dragon}}', feed_the_dragon)
index = index.replace('{{personal-website}}', personal_website)
index = index.replace('{{footer}}', footer)


#把替换的结果存到index.html里
with open('index.html', 'w', encoding = 'utf-8') as f:
    f.write(index)