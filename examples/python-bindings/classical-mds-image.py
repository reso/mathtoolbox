import pymathtoolbox
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from scipy.spatial.distance import pdist, squareform

# Load an image
image = Image.open("../assets/autumn-leaves.jpg")
resized_image = image.resize((30, 20), Image.BILINEAR)

# Generate a color array
colors = np.asarray(resized_image)
colors = colors.reshape(colors.shape[0] * colors.shape[1], 3) / 255.0

# Generate a distance matrix
D = squareform(pdist(colors))

# Compute metric MDS (embedding into a 2-dimensional space)
X = pymathtoolbox.compute_classical_mds(D=D, dim=2)

# Define constants for plot
FIG_SIZE = (8, 4)
IMAGE_FORMAT = "png"
DPI = 200

# Set style
sns.set()
sns.set_context()
plt.rcParams['font.sans-serif'] = ["Linux Biolinum"]

# Draw plot
fig = plt.figure(figsize=FIG_SIZE, dpi=DPI)

ax = fig.add_subplot(1, 2, 1)
ax.set_title("Target Image")
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_yticks([])
ax.imshow(image)

ax = fig.add_subplot(1, 2, 2)
ax.set_title("Pixel Colors Embedded into 2D")
ax.set_xticklabels([])
ax.set_yticklabels([])
num_pixels = colors.shape[0]
for i in range(num_pixels):
    ax.plot(X[0][i], X[1][i], color=colors[i], marker=".")

# Export plot
fig.tight_layout()
fig.savefig("./classical-mds-image-out." + IMAGE_FORMAT)
