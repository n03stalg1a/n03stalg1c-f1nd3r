n03stalg1c f1nd3r

n03stalg1c f1nd3r is a command-line tool designed to find, validate, and collect proxies from a variety of public sources. It supports multiple proxy types (HTTP, HTTPS, SOCKS4, SOCKS5) and allows you to export the working proxies into a .txt file for easy use.
Features

    Multiple Proxy Types Supported: Fetch and validate HTTP, HTTPS, SOCKS4, and SOCKS5 proxies.

    Comprehensive Proxy Sources: Retrieves proxies from 20+ sources, including popular proxy list websites and GitHub repositories with regularly updated lists.

    Proxy Validation: Automatically checks if the proxies are working by attempting to access a test URL.

    Beautiful CLI Interface: Offers a clean, aesthetically pleasing command-line interface with progress bars and color-coded outputs.

    Export Working Proxies: Exports validated proxies to a .txt file for easy use and future reference.

    Logging: Built-in logging system for tracking actions, errors, and proxy validation results.

Installation

Follow these steps to set up n03stalg1c f1nd3r on your machine:
1. Clone the repository:

git clone https://github.com/yourusername/n03stalg1c-f1nd3r.git

2. Navigate to the project folder:

cd n03stalg1c-f1nd3r

3. Install dependencies:

Make sure you have Python 3.6+ installed. Then, install the required libraries using pip:

pip install -r requirements.txt

4. Run the script:

Now, you can run the script from the command line:

python proxy_finder.py

Usage

Once the script is running, follow these steps:

    Select Proxy Type: Choose the proxy type you want (HTTP, HTTPS, SOCKS4, or SOCKS5).

    Fetching Proxies: The script will fetch proxies from over 20 sources.

    Proxy Validation: Each proxy is validated by attempting to fetch a test URL to ensure it works.

    Export Proxies: Once validated, the tool will ask if you want to export the working proxies to a .txt file.

Dependencies

    requests - For making HTTP requests and fetching proxy lists.

    beautifulsoup4 - For scraping proxy data from HTML pages.

    colorama - For adding color to the command-line interface.

    logging - For logging events and errors during execution.

These dependencies are listed in the requirements.txt file, and you can install them using the following command:

pip install -r requirements.txt

Example Output

When running the script, you will see output like this:

Welcome to n03stalg1c f1nd3r!

Please select the type of proxies you're interested in:
1. HTTP
2. HTTPS
3. SOCKS4
4. SOCKS5
Enter the number corresponding to your choice: 2

Searching for HTTPS proxies...
Found 50 HTTPS proxies.

Validating proxies...
[====================] 100% Complete

20 valid HTTPS proxies found.

Do you want to export the valid proxies to a TXT file? (y/n): y
Exporting proxies to 'proxies.txt'...
Proxies exported successfully to proxies.txt!

Contribution

Feel free to contribute! Here are some ways you can help improve n03stalg1c f1nd3r:

    Bug Reports: If you encounter bugs or issues, please open an issue with the details.

    Feature Requests: Suggest new features or improvements for the script.

    Code Contributions: Fork the repository and create pull requests to improve the tool.

Steps to contribute:

    Fork this repository.

    Create a new branch (git checkout -b feature-name).

    Make your changes and commit them (git commit -am 'Add new feature').

    Push to your forked repository (git push origin feature-name).

    Create a pull request to the main repository.

License

n03stalg1c f1nd3r is licensed under the MIT License. See the LICENSE file for more details.
Links

    GitHub Repository

    Issue Tracker
