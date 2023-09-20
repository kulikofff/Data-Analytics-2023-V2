# Installed here - C:\Windows\System32\y
# Tutorial here - https://www.pyxll.com/docs/videos/worksheet-functions.html


from pyxll import xl_func

@xl_func
def hello(name):
    return "Hello, %s" % name

if __name__ == "__main__":
    print(hello())