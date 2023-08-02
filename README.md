# prntsc
`Prntsc` is a powerful Python web scraper tailored specifically for downloading images from `prnt.sc` with ease.

This versatile script allows you to effortlessly generate a specified number of URLs and automatically download the corresponding screenshots. 
The script is designed to be asynchronous, enabling it to download multiple images simultaneously.

With Prntsc at your disposal, you can efficiently collect images from prnt.sc, making it an indispensable tool for your web scraping tasks.

## Requirements
The script is optimized for `Python 3.11`, and it also supports `Python 3.6` and higher.
After ensuring you have `Python 3.11`, you can install the required packages by running the following command in your terminal or command prompt:
```
pip install -r requirements.txt
```

## Usage
From terminal, run `python3 main.py`, followed by the number of images to be generated.
When using this script, if you do not specify the number of pictures to be downloaded, the default number will be set to 10.

### Example
To generate four images:
```
python main.py 4
```

If four URLs are to be generated:
```
https://prnt.sc/0uscjl
https://prnt.sc/huepok
https://prnt.sc/or2b5s
https://prnt.sc/gipq0v
```
The image on each of these URLs will then be opened and saved.

### Disclaimer
This script is intended solely for educational purposes. It is essential to clarify that neither I nor this script are associated with `prnt.sc` in any capacity. It is crucial to understand that this script does not determine the appropriateness of any images for certain users. 
Therefore, it is strongly advised that viewers and users exercise discretion while using this script. Additionally, I explicitly state that I am not accountable for the manner in which this script is utilized.