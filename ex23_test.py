from sys import argv

script, to_file, encoding, errors = argv

indata = "Příliš žluťoučký kůň úpěl ďábelské ódy."
raw_bytes = indata.encode(encoding, errors=errors)
print(indata, "<===>", raw_bytes)

out_file = open(to_file, 'w')
out_file.write(f"{raw_bytes}")

print("\nAlright, all done.\n")
out_file.close()

raw_bytes2 = b'P\xc5\x99\xc3\xadli\xc5\xa1 \xc5\xbelu\xc5\xa5ou\xc4\x8dk\xc3\xbd k\xc5\xaf\xc5\x88 \xc3\xbap\xc4\x9bl \xc4\x8f\xc3\xa1belsk\xc3\xa9 \xc3\xb3dy.'
indata2 = raw_bytes2.decode(encoding, errors=errors)
print(indata2, "<===>", raw_bytes)