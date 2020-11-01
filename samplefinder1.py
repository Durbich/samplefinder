def analyze(text):
    sample = ''
    maxsample = ''
    maxsamplecount = 0
    procent = 0
    maxprocent = 0
    start = 0
    width = 1

    while (start + width*2) <= len(text):
        sample = text[start : start+width]
        samplecount = text[start:].count(sample)
        if samplecount == 1:
            start += width
            width = 1
        else:
            procent = int(samplecount * len(sample) / len(text) * 100)
            if procent > maxprocent:
                maxprocent = procent
                maxsample = sample
                maxsamplecount = samplecount
            width += 1

    return {'sample':maxsample, 'procent':maxprocent, 'count':maxsamplecount}

text = input('text here: ')
print(analyze(text))
