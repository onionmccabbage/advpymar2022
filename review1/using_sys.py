import sys # we now have access to ascpects of the platform we are running on
print(sys.version) # what version of Python
print(sys.path) # where will Python looks for imports
print(sys.platform) # what os
print(sys.base_prefix)

# system arguments (sys.argv[0] is always the current module name)
print(sys.argv)