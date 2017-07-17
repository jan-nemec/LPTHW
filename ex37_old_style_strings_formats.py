# Old Style String Formats

# %d | 	Decimal integers (not floating point).
print("%d" % 47)
print("%d" % 47.8)

# %i | Same as %d
print("%i" % 47.5)

# %o | octal number
print("%o" % 1000)

# %u | unsigned decimal
print("%u" % -1000)

# %x | hexadecimal lowercase
print("%x" % 1000 )

# %X | Hexadecimal uppercase
print("%X" % 1000 )

# %e | Exponential notation, lowercase 'e'
print("%e" % 1000)

# %E | Exponential notation, lowercase 'E'
print("%E" % 1000)

# %f or %F | Floating point real number
print("%f" % 10.34)
print("%F" % 10.34)

# %g | Either %f or %e, whichever is shorter
print("%g" % 10.34)

# %g | Either %f or %e, whichever is shorter
print("%G" % 10.34)

# %c | Character format
print("%c" % 34) # "

# %r | repr format (debugging format)
print("%r" % int) # <class 'int'>

# %s | String format
print("%s there" % "hi")

# %% | A percent sign
print("%g%%" % 10.34)