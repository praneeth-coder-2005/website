import requests

# Proxy configuration
PROXY = {
    "http": "http://moviesavingdrive12:ZmuVSycaVu@202.68.184.108:50100",
    "https": "http://moviesavingdrive12:ZmuVSycaVu@202.68.184.108:50100",
}

def resolve_all_redirects(short_url):
    """
    Resolves a shortened URL and logs all redirections in the chain.
    """
    try:
        redirection_chain = []
        while True:
            print(f"Resolving the shortened URL: {short_url}")
            # Follow redirects manually to log each intermediate URL
            response = requests.get(short_url, proxies=PROXY, timeout=10, allow_redirects=False, verify=False)

            # Log the current URL
            redirection_chain.append(short_url)

            # Check for redirection
            if response.is_redirect or response.is_permanent_redirect:
                next_url = response.headers.get("Location")
                if not next_url.startswith("http"):
                    # Handle relative redirects
                    from urllib.parse import urljoin
                    next_url = urljoin(response.url, next_url)
                print(f"Redirected to: {next_url}")
                short_url = next_url
            else:
                # Final URL reached
                print(f"Final URL reached: {response.url}")
                redirection_chain.append(response.url)
                break

        return redirection_chain
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
            chain = resolve_all_redirects(short_url)
            if chain:
                print("\nRedirection Chain:")
                for idx, url in enumerate(chain, 1):
                    print(f"{idx}: {url}")
            else:
                print("Could not resolve the URL. Please try again.")

if __name__ == "__main__":
    main()
