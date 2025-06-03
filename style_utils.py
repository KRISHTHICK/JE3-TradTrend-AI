import random

def detect_traditional_elements(image):
    # Simulated traditional features based on image
    elements = ["Zari Border", "Paisley Motif", "Chikankari Embroidery", "Banarasi Weave"]
    return random.sample(elements, k=2)

def suggest_fusion_styles(elements):
    style_map = {
        "Zari Border": "Add a denim jacket to contrast the shimmer",
        "Paisley Motif": "Use paisley on sneakers or bucket hats",
        "Chikankari Embroidery": "Pair with wide-leg cargo pants",
        "Banarasi Weave": "Transform the weave into a crop top with culottes"
    }
    output = ""
    for el in elements:
        output += f"- **{el}**: {style_map.get(el, 'Try blending with a minimal silhouette')}  \n"
    return output
