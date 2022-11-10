MENU_PROMPT = 'Input "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, "q" to quit: '
blogs = dict()  #blog_name : Blog object

def menu():
    '''
    show the user the available blogs
    let the user make a choice
    do something with that choice
    exit
    '''
    print_blogs()
    selection = input(MENU_PROMPT)
def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))
blogs = dict()  #blog_name : Blog object
