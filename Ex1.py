text = "X-DSPAM-Confidence:    0.8475"
p = text.find(':')
#print (p)
lp = text.find('5')
#print (lp)

answer = text[p+1 : lp+1]
#print (answer)

a = answer.strip()

print (a)
