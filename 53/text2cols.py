COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
    newlines (\n\n) in text determines the amount of columns.
    Return a string with the column output like:
    line1\nline2\nline3\n ... etc ...
    See also the tests for more info."""

    # split text into len(text)//COL_WIDTH
    rows = (len(text) // COL_WIDTH)

    start = 0 - COL_WIDTH
    end = 0

    cols = []

    for i in range(rows + 1):
        cols.append(text[start:end])
        start += COL_WIDTH
        end += COL_WIDTH
    return r''.join(cols)

print(text_to_columns("""My house is small but cosy.

    It has a white kitchen and an empty fridge.

    I have a very comfortable couch, people love to sit on it."""))