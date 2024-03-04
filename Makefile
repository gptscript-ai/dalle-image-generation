bootstrap:
	python3 -m venv .venv
	. .venv/bin/activate; pip3 install -r requirements.txt

readme:
	gptscript scripts/update-readme.gpt

tool-file:
	gptscript scripts/update-tool-file.gpt

validate: readme tool-file
