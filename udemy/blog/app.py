blogs = dict()  #blog_name : Blog object

def menu():
    '''
    show the user the available blogs
    let the user make a choice
    do something with that choice
    exit
    '''
    print_blogs()

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))
blogs = dict()  #blog_name : Blog object

def menu():
    '''
    show the user the available blogs
    let the user make a choice
    do something with that choice
    exit
    '''
    print_blogs()

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))
