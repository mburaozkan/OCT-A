import json

from oct_converter.readers import FDA

# a sample .fda file can be downloaded from the Biobank resource here:
# https://biobank.ndph.ox.ac.uk/showcase/refer.cgi?id=31
filepath = "./192784.fda"
fda = FDA(filepath)

oct_volume = (
    fda.read_oct_volume()
)  # returns an OCT volume with additional metadata if available
oct_volume.peek(show_contours=True)  # plots a montage of the volume
oct_volume.save("./results/fda_testing.avi")  # save volume as a movie
oct_volume.save(
    "./results/fda_testing.png"
)  # save volume as a set of sequential images, fds_testing_[1...N].png

fundus_image = (
    fda.read_fundus_image()
)  # returns a  Fundus image with additional metadata if available
fundus_image.save("./results/fda_testing_fundus.jpg")

fundus_grayscale_image = fda.read_fundus_image_gray_scale()
if fundus_grayscale_image:
    fundus_grayscale_image.save("./results/fda_testing_grayscalefundus.jpg")

# Read segmentation (contours)
segmentation = fda.read_segmentation()

# extract all other metadata
metadata = fda.read_all_metadata()
with open("metadata.json", "w") as outfile:
    outfile.write(json.dumps(metadata, indent=4))