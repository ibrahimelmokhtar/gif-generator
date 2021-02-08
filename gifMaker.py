import os       # used to get the video's path


def gifMaker(inputPath, targetFormat='.gif'):
    # seperate video's file extension:
    outputPath = os.path.splitext(inputPath)[0]

    # customize directory of the resultant GIFs:
    outputPath = outputPath.split('\\')
    outputPath[-2] = 'GIFs'     # replace 'Videos' with 'GIFs'
    gifDirectory = '\\'.join(outputPath[:-1])         # create GIF's directory path
    outputPath = '\\'.join(outputPath)

    try:
        os.mkdir(gifDirectory)
    except:
        print("Directory already exists!")

    # add file's extension:
    outputPath = outputPath + targetFormat
    print(f"Converting\t: {inputPath}\nInto\t\t: {outputPath}")
