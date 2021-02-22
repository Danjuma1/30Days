def my_print(txt):
    print(txt)

msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you here.
"""

def format_msg(my_name="Justin", my_website="cfe.sh"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    # print(my_msg)
    return my_msg

def base_function(*args, **kwargs):
    print(args, kwargs)