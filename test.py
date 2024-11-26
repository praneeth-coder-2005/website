import requests

# Proxy configuration
PROXY = {
    "http": "http://moviesavingdrive12:ZmuVSycaVu@202.68.184.108:50100",
    "https": "http://moviesavingdrive12:ZmuVSycaVu@202.68.184.108:50100",
}

def resolve_final_url(short_url):
    """
    Recursively resolves a shortened URL to its true final destination using the proxy.
    """
    try:
        while True:
            print(f"Resolving the shortened URL: {short_url}")
            # Follow all redirects
            response = requests.get(short_url, proxies=PROXY, timeout=10, allow_redirects=False, verify=False)

            # Check if there is a redirection
            if response.is_redirect or response.is_permanent_redirect:
                short_url = response.headers.get("Location")
                if not short_url.startswith("http"):
                    # Handle relative redirects
                    from urllib.parse import urljoin
                    short_url = urljoin(response.url, short_url)
                print(f"Redirected to: {short_url}")
            else:
                print(f"Final URL reached: {response.url}")
                return response.url
    except requests.exceptions.RequestException as e:
        print(f"Error resolving the URL: {e}")
        return None

def main():
    print("Welcome to the URL Shortener Bypasser")
    print("Enter the shortened URL below. Type 'exit' to quit.")
    
    while True:
        short_url = input("Shortened URL: ").strip()
        
        if short_url.lower() == "exit":
            print("Exiting the bypasser.")
            break
        
        if short_url:
            final_url = resolve_final_url(short_url)
            if final_url:
                print(f"Final URL: {final_url}")
            else:
                print("Could not resolve the URL. Please try again.")

if __name__ == "__main__":
    main()
