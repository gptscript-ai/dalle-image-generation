# cli.py
import os
import argparse
from openai import OpenAI

client = OpenAI()

def main():
    parser = argparse.ArgumentParser(description="OpenAI API CLI for image generation prompt")
    parser.add_argument('-k', '--api-key', type=str, default=os.environ.get('OPENAI_API_KEY'),
                        help='OpenAI API key. Can also be set with OPENAI_API_KEY environment variable.')
    parser.add_argument('-p', '--prompt', type=str, required=True, help='Prompt for image generation.')
    parser.add_argument('-m', '--model', type=str, default='dall-e-3',
                        help='Model to use for image generation. Default is "default-model" or specify a different model.')
    parser.add_argument('-s', '--size', type=str, default='1024x1024',
                        help='Size of the image to generate, format WxH (e.g. 1024x1024). Default is 1024x1024.')
    parser.add_argument('-q', '--quality', type=str, default='standard',
                        help='Quality of the generated image. Default is "standard"')
    parser.add_argument('-n', '--number', type=int, default=1,
                        help='Number of images to generate. Default is 1.')

    args = parser.parse_args()

    if not args.api_key:
        parser.error('The --api-key argument is required if OPENAI_API_KEY environment variable is not set.')

    print(
        generate_prompt(args.api_key, args.prompt, args.model, args.size, args.quality, args.number)
    )

# Generate image from prompt
def generate_prompt(api_key, prompt, model="dall-e-3", size="1024x1024", quality="standard", n=1):
    response = client.images.generate(
      model=model,
      prompt=prompt,
      size=size,
      quality=quality,
      n=n,
    )

    # build an array of image urls
    return [image.url for image in response.data]

if __name__ == "__main__":
    main()
