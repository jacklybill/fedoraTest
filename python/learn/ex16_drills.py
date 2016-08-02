from sys import argv

script, filename = argv

print "enter your filename"
file = raw_input("> ")
files = open(file)
print files.read() 

