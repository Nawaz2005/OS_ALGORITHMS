def optimalPage(pages, capacity):
    frames = []
    page_faults = 0

    for page in pages:
        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
            else:
                # Find the index of the page that will not be used in the future
                future_pages = pages[pages.index(page)+1:]
                indexes = {frame:future_pages.index(frame) if frame in future_pages else len(future_pages) for frame in frames}
                page_to_replace = max(indexes, key=indexes.get)
                frames[frames.index(page_to_replace)] = page
            page_faults += 1

    return page_faults

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4
r= optimalPage(pages, capacity)
print("fault:",r,"hit:",len(pages)-r)

