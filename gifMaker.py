import os       # used to get the video's path
import imageio


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

    # get video's data:
    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    print(f"Video's FPS: {fps}")

    # set generated_gif's data:
    writer = imageio.get_writer(outputPath, fps=fps)

    # append frames next to each other:
    print("Start converting into GIF ...")
    for frame in reader:
        writer.append_data(frame)

    print("Done!")
    writer.close()
