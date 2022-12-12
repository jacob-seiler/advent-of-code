from pathlib import Path

path = (Path(__file__).parent / "./q8.txt").resolve()
data = []

with open(path) as f:
    for line in f:
        line = line.strip()
        
        sigs, outs = line.split(" | ")
        sigs = sigs.split(" ")
        outs = outs.split(" ")

        data.append({"signals": sigs, "outputs": outs})

total = 0

for line in data:
    signals = line["signals"]
    display = [None] * 10

    for sig in signals:
        # Number 1
        if len(sig) == 2:
            display[1] = sig
            continue
        
        # Number 7
        if len(sig) == 3:
            display[7] = sig
            continue
        
        # Number 4
        if len(sig) == 4:
            display[4] = sig
            continue
        
        # Number 8
        if len(sig) == 7:
            display[8] = sig
            continue
    
    # Number 3
    for sig in signals:
        if len(sig) == 5:
            if display[1][0] in sig and display[1][1] in sig:
                display[3] = sig
                break
    
    # Number 9
    for sig in signals:
        if len(sig) == 6:
            present = True

            for seg in display[3]:
                if seg not in sig:
                    present = False

            if present:
                display[9] = sig
                break
    
    # Number 5
    for sig in signals:
        if len(sig) == 5:
            wrong = 0

            for seg in display[3]:
                if seg not in sig:
                    wrong += 1

            if wrong == 1:
                display[5] = sig
                break
    
    # Number 2
    for sig in signals:
        if len(sig) == 5:
            if sig != display[3] and sig != display[5]:
                display[2] = sig
                break

    # Numbers 0
    for sig in signals:
        if len(sig) == 6:
            if sig == display[9]:
                continue

            present = True

            for seg in display[7]:
                if seg not in sig:
                    present = False
            
            if present:
                display[0] = sig
                break

    # Number 6
    for sig in signals:
        if len(sig) != 6:
            continue

        if sig == display[9] or sig == display[0]:
            continue

        display[6] = sig
        break

    segments = [None] * 7

    # A
    for seg in display[7]:
        if seg not in display[1]:
            segments[0] = seg
            break

    # B
    for seg in display[8]:
        if seg not in display[6]:
            segments[1] = seg
            break

    # E
    for seg in display[8]:
        if seg not in display[9]:
            segments[4] = seg
            break

    # G
    for seg in display[8]:
        if seg not in display[0]:
            segments[6] = seg
            break

    # F
    for seg in display[8]:
        if seg not in display[3] and seg != segments[4]:
            segments[5] = seg
            break

    # D
    for seg in display[8]:
        if seg not in display[4] and seg != segments[0] and seg != segments[4]:
            segments[3] = seg
            break

    # C
    for seg in display[1]:
        if seg != segments[1]:
            segments[2] = seg
            break

    outs = line["outputs"]
    result = []

    for out in outs:
        segs = []

        for letter in out:
            segs.append(segments.index(letter))
        
        # Decode segments into numbers
        segs = sorted(segs)
        val = None

        if len(segs) == 2:
            val = 1

        if len(segs) == 3:
            val = 7

        if len(segs) == 4:
            val = 4

        if len(segs) == 5:
            if segs == [0, 1, 2, 3, 6]:
                val = 3
            elif segs == [0, 1, 3, 4, 6]:
                val = 2
            else:
                val = 5

        if len(segs) == 6:
            if 1 not in segs:
                val = 6
            elif 4 not in segs:
                val = 9
            else:
                val = 0

        if len(segs) == 7:
            val = 8

        result.append(str(val))
    
    result = int(''.join(result))
    total += result

print(total)
