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
        # uncomment line below to see how script works
        # print(f'{text[:start]}[{text[start:start+width]}]{text[start+width:]}','|', sample)
        samplecount = text[start:].count(sample)
        if samplecount == 1:
            if width > 1:
                start += width-1
                width = 1
            else:
                start += 1
        else:
            procent = int(samplecount * len(sample) / len(text) * 100)
            if procent > maxprocent:
                maxprocent = procent
                maxsample = sample
                maxsamplecount = samplecount
                if maxprocent >= 80:
                    break
            width += 1

    return {'sample':maxsample, 'procent':maxprocent, 'count':maxsamplecount}

text = input('text here: ')
print(analyze(text))
