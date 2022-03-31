pt = {'Hydrogen':1, 'Helium':2}

# default only sets if NOT already in the dict
carbon = pt.setdefault('Carbon', 12)
helium = pt.setdefault('Helium', 'squeaky voice') # does not replace the pre-existing value

print(pt)