# 🎩SubSnipe🎩
SubSnipe is a powerful Python tool designed to efficiently discover subdomains associated with a list of input domains. The tool utilizes the Certificate Transparency (CT) Logs to fetch subdomains from crt.sh and also leverages the Subfinder tool for even more comprehensive subdomain enumeration.
<img width="960" alt="subsnipe" src="https://github.com/TheeEclipse/SubSnipe/assets/97826144/7ffa2116-fa44-411c-9d6d-0160dd2c56b3">


# 🎩Key Features:
+ Utilizes Certificate Transparency (CT) Logs to fetch subdomains from crt.sh for the provided domains.
+ Integrates with Subfinder for additional comprehensive subdomain discovery.
+ Provides a clean and user-friendly command-line interface.
+ Utilizes tqdm for progress visualization during subdomain enumeration.
+ Outputs the discovered subdomains to an output file for further analysis.

# 🎩Installation
Install the python modules
+ requests: This module is used to send HTTP requests to fetch data from the crt.sh website.
+ json: This module is used to handle JSON data retrieved from the crt.sh API.
+ sys: This module is used to access command-line arguments and exit the program if the arguments are not provided correctly.
+ subprocess: This module is used to execute the Subfinder tool as a subprocess to perform additional subdomain enumeration.
+ tqdm: This module is used to display a progress bar during the subdomain enumeration process to indicate the progress to the user.
  
If you do not have them , install using:
+ ```pip install requests```
+ ```pip install tqdm```
+ Please note that subfinder is a separate tool and not a Python module. You need to install Subfinder separately by following the installation instructions for your operating system from the official Subfinder repository: https://github.com/projectdiscovery/subfinder
+ Make sure your subfinder is properlly installed or add its absolute path at:
 
  ``` subprocess.run(['subfinder', '-dL', input_file, '-o', output_file])``` in the python file.
  
+ Now clone the repo and ```cd``` into the new folder or just download the python file.
  
  Ready to go!!
   
# 🎩 Usage
```python3 script.py -f input_domains.txt -o output_subdomains.txt```

+ ```-f``` -  Specifies the .txt file with domains 
+ ```-o``` -  Specifies the .txt file where enumerated subdomains will be saved

# Contributions
If you find any issues, have feature requests, or want to improve the tool, feel free to open an issue or submit a pull request. Let's work together to enhance the tool's capabilities and make it even more useful for the community.

# Disclaimer:
SubSnipe is intended for ethical and authorized use only. The user is responsible for complying with all applicable laws and regulations during subdomain enumeration and recon activities. The authors of this tool are not liable for any misuse or unlawful use of the tool. Always obtain proper authorization before scanning or probing any target.


