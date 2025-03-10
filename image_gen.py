from PIL import Image
import random

def create_composite_image(base_width, base_height, base_color, overlay_image_path, output_filename="composite_image.png"):

    try:
        base_img = Image.new("RGB", (base_width, base_height), base_color)

        overlay_img = Image.open(overlay_image_path).convert("RGBA")

        overlay_img = overlay_img.resize((base_width, base_height), Image.LANCZOS)

        base_img = base_img.convert("RGBA")

        base_img = Image.alpha_composite(base_img, overlay_img)


        # Save the composite image
        base_img.save(output_filename)

    except FileNotFoundError:
        print(f"Error: Overlay image not found at '{overlay_image_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example Usage
    base_width = 200
    base_height = 200
    base_color = (random.randint(0,255), random.randint(0, 255), random.randint(0,255))

    overlay_image_path = "overlay.png"

    output_filename = "output.png"

    create_composite_image(base_width, base_height, base_color, overlay_image_path, output_filename)