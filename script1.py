import os
import sys
from subprocess import call

path = "practica_creativa2/bookinfo/src/productpage"

call(["sudo", "apt", "install", "-y", "python3-pip"])
call(["sudo", "apt-get", "install", "-y", "git"])
call(["git", "clone",
"https://github.com/CDPS-ETSIT/practica_creativa2.git"])

os.environ["GROUP_NUMBER"] = "41"

print(os.environ["GROUP_NUMBER"])

with open("{}/templates/productpage.html".format(path), "r") as f:
	data = f.readlines()

data[33] = """\n<a class="navbar-brand" href="#">BookInfo Sample. Grupo
{}</a>\n""".format(os.environ["GROUP_NUMBER"])
print(data)

with open("{}/templates/productpage.html".format(path), "w") as f:
	f.writelines(data)

call(["pip3", "install", "-r", "{}/requirements.txt".format(path), "-v"])
call(["python3", "{}/productpage_monolith.py".format(path), "9080"])
