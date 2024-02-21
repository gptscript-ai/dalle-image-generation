# cli.py
import os
import sys
import logging
import argparse
import openai
from openai import OpenAI
client = OpenAI()

def main():
    parser = argparse.ArgumentParser(description="OpenAI API CLI for image generation prompt")
    parser.add_argument('-k', '--api-key', type=str, default=os.environ.get('OPENAI_API_KEY'),
                        help='OpenAI API key. Can also be set with OPENAI_API_KEY environment variable.')
    parser.add_argument('-p', '--prompt', type=str, required=True, help='Prompt for image generation.')
    parser.add_argument('-m', '--model', type=str, default='dall-e-3',
                        help='Model to use for image generation. Default is "dall-e-3".')
    parser.add_argument('-s', '--size', type=str, default='1024x1024',
                        help='Size of the image to generate, format WxH (e.g. 1024x1024). Default is 1024x1024.')
    parser.add_argument('-q', '--quality', type=str, choices=['standard', 'hd'], default='standard',
                        help='Quality of the generated image. Allowed values are "standard" or "hd". Default is "standard"')
    parser.add_argument('-n', '--number', type=int, default=1,
                        help='Number of images to generate. Default is 1.')
    args = parser.parse_args()

    if not args.api_key:
        parser.error('The --api-key argument is required if OPENAI_API_KEY environment variable is not set.')

    # Reach out to the OpenAI API
    try:
        response = client.images.generate(
            model=args.model,
            prompt=args.prompt,
            size=args.size,
            quality=args.quality,
            n=args.number,
        )
        print([image.url for image in response.data])
    except openai.OpenAIError as e:
        print(f"Recieved an error code while generating images: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
