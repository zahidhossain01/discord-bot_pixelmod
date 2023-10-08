import PIL.Image as Image
import numpy as np
import os

# BOT NOTES:
# https://support-dev.discord.com/hc/en-us/articles/6381892888087-Bots-Buttons
# https://discord.com/blog/slash-commands-are-here


def pixelrandomize(I):
    patch = np.copy(I)
    original_patch_shape = patch.shape
    patch = patch.reshape((-1,3))

    np.random.shuffle(patch)

    patch = patch.reshape(original_patch_shape)
    return patch

def pixelsort(I):
    patch = np.copy(I)
    original_patch_shape = patch.shape
    patch = patch.reshape((-1,3))

    luminance = 0.299*patch[:,0]+0.587*patch[:,1]+0.114*patch[:,2]
    order = np.argsort(luminance)
    patch = patch[order]

    patch = patch.reshape(original_patch_shape)
    return patch

def pixelmod(I, W):
    window_height = W[0]
    window_width = W[1]
    img_height = I.shape[0]
    img_width = I.shape[1]

    idx_h = 0
    idx_v = 0
    while (idx_v < img_height):

        bound_left = idx_h
        bound_right = idx_h+window_height
        bound_top = idx_v
        bound_bottom = idx_v+window_height

        if(bound_right > img_width):
            bound_right = img_width
        if(bound_bottom > img_height):
            bound_bottom = img_height

        slice_h = slice(bound_left, bound_right)
        slice_v = slice(bound_top, bound_bottom)
        patch_slice = np.s_[slice_v, slice_h]

        patch = pixelrandomize(I[patch_slice])
        I[patch_slice] = patch

        idx_h += window_width
        if(idx_h >= img_width):
            idx_v += window_height
            idx_h = 0
    

if __name__ == "__main__":
    filepath = "Images/figures.jpg"
    # TODO: take command line arg for filepath (save in same folder as script? output dest flag too i guess)
    # TODO: use argparse library? or optparse? whichever better
    
    img_file = open(filepath, "rb")
    src_filename = os.path.basename(filepath)
    scrambled_filename = "s_" + src_filename
    scrambled_filepath = os.path.join("Images", scrambled_filename)

    I = Image.open(img_file)
    I = np.asarray(I, dtype=np.uint8)
    I_mod = np.copy(I)
    pixelmod(I_mod, (10,10))
    img_s = Image.fromarray(I_mod)
    img_s.save(scrambled_filepath, quality=95, subsampling=0)

    # TODO: gif! (or video frames?)
    # TODO: discord bot!
    # TODO: vector op / multithreaded way of scrambling each segment? | test single vs multi thread speed
