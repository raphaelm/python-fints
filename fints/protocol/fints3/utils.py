def segments_to_ascii(segments, counter=1):
    ascii = ''

    for segment in segments:
        # do only set counter if is 0; see B.8
        if segment.get_counter() == 0:
            counter += 1
            segment.set_counter(counter)

        s = segment.to_ascii()
        ascii += s + "'"

    return counter, ascii
