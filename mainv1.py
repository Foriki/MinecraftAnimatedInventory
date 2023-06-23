from PIL import Image, ImageSequence
import os
def resize(im, size,fps):
    frames = ImageSequence.Iterator(im)
    resized_frames = []
    for frame in frames:
        resized_frame = frame.copy()
        resized_frame = resized_frame.resize(size, Image.LANCZOS)
        resized_frames.append(resized_frame)
    resized_frames[0].save("out.gif", save_all=True, append_images=resized_frames[1:], loop=0, duration=fps)
    return Image.open("out.gif")

def create_inventory(gif_path, fps):
    # Open the GIF file
    effects_image = Image.open("effects.png")
    overlay_image = Image.open("overlay.png")

    gif = Image.open(gif_path)
    gif = resize(gif, overlay_image.size,fps)
    frames = []
    count = 0
    # Extract frames at specified FPS
    for i, frame in enumerate(ImageSequence.Iterator(gif)):
        if i % fps == 0:
            count += 1
            frame_with_overlay = frame.copy()
            frame_with_overlay.paste(overlay_image, (0, 0), mask=overlay_image)
            frames.append(frame_with_overlay)
    
    width = 512  # i am not sure why 512, the pack i originally took inspiration from also had dead space on the right, it as also 512 with the exact overlay.png
    height = gif.height * len(frames) + 180 * (len(frames))
    output = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    current_img_y = 0
    above_effects_offset=19
    for i, frame in enumerate(frames):
        frame_width, frame_height = frame.size

        resized_frame = frame.resize((width - 180, int(frame_height * (width - 180) / frame_width))).convert("RGBA")

        # Put at the top-left corner of the output
        output.paste(resized_frame, (0, current_img_y), mask=resized_frame)

        # Check if it is the last frame, doing this because
        # 1. sometime it doesnt add effects.png
        # 2. offset which is also fucked
        if i == len(frames) - 1:
            # Below effects
            output.paste(effects_image, (0, current_img_y + resized_frame.height + above_effects_offset))
            current_img_y += resized_frame.height  # + 1
        else:
            # Above effects
            output.paste(effects_image, (0, current_img_y + resized_frame.height + above_effects_offset))
            current_img_y += resized_frame.height + 180

    # fix dead space, sometimes 
    if(count%2==0):
        output_height = output.size[1] - 266  # 266 is normal is total image size(of each frame), I'm leaving the extra 8
        output = output.crop((0, 0, width, output_height))

    output.save("output.png")
    print(count)
    print("Vertical output created successfully.")



# Example usage
gif_path = input("enter path to gif (..\Desktop\\a.gif): ")
fps = 5
#fps = int(input("enter fps(need to fix): ")) do not question why its fucked nor do i know how and why

create_inventory(gif_path, fps)
os.remove("out.gif")
