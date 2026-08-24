import os
import asyncio
import aiohttp
from urllib.parse import quote
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("POLLINATIONS_API_KEY")

PROMPT_FILE = "prompts.txt"
OUTPUT_DIR = "output"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)


def read_prompts():
    """Read prompts from prompts.txt."""
    with open(PROMPT_FILE, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


async def generate_image(session, prompt, index):
    """Generate and save one image."""
    encoded_prompt = quote(prompt)

    url = (
        f"https://gen.pollinations.ai/image/"
        f"{encoded_prompt}?model=flux"
    )

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    filename = os.path.join(OUTPUT_DIR, f"image_{index}.png")

    try:
        async with session.get(url, headers=headers) as response:

            if response.status == 200:
                image_data = await response.read()

                with open(filename, "wb") as file:
                    file.write(image_data)

                print(f"✅ Saved: {filename}")

            else:
                error = await response.text()
                print(f"❌ Failed image {index}: HTTP {response.status}")
                print(error[:300])

    except Exception as error:
        print(f"❌ Error with image {index}: {error}")


async def main():

    if not API_KEY:
        print("❌ API key not found.")
        print("Check your .env file.")
        return

    prompts = read_prompts()

    if not prompts:
        print("❌ No prompts found in prompts.txt.")
        return

    print(f"Found {len(prompts)} prompts.")
    print("Starting image generation...\n")

    async with aiohttp.ClientSession() as session:

        tasks = [
            generate_image(session, prompt, index)
            for index, prompt in enumerate(prompts, start=1)
        ]

        await asyncio.gather(*tasks)

    print("\n🎉 Image generation completed!")


if __name__ == "__main__":
    asyncio.run(main())