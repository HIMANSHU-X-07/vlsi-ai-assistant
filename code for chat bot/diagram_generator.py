from openai import OpenAI
import base64
from io import BytesIO
from PIL import Image

client = OpenAI()

def generate_diagram(topic):
    prompt = f"""
    Create a clean, academic, black-and-white technical diagram for:
    {topic}

    Rules:
    - White background
    - Clear labels
    - Simple lines
    - No artistic style
    - Suitable for Electronics/VLSI textbooks
    """

    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    return Image.open(BytesIO(image_bytes))
