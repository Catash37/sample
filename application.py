from flask import Flask

def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

header_text = '''
    <html>\n<head> <title> EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''

application = Flask(__name__)

application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

if __name__ == "__main__":
    application.debug = True
    application.run()