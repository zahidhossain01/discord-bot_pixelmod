import PIL.Image as Image
import tqdm
import hashlib

# progress bar: https://github.com/tqdm/tqdm

# https://stackoverflow.com/questions/50815632/saving-image-twice-using-pil
# https://github.com/Ovyerus/deeppyer/blob/master/deeppyer/__init__.py


def md5sum(fn):
    hasher = hashlib.md5()
    with open(fn, 'rb') as f:
        hasher.update(f.read())
        return hasher.hexdigest()

def generate_gif_frames(img:Image.Image, n, quality, subsampling):
    frames = [img]
    hash_set = set()


    for i in tqdm.trange(1,n):
        filepath = "gif_scratch/test"+str(i)+".jpg"
        frames[i-1].save(filepath, quality=quality, subsampling=subsampling)
        img_i = Image.open(filepath)
        frames.append(img_i)

        md5 = md5sum(filepath)
        if md5 in hash_set:
            print(f"Stopped at iteration #{i}")
            break
        hash_set.add(md5)
        

    return frames
    

if __name__ == "__main__":
    filepath = "TestImages/kchw_20220905_010006_square_c.jpg"
    img_file = open(filepath, "rb")

    img = Image.open(img_file)
    quality = 50
    subsampling = 2
    iterations = 1000
    frames = generate_gif_frames(img, iterations, quality, subsampling)

    total_duration = 5000
    frame_duration = total_duration // len(frames)

    # TODO: maybe gif isn't the move for this... ffmpeg video stitch?

    # frames[0].save("test.gif", save_all=True, append_images=frames[1:], duration=frame_duration, loop=0)
    
    